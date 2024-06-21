import tkinter as tk
from tkinter import ttk
from create_submission import CreateSubmissionForm
from view_submissions import ViewSubmissionsForm

class MainForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PyFormExpress - Google Forms PythonForms")
        self.geometry("300x200")
        self.configure(bg='#85C1E9')  # Set background color

        style = ttk.Style()
        style.configure("TButton", font=("Arial", 12), padding=5, background="#3498DB", foreground="black")

        btn_view = ttk.Button(self, text="View Submissions (Ctrl+V)", command=self.open_view_submissions)
        btn_view.pack(pady=20)

        btn_create = ttk.Button(self, text="Create New Submission (Ctrl+N)", command=self.open_create_submission)
        btn_create.pack(pady=20)

        self.bind("<Control-v>", lambda event: self.open_view_submissions())
        self.bind("<Control-n>", lambda event: self.open_create_submission())

    def open_view_submissions(self):
        view_form = ViewSubmissionsForm(self)
        view_form.grab_set()

    def open_create_submission(self):
        create_form = CreateSubmissionForm(self)
        create_form.grab_set()

if __name__ == "__main__":
    app = MainForm()
    app.mainloop()
