import tkinter as tk
from tkinter import messagebox

# Dummy function to simulate URL checking
def check_url():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Input Error", "Please enter a URL")
        return

    # Placeholder for the actual machine learning model prediction logic
    # This is a dummy condition for demonstration purposes
    if "phish" in url:
        result = "Phishing"
    else:
        result = "Legitimate"
    
    result_label.config(text=f"Result: {result}")

# Create the main window
root = tk.Tk()
root.title("Phishing Website Detector")

# Input Section
input_frame = tk.Frame(root, padx=10, pady=10)
input_frame.pack(pady=10)
tk.Label(input_frame, text="Enter the URL to check:").pack(side=tk.LEFT)
url_entry = tk.Entry(input_frame, width=50)
url_entry.pack(side=tk.LEFT, padx=10)
check_button = tk.Button(input_frame, text="Check URL", command=check_url)
check_button.pack(side=tk.LEFT)

# Result Section
result_frame = tk.Frame(root, padx=10, pady=10)
result_frame.pack(pady=10)
result_label = tk.Label(result_frame, text="Result: ", font=("Helvetica", 14))
result_label.pack()

# Footer Note
footer_note = tk.Label(root, text="This tool uses dummy logic for demonstration. Implement actual ML model for real results.", font=("Helvetica", 10))
footer_note.pack(pady=20)

# Run the main loop
root.mainloop()
