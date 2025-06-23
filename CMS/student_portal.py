import tkinter as tk
from tkinter import messagebox
from data_manager import load_data

def open_student_portal():
    def login():
        sid = entry_id.get()
        students = load_data('students.pkl')
        if sid not in students:
            messagebox.showerror("Error", "Student not found")
            return

        result = load_data('results.pkl').get(sid, "Not available")
        attendance = load_data('attendance.pkl').get(sid, "Not available")
        transcript = load_data('transcripts.pkl').get(sid, "Not available")

        dashboard = tk.Toplevel(win)
        dashboard.title(f"Student Dashboard - {students[sid]['name']}")
        tk.Label(dashboard, text=f"Result: {result}").pack()
        tk.Label(dashboard, text=f"Attendance: {attendance}").pack()
        tk.Label(dashboard, text=f"Transcript: {transcript}").pack()
        tk.Button(dashboard, text="Logout", command=dashboard.destroy).pack(pady=10)

    win = tk.Toplevel()
    win.title("Student Login")
    tk.Label(win, text="Student ID").pack()
    entry_id = tk.Entry(win); entry_id.pack()
    tk.Button(win, text="Login", command=login).pack()
