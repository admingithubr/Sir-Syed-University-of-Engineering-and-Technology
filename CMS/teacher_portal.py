import tkinter as tk
from tkinter import messagebox
from data_manager import load_data, save_data

def open_teacher_portal():
    def login():
        tid = entry_id.get()
        teachers = load_data('teachers.pkl')
        if tid not in teachers:
            messagebox.showerror("Error", "Teacher not found")
            return

        dashboard = tk.Toplevel(win)
        dashboard.title(f"Teacher Dashboard - {teachers[tid]['name']}")

        def input_data(field, filename):
            sid = entry_sid.get()
            value = entry_value.get()
            students = load_data('students.pkl')
            if sid not in students:
                messagebox.showerror("Error", "Student not found")
                return
            data = load_data(filename)
            data[sid] = value
            save_data(data, filename)
            messagebox.showinfo("Success", f"{field} updated")

        tk.Label(dashboard, text="Student ID").grid(row=0, column=0)
        entry_sid = tk.Entry(dashboard); entry_sid.grid(row=0, column=1)
        tk.Label(dashboard, text="Value").grid(row=1, column=0)
        entry_value = tk.Entry(dashboard); entry_value.grid(row=1, column=1)

        tk.Button(dashboard, text="Input Result", command=lambda: input_data("Result", "results.pkl")).grid(row=2, columnspan=2)
        tk.Button(dashboard, text="Input Attendance", command=lambda: input_data("Attendance", "attendance.pkl")).grid(row=3, columnspan=2)
        tk.Button(dashboard, text="Logout", command=dashboard.destroy).grid(row=4, columnspan=2, pady=10)

    win = tk.Toplevel()
    win.title("Teacher Login")
    tk.Label(win, text="Teacher ID").pack()
    entry_id = tk.Entry(win); entry_id.pack()
    tk.Button(win, text="Login", command=login).pack()
