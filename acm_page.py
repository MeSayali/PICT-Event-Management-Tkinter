import tkinter as tk
from PIL import Image, ImageTk
import os

def open_acm_page():
    win = tk.Toplevel()
    win.title("ACM Chapter - PICT Student Organization")
    win.geometry("1000x850")
    win.configure(bg="#f5f5f5")

    base_path = os.path.dirname(os.path.abspath(__file__))

    # ---------------- HEADER ----------------
    header_frame = tk.Frame(win, bg="#4CAF50", height=100)  # Green header
    header_frame.pack(fill="x")
    
     

    # ACM Logo
    try:
        img_path = os.path.join(base_path, "assets", "ACM.png")
        logo_img = Image.open(img_path)
        logo_img = logo_img.resize((60, 60), Image.Resampling.LANCZOS)
        logo_photo = ImageTk.PhotoImage(logo_img)
        logo_label = tk.Label(header_frame, image=logo_photo, bg="#4CAF50")
        logo_label.image = logo_photo
        logo_label.place(x=30, y=35)
    except Exception as e:
        print("ACM image not loaded:", e)

    # Title Text
    tk.Label(header_frame, text="ACM Chapter", bg="#4CAF50", fg="white", font=("Helvetica", 20, "bold")).place(x=110, y=35)
    tk.Label(header_frame, text="PICT Student Organization", bg="#4CAF50", fg="white", font=("Helvetica", 12)).place(x=110, y=65)

    # ---------------- MAIN CONTENT ----------------
    content_frame = tk.Frame(win, bg="#f5f5f5")
    content_frame.pack(fill="both", expand=True, padx=30, pady=20)

    # LEFT SIDE
    left_frame = tk.Frame(content_frame, bg="#f5f5f5")
    left_frame.pack(side="left", fill="both", expand=True, padx=(0, 20))

    # About Section
    about_card = tk.Frame(left_frame, bg="white", bd=0, relief="solid")
    about_card.pack(fill="both", expand=False, pady=5)

    tk.Label(about_card, text="📘 About ACM Chapter", bg="white", font=("Helvetica", 14, "bold")).pack(anchor="w", padx=20, pady=(15, 5))
    about_text = (
        "The ACM Student Chapter at PICT is dedicated to advancing computing as a science and profession. "
        "We organize coding competitions, technical workshops, and guest lectures by industry experts. "
        "Our focus areas include algorithms, data structures, and competitive programming."
    )
    tk.Label(about_card, text=about_text, bg="white", font=("Helvetica", 11), wraplength=400, justify="left").pack(anchor="w", padx=20, pady=(0, 15))

    # What We Offer box
    offer_box = tk.Frame(about_card, bg="#f1f1f1", padx=15, pady=10)
    offer_box.pack(padx=15, pady=(0, 15), fill="x")

    tk.Label(offer_box, text="What We Offer:", font=("Helvetica", 11, "bold"), bg="#f1f1f1").pack(anchor="w")
    offers = [
        "• Regular workshops and training sessions",
        "• Networking opportunities with industry professionals",
        "• Hands-on experience with real-world projects",
        "• Certification and skill development programs",
        "• Leadership and teamwork opportunities"
    ]
    for offer in offers:
        tk.Label(offer_box, text=offer, font=("Helvetica", 10), bg="#f1f1f1").pack(anchor="w")

    # RIGHT SIDE
    right_frame = tk.Frame(content_frame, bg="#f5f5f5")
    right_frame.pack(side="right", fill="both", expand=True)

    tk.Label(right_frame, text="Upcoming Events", font=("Helvetica", 14, "bold"), bg="#f5f5f5").pack(anchor="w", pady=(0, 10))

    def create_event_card(parent, title, date, time, location, desc):
        card = tk.Frame(parent, bg="white", padx=15, pady=10)
        card.pack(fill="x", pady=10)

        header = tk.Frame(card, bg="white")
        header.pack(fill="x")

        tk.Label(header, text=title, font=("Helvetica", 12, "bold"), bg="white").pack(side="left")

        tag = tk.Label(header, text="Upcoming", bg="#4CAF50", fg="white", font=("Helvetica", 9, "bold"), padx=8, pady=2)
        tag.pack(side="right", padx=5)

        info = f"📅 {date}     ⏰ {time}     📍 {location}"
        tk.Label(card, text=info, font=("Helvetica", 10), bg="white").pack(anchor="w", pady=(5, 0))

        tk.Label(card, text=desc, font=("Helvetica", 10), bg="white", wraplength=300, justify="left").pack(anchor="w", pady=5)

        tk.Button(card, text="Register", bg="#4CAF50", fg="white", font=("Helvetica", 10, "bold"), padx=10, pady=1).pack(anchor="e")

    # Add events
    create_event_card(
        right_frame,
        title="Competitive Programming Bootcamp",
        date="9/15/2024",
        time="10:00 AM",
        location="Main Auditorium",
        desc="Intensive training on algorithms and problem-solving techniques."
    )

    create_event_card(
        right_frame,
        title="Industry Expert Talk: AI in Software Development",
        date="9/22/2024",
        time="9:00 AM",
        location="Seminar Hall B",
        desc="Guest lecture by senior software engineer from Microsoft."
    )

    # ---------------- ADDITIONAL CONTENT ----------------

    bottom_frame = tk.Frame(win, bg="#f5f5f5")
    bottom_frame.pack(fill="both", expand=True, padx=30, pady=(0, 10))

    # Certifications Offered
    certs_card = tk.Frame(bottom_frame, bg="white", padx=20, pady=15)
    certs_card.pack(fill="x", pady=10)

    tk.Label(certs_card, text="🎓 Certifications Offered", bg="white", font=("Helvetica", 13, "bold")).pack(anchor="w")
    certs_list = [
        "• Certificate of Participation in Workshops",
        "• Certification for Competitive Programming Challenges",
        "• Leadership Training Certifications",
    ]
    for cert in certs_list:
        tk.Label(certs_card, text=cert, font=("Helvetica", 10), bg="white").pack(anchor="w", pady=2)

    # Tools & Technologies
    tools_card = tk.Frame(bottom_frame, bg="white", padx=20, pady=15)
    tools_card.pack(fill="x", pady=10)

    tk.Label(tools_card, text="🛠 Tools & Technologies We Use", bg="white", font=("Helvetica", 13, "bold")).pack(anchor="w")
    tools_list = [
        "• C++, Python, Java",
        "• GitHub for collaboration",
        "• Online Judges: Codeforces, LeetCode, HackerRank",
        "• Algorithms & Data Structures",
    ]
    for tool in tools_list:
        tk.Label(tools_card, text=tool, font=("Helvetica", 10), bg="white").pack(anchor="w", pady=2)

    # Contact Us
    contact_card = tk.Frame(bottom_frame, bg="white", padx=20, pady=15)
    contact_card.pack(fill="x", pady=10)

    tk.Label(contact_card, text="📬 Contact Us", bg="white", font=("Helvetica", 13, "bold")).pack(anchor="w")
    tk.Label(contact_card, text="📧 Email: acmchapter@pict.edu", bg="white", font=("Helvetica", 10)).pack(anchor="w", pady=2)
    tk.Label(contact_card, text="🌐 Website: www.acmchapterpict.in", bg="white", font=("Helvetica", 10)).pack(anchor="w", pady=2)
    tk.Label(contact_card, text="📍 Location: PICT Campus, Pune", bg="white", font=("Helvetica", 10)).pack(anchor="w", pady=2)

    # Close Button
    tk.Button(win, text="Close", command=win.destroy, bg="#d9534f", fg="white", font=("Helvetica", 12)).pack(pady=10)


# ---------------- MAIN LAUNCHER ----------------
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    open_acm_page()
    root.mainloop()
