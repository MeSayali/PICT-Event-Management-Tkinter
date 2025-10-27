import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
import subprocess
from admin_login import open_admin_login  # Import the login window function

# ---------------- FUNCTION TO OPEN NEW CLUB PAGE (Fallback) ----------------
def open_club_page(club_name):
    """Fallback function if club script is missing."""
    win = tk.Toplevel()
    win.title(f"{club_name} - PICT Event Management")
    win.geometry("600x400")
    win.configure(bg="#f5f5f5")

    tk.Label(
        win,
        text=f"Welcome to {club_name}",
        font=("Helvetica", 16, "bold"),
        bg="#f5f5f5",
        fg="#333"
    ).pack(pady=30)

    tk.Label(
        win,
        text=f"This is the {club_name} page. Content will be added soon.",
        font=("Helvetica", 12),
        bg="#f5f5f5"
    ).pack(pady=10)

    tk.Button(
        win,
        text="Close",
        command=win.destroy,
        bg="#d9534f",
        fg="white"
    ).pack(pady=20)

# ---------------- HOMEPAGE FUNCTION ----------------
def show_homepage(root=None):
    if root is None:
        root = tk.Tk()
    else:
        root.deiconify()  # Restore if hidden

    root.title("PICT Event Management System")
    root.geometry("900x600")
    root.configure(bg="#f5f5f5")
    root.minsize(800, 600)

    root.grid_rowconfigure(1, weight=1)
    root.grid_columnconfigure(0, weight=1)

    base_path = os.path.dirname(os.path.abspath(__file__))

    if not hasattr(root, "images_cache"):
        root.images_cache = []

    # HEADER
    header = tk.Frame(root, bg="#5C5CE5", height=80)
    header.grid(row=0, column=0, sticky="nsew")
    header.grid_columnconfigure(1, weight=1)

    try:
        logo_img = Image.open(os.path.join(base_path, "assets", "pict.png"))
        logo_img = logo_img.resize((50, 50), Image.Resampling.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_img)
        root.images_cache.append(logo_photo)
        logo_label = tk.Label(header, image=logo_photo, bg="#5C5CE5")
        logo_label.grid(row=0, column=0, rowspan=2, padx=(15, 10), pady=10, sticky="w")
    except Exception as e:
        print("Logo load error:", e)
        logo_label = tk.Label(header, text="[Logo]", bg="#5C5CE5", fg="white", font=("Helvetica", 12))
        logo_label.grid(row=0, column=0, rowspan=2, padx=(15, 10), pady=10, sticky="w")

    title = tk.Label(header, text="PICT Event Management System", fg="white", bg="#5C5CE5",
                     font=("Helvetica", 18, "bold"))
    title.grid(row=0, column=1, sticky="w", pady=(10, 0))

    subtitle = tk.Label(header, text="Pune Institute of Computer Technology", fg="white", bg="#5C5CE5",
                        font=("Helvetica", 10))
    subtitle.grid(row=1, column=1, sticky="w", pady=(0, 10))

    try:
        admin_img = Image.open(os.path.join(base_path, "assets", "Homepage_admin.png"))
        admin_img = admin_img.resize((20, 20), Image.Resampling.LANCZOS)
        admin_photo = ImageTk.PhotoImage(admin_img)
        root.images_cache.append(admin_photo)
        admin_btn = tk.Button(header, text=" Admin Login", image=admin_photo, compound="left",
                              bg="#8c8cf0", fg="black", font=("Helvetica", 10, "bold"),
                              command=lambda: open_admin_login(root))
    except Exception as e:
        print("Admin image load error:", e)
        admin_btn = tk.Button(header, text="Admin Login", bg="#8c8cf0", fg="black", font=("Helvetica", 10, "bold"),
                              command=lambda: open_admin_login(root))

    admin_btn.grid(row=0, column=2, rowspan=2, padx=20, pady=20, sticky="e")

    # MAIN CONTENT
    main_frame = tk.Frame(root, bg="#f5f5f5")
    main_frame.grid(row=1, column=0, sticky="nsew")
    main_frame.grid_rowconfigure(2, weight=1)
    main_frame.grid_columnconfigure(0, weight=1)

    main_title = tk.Label(main_frame, text="Explore Student Clubs & Organizations", font=("Helvetica", 16, "bold"),
                          bg="#f5f5f5")
    main_title.grid(row=0, column=0, pady=(20, 5))

    description = tk.Label(
        main_frame,
        text="Join our vibrant community of student clubs.\nDiscover events, workshops, and activities that match your interests and help you grow both personally and professionally.",
        font=("Helvetica", 10),
        bg="#f5f5f5",
        justify="center"
    )
    description.grid(row=1, column=0, pady=(0, 20))

    canvas_frame = tk.Frame(main_frame, bg="#f5f5f5")
    canvas_frame.grid(row=2, column=0, sticky="nsew", padx=20, pady=10)

    canvas = tk.Canvas(canvas_frame, bg="#f5f5f5", highlightthickness=0)
    scrollbar = ttk.Scrollbar(canvas_frame, orient="vertical", command=canvas.yview)

    scrollable_frame = tk.Frame(canvas, bg="#f5f5f5")

    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="n")
    canvas.configure(yscrollcommand=scrollbar.set)

    canvas.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    scrollable_frame.grid_columnconfigure(0, weight=1)
    scrollable_frame.grid_columnconfigure(2, weight=1)

    center_frame = tk.Frame(scrollable_frame, bg="#f5f5f5")
    center_frame.grid(row=0, column=1, pady=10)

    # CLUB DATA
    clubs = [
        ("AWS Club", "Learn Cloud computing and AWS technologies through\nhands-on workshops.", "#d9e1f2", "AWS.png"),
        ("ACM Chapter", "Advance computing knowledge through coding competitions\nand tech talks.", "#c7e6c1", "ACM.png"),
        ("DebSoc", "Develop public speaking and debating skills through competitions", "#f5c7c7", "Debsoc.png"),
        ("Model UN", "Simulate United Nations proceedings and develop diplomacy skills.", "#e6c7f5", "model_un.png"),
        ("Cyber Cell", "Learn cyber security and ethical hacking through practical sessions", "#d9d9d9", "Cyber.png"),
        ("Cultural Committee", "Organize cultural events festivals and artistic performances.", "#f5f0b7", "cultural.png")
    ]

    def create_club_card(parent, club):
        title, desc, color, img_file = club
        card = tk.Frame(parent, bg=color, width=250, height=160, bd=1, relief="raised")
        card.pack_propagate(False)

        try:
            img_path = os.path.join(base_path, "assets", img_file)
            img = Image.open(img_path)
            img = img.resize((50, 50), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)
            root.images_cache.append(photo)
            img_label = tk.Label(card, image=photo, bg=color)
            img_label.pack(pady=5)
        except Exception as e:
            print(f"Error loading {img_file}: {e}")
            img_label = tk.Label(card, text="[Image]", bg=color)
            img_label.pack(pady=5)

        tk.Label(card, text=title, font=("Helvetica", 12, "bold"), bg=color).pack()
        tk.Label(card, text=desc, font=("Helvetica", 9), bg=color, wraplength=220, justify="center").pack()

        # Open respective club page script on click
        def open_club_script(script_name):
            try:
                subprocess.Popen(["python", script_name])
            except Exception as e:
                print(f"Failed to open {script_name}: {e}")

        club_scripts = {
            "AWS Club": "aws_page.py",
            "ACM Chapter": "acm_page.py",
            "DebSoc": "debsoc_page.py",
            "Model UN": "modelun_page.py",
            "Cyber Cell": "cybercell_page.py",
            "Cultural Committee": "cultural_page.py"
        }

        script_to_run = club_scripts.get(title)
        if script_to_run:
            card.bind("<Button-1>", lambda e: open_club_script(script_to_run))
            for child in card.winfo_children():
                child.bind("<Button-1>", lambda e: open_club_script(script_to_run))
        else:
            card.bind("<Button-1>", lambda e, name=title: open_club_page(name))
            for child in card.winfo_children():
                child.bind("<Button-1>", lambda e, name=title: open_club_page(name))

        return card

    for i, club in enumerate(clubs):
        card = create_club_card(center_frame, club)
        card.grid(row=i // 3, column=i % 3, padx=15, pady=15, sticky="n")

    return root


if __name__ == "__main__":
    app = show_homepage()
    app.mainloop()
