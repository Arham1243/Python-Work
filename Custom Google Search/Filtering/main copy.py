import webbrowser
import pandas as pd
import tkinter as tk
from tkinter import ttk
import pyautogui
import time

def custom_yes_no_question():
    # Create a new top-level window
    dialog = tk.Toplevel()
    dialog.title("Confirmation")

    # Get the screen dimensions
    screen_width = dialog.winfo_screenwidth()
    screen_height = dialog.winfo_screenheight()

    # Set the position of the dialog box (left middle)
    x_position = 0
    y_position = int(screen_height / 2) - 50
    dialog.geometry(f"300x100+{x_position}+{y_position}")

    # Make sure the dialog appears in front of all other windows
    dialog.attributes("-topmost", True)

    # Create a label and buttons
    label = ttk.Label(dialog, text="Do you want to target this client?", wraplength=280)
    label.pack(pady=10)

    response = tk.BooleanVar()

    def on_yes():
        response.set(True)
        dialog.destroy()

    def on_no():
        response.set(False)
        dialog.destroy()

    button_frame = ttk.Frame(dialog)
    button_frame.pack(pady=5)

    yes_button = ttk.Button(button_frame, text="Yes", command=on_yes)
    yes_button.pack(side=tk.LEFT, padx=5)

    no_button = ttk.Button(button_frame, text="No", command=on_no)
    no_button.pack(side=tk.LEFT, padx=5)

    dialog.wait_window(dialog)
    return response.get()

# Read the Excel file into a DataFrame
excel_file = "others_accounts.xlsx"
df = pd.read_excel(excel_file)

# Initialize 'target' column if it doesn't exist
if 'target' not in df.columns:
    df['target'] = None

# Iterate through each URL in the DataFrame
for index, row in df.iterrows():
    url = row['business_url']
    
    # Open the URL in a web browser
    webbrowser.open(url)
    
    # Small delay to ensure the browser has time to open the URL
    time.sleep(5)
    
    # Ask the user whether to target this client
    response = custom_yes_no_question()
    df.at[index, 'target'] = 'Yes' if response else 'No'
    
    # Save the DataFrame to Excel after each update
    df.to_excel(excel_file, index=False)
    print(f"Updated and saved status for account {index + 1}/{len(df)}")

    # Close the current tab using pyautogui (Ctrl + W on Windows/Linux, Cmd + W on Mac)
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(1)  # Small delay to ensure the tab is closed before opening the next one

print("Process completed. Updated accounts saved to 'others_accounts.xlsx'.")
