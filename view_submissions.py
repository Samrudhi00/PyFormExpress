import tkinter as tk
from tkinter import ttk, messagebox
import json

class ViewSubmissionsForm(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.title("View Submissions")
        self.geometry("1000x600")
        self.configure(bg="#85C1E9")  # Set background color

        self.current_index = 0
        self.db_path = r"C:\Users\SAMRUDHI\source\repos\PyFormExpress\PyFormExpress\backend\src\db.json"
        self.submissions = self.load_all_submissions()

        self.lbl_submission = ttk.Label(self, text="", justify=tk.LEFT, wraplength=700, font=("Arial", 12), background="#f0f0f0")
        self.lbl_submission.pack(pady=20, padx=10)

        frame_buttons = ttk.Frame(self, style="TButton")
        frame_buttons.pack(pady=20)

        btn_previous = ttk.Button(frame_buttons, text="Previous (Ctrl+P)", command=self.show_previous, style="TButton")
        btn_previous.pack(side=tk.LEFT, padx=10)

        btn_next = ttk.Button(frame_buttons, text="Next (Ctrl+N)", command=self.show_next, style="TButton")
        btn_next.pack(side=tk.LEFT, padx=10)

        btn_edit = ttk.Button(frame_buttons, text="Edit (Ctrl+E)", command=self.edit_submission, style="TButton")
        btn_edit.pack(side=tk.LEFT, padx=10)

        btn_delete = ttk.Button(frame_buttons, text="Delete (Delete)", command=self.delete_submission, style="TButton")
        btn_delete.pack(side=tk.LEFT, padx=10)

        if self.submissions:
            self.display_submission(self.current_index)
        else:
            self.lbl_submission.config(text="No submissions available", foreground="red")

        # Keyboard shortcuts
        self.bind("<Control-p>", lambda event: self.show_previous())
        self.bind("<Control-n>", lambda event: self.show_next())
        self.bind("<Control-e>", lambda event: self.edit_submission())
        self.bind("<Delete>", lambda event: self.delete_submission())

    def load_all_submissions(self):
        try:
            with open(self.db_path, 'r') as f:
                submissions = json.load(f)
            return submissions
        except FileNotFoundError:
            messagebox.showerror("Error", f"Database file '{self.db_path}' not found")
            return []
        except json.JSONDecodeError:
            messagebox.showerror("Error", "Error decoding JSON data from 'db.json'")
            return []

    def display_submission(self, index):
        if self.submissions:
            submission = self.submissions[index]
            self.lbl_submission.config(
                text=f"ID: {submission['id']}\n"
                     f"Name: {submission['name']}\n"
                     f"Email: {submission['email']}\n"
                     f"Phone: {submission['phone']}\n"
                     f"GitHub: {submission['github_link']}\n"
                     f"Time: {submission['stopwatch_time']}",
                foreground="black"
            )

    def show_previous(self, event=None):
        if self.current_index > 0:
            self.current_index -= 1
            self.display_submission(self.current_index)

    def show_next(self, event=None):
        if self.current_index < len(self.submissions) - 1:
            self.current_index += 1
            self.display_submission(self.current_index)

    def edit_submission(self, event=None):
        if self.submissions:
            submission_to_edit = self.submissions[self.current_index]
            edit_form = EditSubmissionForm(self, submission_to_edit)
            edit_form.grab_set()
            self.wait_window(edit_form)  # Wait for the edit form to be closed

            # Update displayed submission after editing
            self.submissions = self.load_all_submissions()  # Reload submissions
            if self.submissions:
                self.display_submission(self.current_index)
            else:
                self.lbl_submission.config(text="No submissions available", foreground="red")

    def delete_submission(self, event=None):
        if self.submissions:
            submission_to_delete = self.submissions[self.current_index]
            confirm = messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this submission?")
            if confirm:
                try:
                    self.submissions.pop(self.current_index)
                    with open(self.db_path, 'w') as f:
                        json.dump(self.submissions, f, indent=4)
                    messagebox.showinfo("Success", "Submission deleted successfully")
                    self.submissions = self.load_all_submissions()
                    self.current_index = min(self.current_index, len(self.submissions) - 1)
                    if self.submissions:
                        self.display_submission(self.current_index)
                    else:
                        self.lbl_submission.config(text="No submissions available", foreground="red")
                except Exception as e:
                    messagebox.showerror("Error", f"Failed to delete submission: {e}")

class EditSubmissionForm(tk.Toplevel):
    def __init__(self, parent, submission_data):
        super().__init__(parent)
        self.parent = parent
        self.submission_data = submission_data
        self.title("Edit Submission")
        self.geometry("600x400")
        self.configure(bg="#85C1E9")

        self.heading_label = ttk.Label(self, text="Edit Submission", font=("Arial", 16, "bold"), background='#85C1E9', foreground='black')
        self.heading_label.pack(pady=10)

        self.create_widgets()
        self.load_submission_data()

        self.bind("<Control-s>", lambda event: self.update_submission())

    def create_widgets(self):
        style = ttk.Style(self)
        style.configure("TLabel", font=("Arial", 12), padding=5, background='#85C1E9', foreground='black')
        style.configure("TEntry", padding=10)
        style.configure("TButton", font=("Arial", 10), padding=10, background="#3498DB", foreground="black")

        input_frame = ttk.Frame(self, padding=20, style="TLabel")
        input_frame.pack(expand=True, fill=tk.BOTH)

        ttk.Label(input_frame, text=f"ID: {self.submission_data['id']}", anchor="e").grid(row=0, column=0, padx=10, pady=5, sticky=tk.E)

        ttk.Label(input_frame, text="Name:", anchor="e").grid(row=1, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_name = ttk.Entry(input_frame, width=40)
        self.entry_name.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        ttk.Label(input_frame, text="Email:", anchor="e").grid(row=2, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_email = ttk.Entry(input_frame, width=40)
        self.entry_email.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        ttk.Label(input_frame, text="Phone Number:", anchor="e").grid(row=3, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_phone = ttk.Entry(input_frame, width=40)
        self.entry_phone.grid(row=3, column=1, padx=10, pady=5, sticky=tk.W)

        ttk.Label(input_frame, text="GitHub Repo Link:", anchor="e").grid(row=4, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_github = ttk.Entry(input_frame, width=40)
        self.entry_github.grid(row=4, column=1, padx=10, pady=5, sticky=tk.W)

        ttk.Label(input_frame, text="Stopwatch Time:", anchor="e").grid(row=5, column=0, padx=10, pady=5, sticky=tk.E)
        self.entry_stopwatch_time = ttk.Entry(input_frame, width=40)
        self.entry_stopwatch_time.grid(row=5, column=1, padx=10, pady=5, sticky=tk.W)

        btn_frame = ttk.Frame(input_frame)
        btn_frame.grid(row=6, column=0, columnspan=2, pady=10)

        self.btn_update = ttk.Button(btn_frame, text="Update Submission (Ctrl+S)", command=self.update_submission)
        self.btn_update.grid(row=0, column=0, padx=10, pady=5)

        self.btn_cancel = ttk.Button(btn_frame, text="Cancel", command=self.destroy)
        self.btn_cancel.grid(row=0, column=1, padx=10, pady=5)

    def load_submission_data(self):
        self.entry_name.insert(0, self.submission_data.get('name', ''))
        self.entry_email.insert(0, self.submission_data.get('email', ''))
        self.entry_phone.insert(0, self.submission_data.get('phone', ''))
        self.entry_github.insert(0, self.submission_data.get('github_link', ''))
        self.entry_stopwatch_time.insert(0, self.submission_data.get('stopwatch_time', ''))

    def update_submission(self):
        name = self.entry_name.get()
        email = self.entry_email.get()
        phone = self.entry_phone.get()
        github_link = self.entry_github.get()
        stopwatch_time = self.entry_stopwatch_time.get()

        if not name or not email or not phone or not github_link or not stopwatch_time:
            messagebox.showerror("Error", "All fields are required")
            return

        updated_submission = {
            "id": self.submission_data['id'],
            "name": name,
            "email": email,
            "phone": phone,
            "github_link": github_link,
            "stopwatch_time": stopwatch_time
        }

        try:
            with open(self.parent.db_path, 'r+') as f:
                submissions = json.load(f)
                for i, submission in enumerate(submissions):
                    if submission['id'] == updated_submission['id']:
                        submissions[i] = updated_submission
                        break
                f.seek(0)
                json.dump(submissions, f, indent=4)
                f.truncate()

            messagebox.showinfo("Success", "Submission updated successfully")
            self.parent.submissions = self.parent.load_all_submissions()
            self.parent.display_submission(self.parent.current_index)
            self.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update submission: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    app = ViewSubmissionsForm(root)
    app.mainloop()
