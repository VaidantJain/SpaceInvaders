import tkinter as tk


# Define colors used in the design
BG_COLOR = "#000"
TEXT_COLOR = "#fff"
ACCENT_COLOR = "#0f0"
SECONDARY_ACCENT = "#aaa"


class SignUpWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Sign Up")
        self.geometry("400x400")
        self.configure(bg=BG_COLOR)

        self.create_signup_form()

    def create_signup_form(self):
        # Sign-up title (using system font)
        signup_title = tk.Label(self, text="Sign Up", font=(None, 18), fg=ACCENT_COLOR, bg=BG_COLOR)
        signup_title.pack(pady=20)

        # Form container
        form_container = tk.Frame(self, bg=BG_COLOR)
        form_container.pack()

        # Username label and entry
        username_label = tk.Label(form_container, text="Username:", font=(None, 12), fg=TEXT_COLOR, bg=BG_COLOR)
        username_label.pack()
        username_entry = tk.Entry(form_container, font=(None, 12), bg="#333", fg=TEXT_COLOR, highlightthickness=0)
        username_entry.pack(pady=10)

        # Email label and entry (optional)
        email_label = tk.Label(form_container, text="Email:", font=(None, 12), fg=TEXT_COLOR, bg=BG_COLOR)
        email_label.pack()
        email_entry = tk.Entry(form_container, font=(None, 12), bg="#333", fg=TEXT_COLOR, highlightthickness=0)
        email_entry.pack(pady=10)

        # Password label and entry
        password_label = tk.Label(form_container, text="Password:", font=(None, 12), fg=TEXT_COLOR, bg=BG_COLOR)
        password_label.pack()
        password_entry = tk.Entry(form_container, show="*", font=(None, 12), bg="#333", fg=TEXT_COLOR, highlightthickness=0)
        password_entry.pack(pady=10)

        # Confirm password label and entry (optional)
        confirm_password_label = tk.Label(form_container, text="Confirm Password:", font=(None, 12), fg=TEXT_COLOR, bg=BG_COLOR)
        confirm_password_label.pack()
        confirm_password_entry = tk.Entry(form_container, show="*", font=(None, 12), bg="#333", fg=TEXT_COLOR, highlightthickness=0)
        confirm_password_entry.pack(pady=10)

        # Sign-up button (replace with appropriate action)
        signup_button = tk.Button(
            form_container, text="Sign Up", font=(None, 12, "bold"), bg=ACCENT_COLOR, fg=BG_COLOR, cursor="hand2"
        )
        signup_button.pack(pady=15)


# Run the main loop
root = SignUpWindow()
root.mainloop()
