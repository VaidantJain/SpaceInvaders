import tkinter as tk
import smtplib  # Import smtplib for sending emails (replace with your email sending method)

# Define colors used in the design (same as login.py)
BG_COLOR = "#000"
TEXT_COLOR = "#fff"
ACCENT_COLOR = "#0f0"
SECONDARY_ACCENT = "#aaa"


class ForgotPasswordWindow(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("Forgot Password")
        self.geometry("400x300")
        self.configure(bg=BG_COLOR)

        self.create_forgot_password_form()

    def create_forgot_password_form(self):
        # Forgot password title
        forgot_password_title = tk.Label(
            self, text="Forgot Password", font=(None, 18), fg=ACCENT_COLOR, bg=BG_COLOR
        )
        forgot_password_title.pack(pady=20)

        # Form container
        form_container = tk.Frame(self, bg=BG_COLOR)
        form_container.pack()

        # Email label and entry
        email_label = tk.Label(form_container, text="Email:", font=(None, 12), fg=TEXT_COLOR, bg=BG_COLOR)
        email_label.pack()
        self.email_entry = tk.Entry(form_container, font=(None, 12), bg="#333", fg=TEXT_COLOR, highlightthickness=0)
        self.email_entry.pack(pady=10)

        # Submit button
        submit_button = tk.Button(
            form_container, text="Submit", font=(None, 12, "bold"), bg=ACCENT_COLOR, fg=BG_COLOR, cursor="hand2"
        )
        submit_button.pack(pady=15)
        submit_button.bind("<Button-1>", self.handle_submit_button)

        # Back button (optional)
        back_button = tk.Button(
            self, text="Back to Login", font=(None, 10), fg=SECONDARY_ACCENT, bg=BG_COLOR, cursor="hand2"
        )
        back_button.pack(pady=10)
        back_button.bind("<Button-1>", self.handle_back_button)

    def handle_submit_button(self, event):
        # Get email address from entry field
        email = self.email_entry.get()

        # (Replace with your actual email sending logic)
        # This is a basic example using smtplib (consider security best practices)
        sender_email = "your_email@example.com"  # Replace with your email address
        sender_password = "your_email_password"  # Replace with your email password (securely store)
        receiver_email = email  # Replace with logic to determine recipient email
        message = f"A password reset link has been sent to your email address: {receiver_email}.\n" \
                  f"If you did not request a password reset, please ignore this email."

        with smtplib.SMTP("smtp.example.com", 587) as server:  # Replace with your email server details
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, receiver_email, message)

        # Display success message
        messagebox = tk.messagebox.showinfo(
            title="Password Reset", message="A password reset link has been sent to your email address."
        )

    def handle_back_button(self, event):
        # Implement logic to close this window and open the login window (replace with your code)
        self.destroy()  # Close current window (Forgot Password)
        # Open Login window (replace with your actual login window creation code)
        login_window = LoginWindow()  # Assuming you have a LoginWindow class defined
        login_window.mainloop()


# Run the main loop (optional, if running this file independently)
# root = ForgotPasswordWindow()
# root.mainloop()
