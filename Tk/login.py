import tkinter as tk
from forgot import ForgotPasswordWindow

# Define colors used in the design
BG_COLOR = "#000"
TEXT_COLOR = "#fff"
ACCENT_COLOR = "#0f0"
SECONDARY_ACCENT = "#aaa"


class LoginWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Login")
        self.geometry("400x400")
        self.configure(bg=BG_COLOR)

        # Create the login form section
        self.login_section = tk.Frame(self, bg=BG_COLOR)
        self.login_section.pack(pady=40)

        self.create_login_form(self.login_section)

    def create_login_form(self, parent):
        # Login title (using system font)
        login_title = tk.Label(parent, text="Login", font=(None, 18), fg=ACCENT_COLOR, bg=BG_COLOR)
        login_title.pack(pady=20)

        # Form container
        form_container = tk.Frame(parent, bg=BG_COLOR)
        form_container.pack()

        # Username and password input fields (replace with Entry widgets)
        username_label = tk.Label(form_container, text="Username:", font=(None, 12), fg=TEXT_COLOR, bg=BG_COLOR)
        username_label.pack()
        username_entry = tk.Entry(form_container, font=(None, 12), bg="#333", fg=TEXT_COLOR, highlightthickness=0)
        username_entry.pack(pady=10)

        password_label = tk.Label(form_container, text="Password:", font=(None, 12), fg=TEXT_COLOR, bg=BG_COLOR)
        password_label.pack()
        password_entry = tk.Entry(form_container, show="*", font=(None, 12), bg="#333", fg=TEXT_COLOR, highlightthickness=0)
        password_entry.pack(pady=10)

        # Login button
        login_button = tk.Button(
            form_container, text="Login", font=(None, 12, "bold"), bg=ACCENT_COLOR, fg=BG_COLOR, cursor="hand2"
        )
        login_button.pack(pady=15)

        # Links (replace with Label or Button widgets)
        links_frame = tk.Frame(form_container, bg=BG_COLOR)
        links_frame.pack()

        # Forgot Password with underline and click event (optional)
        forgot_password_link = tk.Label(
            links_frame,
            text="Forgot Password?",
            font=(None, 10),
            fg=SECONDARY_ACCENT,
            bg=BG_COLOR,
            cursor="hand2",
            underline=True,  # Optional: Underline for link appearance
        )
        forgot_password_link.pack(side=tk.LEFT)

        forgot_password_link.pack(side=tk.LEFT)
        forgot_password_link.bind(
            "<Button-1>",
            lambda event: ForgotPasswordWindow().mainloop()  # Assuming ForgotPasswordWindow is defined
        )

        signup_link = tk.Label(links_frame, text="Sign Up", font=(None, 10, "bold"), fg=ACCENT_COLOR, bg=BG_COLOR, cursor="hand2")
        signup_link.pack(side=tk.RIGHT)

        def handle_forgot_password(self, event):
            forgot_password_window = ForgotPasswordWindow()
            forgot_password_window.mainloop()  # Run the forgot password window loop
        # Bind click event to defined function (optional)



# Run the main loop
root = LoginWindow()
root.mainloop()
