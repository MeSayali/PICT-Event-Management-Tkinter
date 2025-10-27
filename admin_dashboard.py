import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os


def open_add_event_page(parent):
    # Create new top-level window
    add_event_win = tk.Toplevel(parent)
    add_event_win.title("Admin Panel - Add Event")
    add_event_win.geometry("500x420")  # smaller size
    add_event_win.configure(bg="#f5f5f5")

    base_path = os.path.dirname(os.path.abspath(__file__))

    # ---------- HEADER ----------
    header = tk.Frame(add_event_win, bg="#5C5CE5", height=60)
    header.pack(fill="x")

    try:
        logo_img = Image.open(os.path.join(base_path, "assets", "panel.png"))
        logo_img = logo_img.resize((35, 35), Image.Resampling.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_img)

        logo_label = tk.Label(header, image=logo_photo, bg="#5C5CE5")
        logo_label.image = logo_photo
        logo_label.pack(side="left", padx=15, pady=10)
    except Exception:
        logo_label = tk.Label(header, text="[Logo]", bg="#5C5CE5", fg="white", font=("Helvetica", 10))
        logo_label.pack(side="left", padx=15, pady=10)

    tk.Label(header, text="Add New Event", font=("Helvetica", 14, "bold"),
             fg="white", bg="#5C5CE5").pack(side="left", padx=10)

    # ---------- FORM ----------
    form_frame = tk.Frame(add_event_win, bg="white", bd=2, relief="groove")
    form_frame.pack(padx=20, pady=20, fill="both", expand=True)

    def add_field(row, text, widget):
        tk.Label(form_frame, text=text, bg="white",
                 font=("Helvetica", 10, "bold")).grid(row=row, column=0, sticky="w", pady=6, padx=10)
        widget.grid(row=row, column=1, sticky="ew", pady=6, padx=10)

    form_frame.grid_columnconfigure(1, weight=1)

    # Dropdown
    club_combo = ttk.Combobox(form_frame, values=[
        "AWS Club", "ACM Chapter", "DebSoc", "Model UN", "Cyber Cell", "Cultural Committee"
    ], state="readonly")
    add_field(0, "Select Club *", club_combo)

    # Title
    event_title = tk.Entry(form_frame)
    add_field(1, "Event Title *", event_title)

    # Date
    event_date = tk.Entry(form_frame)
    event_date.insert(0, "dd-mm-yyyy")
    add_field(2, "Date *", event_date)

    # Time
    event_time = tk.Entry(form_frame)
    event_time.insert(0, "--:--")
    add_field(3, "Time *", event_time)

    # Location
    event_location = tk.Entry(form_frame)
    event_location.insert(0, "e.g., Seminar Hall A")
    add_field(4, "Location *", event_location)

    # Description
    tk.Label(form_frame, text="Description", bg="white",
             font=("Helvetica", 10, "bold")).grid(row=5, column=0, sticky="nw", pady=6, padx=10)
    description = tk.Text(form_frame, height=3, width=25)
    description.grid(row=5, column=1, sticky="ew", pady=6, padx=10)

    # ---------- ADD BUTTON ----------
    def on_enter(e): add_btn.config(bg="#4040c8")
    def on_leave(e): add_btn.config(bg="#5C5CE5")

    add_btn = tk.Button(add_event_win, text="Add Event",
                        bg="#5C5CE5", fg="white",
                        font=("Helvetica", 11, "bold"), width=15)
    add_btn.pack(pady=10)
    add_btn.bind("<Enter>", on_enter)
    add_btn.bind("<Leave>", on_leave)


def open_admin_dashboard():
    dash = tk.Tk()
    dash.title("Admin Dashboard - PICT Event Management")
    dash.geometry("700x450")
    dash.configure(bg="#f5f5f5")

    base_path = os.path.dirname(os.path.abspath(__file__))

    # ---------- HEADER ----------
    header = tk.Frame(dash, bg="#5C5CE5", height=70)
    header.pack(fill="x")

    try:
        logo_img = Image.open(os.path.join(base_path, "assets", "panel.png"))
        logo_img = logo_img.resize((40, 40), Image.Resampling.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_img)

        logo_label = tk.Label(header, image=logo_photo, bg="#5C5CE5")
        logo_label.image = logo_photo
        logo_label.pack(side="left", padx=15, pady=10)
    except Exception:
        logo_label = tk.Label(header, text="[Logo]", bg="#5C5CE5", fg="white", font=("Helvetica", 12))
        logo_label.pack(side="left", padx=15, pady=10)

    tk.Label(header, text="Admin Dashboard", font=("Helvetica", 16, "bold"),
             fg="white", bg="#5C5CE5").pack(side="left", padx=10)

    # ---------- MAIN CONTENT ----------
    content = tk.Frame(dash, bg="#f5f5f5")
    content.pack(expand=True)

    tk.Label(content, text="Welcome, Admin!", font=("Helvetica", 14, "bold"),
             bg="#f5f5f5", fg="#333").pack(pady=30)

    # Add Events Button
    def on_enter_add(e): add_btn.config(bg="#4040c8")
    def on_leave_add(e): add_btn.config(bg="#5C5CE5")

    add_btn = tk.Button(content, text="➕ Add Events", width=20, bg="#5C5CE5",
                        fg="white", font=("Helvetica", 11, "bold"),
                        command=lambda: open_add_event_page(dash))
    add_btn.pack(pady=10)
    add_btn.bind("<Enter>", on_enter_add)
    add_btn.bind("<Leave>", on_leave_add)

    # Logout Button
    def on_enter_logout(e): logout_btn.config(bg="#c9302c")
    def on_leave_logout(e): logout_btn.config(bg="#d9534f")

    logout_btn = tk.Button(content, text="🚪 Logout", width=20, bg="#d9534f",
                           fg="white", font=("Helvetica", 11, "bold"),
                           command=dash.destroy)
    logout_btn.pack(pady=10)
    logout_btn.bind("<Enter>", on_enter_logout)
    logout_btn.bind("<Leave>", on_leave_logout)

    dash.mainloop()


# Run standalone
if __name__ == "__main__":
    open_admin_dashboard()
