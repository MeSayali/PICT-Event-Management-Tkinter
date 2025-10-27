import tkinter as tk
from tkinter import messagebox
from admin_dashboard import open_admin_dashboard

def open_admin_login(homepage_root):
    """Open login window."""
    login_win = tk.Toplevel()
    login_win.title("Admin Login")
    login_win.geometry("350x220")
    login_win.configure(bg="#f5f5f5")

    tk.Label(login_win, text="Admin Login", font=("Helvetica", 14, "bold"), bg="#f5f5f5").pack(pady=10)

    tk.Label(login_win, text="Username:", bg="#f5f5f5").pack(pady=(10, 0))
    username_entry = tk.Entry(login_win, width=25)
    username_entry.pack()

    tk.Label(login_win, text="Password:", bg="#f5f5f5").pack(pady=(10, 0))
    password_entry = tk.Entry(login_win, width=25, show="*")
    password_entry.pack()

    def check_login():
        username = username_entry.get()
        password = password_entry.get()
        if username == "admin" and password == "admin123":  # Example credentials
            messagebox.showinfo("Login Successful", "Welcome, Admin!")
            login_win.destroy()
            homepage_root.destroy()   # Close homepage
            open_admin_dashboard()    # Open Dashboard
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    tk.Button(login_win, text="Login", width=15, bg="#5C5CE5", fg="white",
              command=check_login).pack(pady=15)
