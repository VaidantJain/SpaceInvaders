from PIL import Image, ImageTk
import tkinter as tk
import pygame, sys
from button import Button

# Function to start the game (replace with your game logic)
def start_game():
    print("Starting the game...")  # Replace with actual game start logic

# Function to handle Sign Up/Login (replace with your implementation)
def signup_login():
    # Prompt user for signup or login and handle accordingly
    print("Sign Up/Login menu")  # Replace with actual signup/login logic

# Function to quit the application
def quit_game():
    root.destroy()  # Close the Tkinter window

# Constants for window size
SCREEN_WIDTH = 750
SCREEN_HEIGHT = 700

# Create the main window
root = tk.Tk()
root.title("Space Invaders")
root.configure(bg="black")

# Set window size
root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
# Load the Space Invaders logo image (replace with your image path)
try:
  image = Image.open("1_eN0rNuj5RgXOcr69MdbtcA.png")  # Replace with your image path
  max_width = 750  # Adjust this value to fit your window width
  max_height = 700  # Adjust this value to fit your window height
  image = image.resize((max_width, max_height), Image.LANCZOS)
  logo_image = ImageTk.PhotoImage(image=image)

except (IOError, tk.TclError) as e:
    print(f"Error loading image: {e}")
    logo_image = None  # Set logo_image to None if loading fails

if logo_image is not None:
  logo_label = tk.Label(root, image=logo_image)
  logo_label.pack()


# Start the Tkinter main loop
root.mainloop()
