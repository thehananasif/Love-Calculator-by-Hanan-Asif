import tkinter as tk
from tkinter import messagebox
import random

# Calculate love score (enhanced)
def calculate_love_score():
    name1 = entry_name1.get().strip().lower()
    name2 = entry_name2.get().strip().lower()

    if not name1 or not name2:
        messagebox.showerror("Error", "Please enter both names.")
        return

    # Calculate love score using enhanced method
    love_score = calculate_score(name1, name2)

    result_label.config(text=f"The love score between {name1.capitalize()} and {name2.capitalize()} is {love_score}%.")

    if love_score > 60:
        start_love_rain()

# Enhanced love score calculation
def calculate_score(name1, name2):
    combined_name = name1 + name2

    # Base calculation on ASCII values of characters, modulo 101 for percentage
    score = sum(ord(char) for char in combined_name) % 101

    # Adding randomness for uniqueness
    name1_random_factor = random.randint(1, 10)
    name2_random_factor = random.randint(1, 10)
    random_boost = random.randint(10, 30)

    score += name1_random_factor + name2_random_factor + random_boost

    # Normalize score to a max of 100%
    return min(score, 100)

# Function to simulate love rain (hearts falling from the top)
def start_love_rain():
    for _ in range(30):  # Number of hearts falling
        x = random.randint(0, 400)  # Random x position
        heart = canvas.create_text(x, 0, text="❤️", font=("Helvetica", 18), fill="red")
        fall_heart(heart)

# Function to animate falling hearts
def fall_heart(heart):
    def move():
        y = canvas.coords(heart)[1]
        if y < 300:  # Height limit
            canvas.move(heart, 0, 5)  # Move heart down
            canvas.after(50, move)  # Call move() every 50ms
        else:
            canvas.delete(heart)  # Delete heart when it reaches bottom

    move()

# Create GUI window
root = tk.Tk()
root.title("💖 Love Calculator of Hanan Asif 💖")
root.geometry("400x500")
root.configure(bg="misty rose")

# Header with elegant font and romantic colors
header = tk.Label(root, text="💘 Welcome to the Love Calculator 💘", font=("Lucida Calligraphy", 18, "bold"), bg="misty rose", fg="dark red")
header.pack(pady=20)

# Create labels with a romantic theme
label_name1 = tk.Label(root, text="💖 Your Name:", font=("Georgia", 14), bg="misty rose", fg="purple")
label_name1.pack(pady=5)
label_name2 = tk.Label(root, text="💖 Partner's Name:", font=("Georgia", 14), bg="misty rose", fg="purple")
label_name2.pack(pady=5)

# Create a frame for the input fields
input_frame = tk.Frame(root, bg="misty rose")
input_frame.pack(pady=10)

# Create entry fields with enhanced styling
entry_name1 = tk.Entry(input_frame, font=("Georgia", 14), bd=0, highlightthickness=2, highlightbackground="light pink", highlightcolor="red", relief="flat", insertbackground="purple")
entry_name1.pack(pady=5, padx=10, ipady=5)  # Extra padding for a more spacious feel
entry_name2 = tk.Entry(input_frame, font=("Georgia", 14), bd=0, highlightthickness=2, highlightbackground="light pink", highlightcolor="red", relief="flat", insertbackground="purple")
entry_name2.pack(pady=5, padx=10, ipady=5)  # Extra padding for a more spacious feel

# Create a beautiful rounded button for calculating love score
calculate_button = tk.Button(root, text="💞 Calculate Love Score 💞", font=("Helvetica", 14), bg="deep pink", fg="white", command=calculate_love_score, relief="solid", bd=3)
calculate_button.pack(pady=20)

# Result label with soft colors and elegant font
result_label = tk.Label(root, text="", font=("Lucida Calligraphy", 16), bg="misty rose", fg="dark red")
result_label.pack(pady=20)

# Canvas for love rain effect (falling hearts)
canvas = tk.Canvas(root, width=400, height=300, bg="misty rose", highlightthickness=0)
canvas.pack()

# Run the GUI
root.mainloop()
