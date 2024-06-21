import tkinter as tk
from tkinter import ttk, messagebox
import requests
import time

class CreateSubmissionForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("Create New Submission")
        self.configure(bg='#85C1E9')  # Set background color

        self.heading_label = ttk.Label(self, text="Wow!! We are adding a new submission!!", font=("Arial", 16, "bold"), background='#85C1E9', foreground='black')
        self.heading_label.pack(pady=10)

        self.create_widgets()

        # Center window and set initial size
        self.update_window_size()

        # Bind event to update window size if the window is resized
        self.bind("<Configure>", lambda e: self.update_window_size())

        self.stopwatch_running = False
        self.stopwatch_start_time = 0
        self.stopwatch_elapsed_time = 0

        self.bind("<Control-t>", lambda event: self.toggle_stopwatch())
        self.bind("<Control-s>", lambda event: self.submit_form())

    def create_widgets(self):
        style = ttk.Style(self)
        style.configure("TLabel", font=("Arial", 12), padding=5, background='#85C1E9', foreground='black')
        style.configure("TEntry", padding=10)
        style.configure("TButton", font=("Arial", 10), padding=10, background="#3498DB", foreground="black")

        input_frame = ttk.Frame(self, padding=20, style="TLabel")
        input_frame.pack(expand=True, fill=tk.BOTH)

        # Name
        ttk.Label(input_frame, text="Name:", anchor="e").grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_name = ttk.Entry(input_frame, width=40)
        self.entry_name.grid(row=0, column=1, padx=10, pady=5, sticky=tk.W)

        # Email
        ttk.Label(input_frame, text="Email:", anchor="e").grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_email = ttk.Entry(input_frame, width=40)
        self.entry_email.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        # Phone Number
        ttk.Label(input_frame, text="Phone Number:", anchor="e").grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_phone = ttk.Entry(input_frame, width=40)
        self.entry_phone.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        # GitHub Repo Link
        ttk.Label(input_frame, text="GitHub Repo Link:", anchor="e").grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_github = ttk.Entry(input_frame, width=40)
        self.entry_github.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

        # Stopwatch and Buttons
        self.lbl_stopwatch = ttk.Label(input_frame, text="Stopwatch: 0 min 0 sec")
        self.lbl_stopwatch.grid(row=4, column=1, padx=10, pady=10, sticky=tk.W)

        btn_frame = ttk.Frame(input_frame)
        btn_frame.grid(row=5, column=0, columnspan=2, pady=10)

        self.btn_start_pause = ttk.Button(btn_frame, text="Start (Ctrl+T)", command=self.toggle_stopwatch)
        self.btn_start_pause.grid(row=0, column=0, padx=10, pady=5)

        self.btn_submit = ttk.Button(btn_frame, text="Submit (Ctrl+S)", command=self.submit_form)
        self.btn_submit.grid(row=0, column=1, padx=10, pady=5)

    def toggle_stopwatch(self, event=None):
        if self.stopwatch_running:
            self.stopwatch_running = False
            self.stopwatch_elapsed_time += time.time() - self.stopwatch_start_time
            self.btn_start_pause.config(text="Start (Ctrl+T)")
        else:
            self.stopwatch_running = True
            self.stopwatch_start_time = time.time()
            self.btn_start_pause.config(text="Pause (Ctrl+T)")
            self.update_stopwatch()

    def update_stopwatch(self):
        if self.stopwatch_running:
            elapsed = time.time() - self.stopwatch_start_time + self.stopwatch_elapsed_time
            minutes = int(elapsed // 60)
            seconds = int(elapsed % 60)
            self.lbl_stopwatch.config(text=f"Stopwatch: {minutes} min {seconds} sec")
            self.after(1000, self.update_stopwatch)

    def submit_form(self, event=None):
        if not self.entry_name.get() or not self.entry_email.get() or not self.entry_phone.get() or not self.entry_github.get():
            messagebox.showerror("Error", "All fields are required")
            return

        data = {
            "name": self.entry_name.get(),
            "email": self.entry_email.get(),
            "phone": self.entry_phone.get(),
            "github_link": self.entry_github.get(),
            "stopwatch_time": int(time.time() - self.stopwatch_start_time + self.stopwatch_elapsed_time)
        }

        try:
            response = requests.post('http://localhost:3000/submit', json=data)
            response.raise_for_status()
            messagebox.showinfo("Success", "Submission successful")
        except requests.exceptions.RequestException as e:
            messagebox.showerror("Error", f"Failed to submit form: {e}")

    def update_window_size(self):
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        window_width = int(screen_width * 0.4)  # Adjust as needed
        window_height = int(screen_height * 0.6)  # Adjust as needed

        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2

        self.geometry(f'{window_width}x{window_height}+{x_coordinate}+{y_coordinate}')


if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    app = CreateSubmissionForm(root)
    app.mainloop()
