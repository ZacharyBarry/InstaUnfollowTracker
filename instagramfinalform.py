import json
import tkinter as tk
import webbrowser
from tkinter import filedialog, font as tkfont

# Initialize paths to None
followers_file_path = None
following_file_path = None

# Initialize data structures
followers_data = []
following_data = {"relationships_following": []}
followers = set()
following = set()
not_following_back = []

# Function to load JSON data from files
def load_json(file_path):
    with open(file_path, 'r') as f:
        return json.load(f)

# Function to select and load followers JSON file
def select_followers_file():
    global followers_file_path, followers_data, followers
    followers_file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if followers_file_path:
        followers_data = load_json(followers_file_path)
        followers = {user["string_list_data"][0]["value"] for user in followers_data}
        if following_file_path:
            find_not_following_back()
            update_display()

# Function to select and load following JSON file
def select_following_file():
    global following_file_path, following_data, following
    following_file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
    if following_file_path:
        following_data = load_json(following_file_path)
        following = {user["string_list_data"][0]["value"] for user in following_data["relationships_following"]}
        if followers_file_path:
            find_not_following_back()
            update_display()

# Function to find users not following back
def find_not_following_back():
    global not_following_back
    not_following_back = sorted(following - followers)

# Function to handle link click, remove user from list, and open profile in browser
def handle_click(user):
    global not_following_back
    if user in not_following_back:
        not_following_back.remove(user)
        update_display()
        profile_url = f"https://www.instagram.com/{user}/"
        webbrowser.open(profile_url)

# Update the display of the list
def update_display():
    for widget in canvas_frame.winfo_children():
        widget.destroy()

    # Create a frame to center the list
    list_frame = tk.Frame(canvas_frame, bg="#1e1e1e")
    list_frame.pack(side="top", fill="both", expand=True, padx=20, pady=20)

    # Define grid size and spacing
    max_columns = 3
    padding_x = 20
    padding_y = 20

    for i, user in enumerate(not_following_back, start=1):
        row = (i - 1) // max_columns
        column = (i - 1) % max_columns
        profile_url = f"https://www.instagram.com/{user}/"
        text = f"{i}. {user}"
        link = tk.Label(list_frame, text=text, fg="#ffffff", cursor="hand2", bg="#2c2c2c", font=("Helvetica Neue", 14),
                        relief="flat", padx=10, pady=5, borderwidth=1, highlightbackground="#444444", highlightcolor="#444444")
        link.grid(row=row, column=column, padx=padding_x, pady=padding_y, sticky="w")
        link.bind("<Button-1>", lambda e, user=user: handle_click(user))

    # Update the scroll region of the canvas
    canvas.configure(scrollregion=canvas.bbox("all"))

# Scroll up or down with mouse wheel
def on_mouse_wheel(event):
    canvas.yview_scroll(-1 * (event.delta // 120), "units")

# Create the main window
root = tk.Tk()
root.title("Not Following Back List")

# Set the main window background color
root.configure(bg="#1e1e1e")

# Create a canvas and a scrollbar
canvas = tk.Canvas(root, bg="#1e1e1e", highlightthickness=0)
scrollbar = tk.Scrollbar(root, orient="vertical", command=canvas.yview, bg="#333333", troughcolor="#1e1e1e", activebackground="#555555")
scrollbar_horizontal = tk.Scrollbar(root, orient="horizontal", command=canvas.xview, bg="#333333", troughcolor="#1e1e1e", activebackground="#555555")

# Create a frame inside the canvas to hold the profile links
canvas_frame = tk.Frame(canvas, bg="#1e1e1e")

# Add the frame to the canvas
canvas.create_window((0, 0), window=canvas_frame, anchor="nw")

# Configure the scrollbar and canvas
scrollbar.config(command=canvas.yview)
scrollbar_horizontal.config(command=canvas.xview)
canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")
scrollbar_horizontal.pack(side="bottom", fill="x")

# Bind the mouse wheel event to the canvas
root.bind_all("<MouseWheel>", on_mouse_wheel)

# Add a title at the top
title = tk.Label(root, text="I ain't no fan of you", font=("Brush Script MT", 30), fg="#b3b3b3", bg="#1e1e1e")
title.pack(side="top", fill="x", pady=20)

# Add buttons to select JSON files
button_frame = tk.Frame(root, bg="#1e1e1e")
button_frame.pack(side="top", pady=10)

select_followers_button = tk.Button(button_frame, text="Select Followers JSON", command=select_followers_file, bg="#333333", fg="#ffffff")
select_followers_button.pack(side="left", padx=10)

select_following_button = tk.Button(button_frame, text="Select Following JSON", command=select_following_file, bg="#333333", fg="#ffffff")
select_following_button.pack(side="left", padx=10)

# Update the canvas scroll region and ensure the frame resizes properly
canvas_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

root.mainloop()
