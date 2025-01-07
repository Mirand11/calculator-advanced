import tkinter as tk
from tkinter import messagebox

def press(key):
    if key == "=":
        try:
            result = eval(entry.get())
            history.insert(tk.END, f"{entry.get()} = {result}")
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(result))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    elif key == "C":
        entry.delete(0, tk.END)
    elif key == "←":
        current_text = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current_text[:-1])
    elif key == "%":
        try:
            value = float(entry.get()) / 100
            entry.delete(0, tk.END)
            entry.insert(tk.END, str(value))
        except Exception as e:
            messagebox.showerror("Error", "Invalid Input")
    else:
        entry.insert(tk.END, key)

def clear_history():
    history.delete(0, tk.END)

def toggle_theme():
    global dark_mode
    dark_mode = not dark_mode
    if dark_mode:
        root.configure(bg="#2C2C2C")
        entry.configure(bg="#3C3C3C", fg="white")
        history.configure(bg="#3C3C3C", fg="white")
        theme_button.configure(bg="#555555", fg="white", text="Light Mode")
        for btn in buttons_list:
            btn.configure(bg="#555555", fg="white", activebackground="#777777", activeforeground="white")
    else:
        root.configure(bg="white")
        entry.configure(bg="white", fg="black")
        history.configure(bg="white", fg="black")
        theme_button.configure(bg="#E0E0E0", fg="black", text="Dark Mode")
        for btn in buttons_list:
            btn.configure(bg="#F8F8F8", fg="black", activebackground="#E0E0E0", activeforeground="black")

# Create main window
root = tk.Tk()
root.title("Kalkulator GUI")
root.geometry("400x600")
root.configure(bg="white")

# Entry widget
entry = tk.Entry(root, font=("Arial", 24), bd=5, insertwidth=2, width=15, justify="right", bg="white", fg="black")
entry.grid(row=0, column=0, columnspan=4, pady=10, padx=10)

# History widget
history_label = tk.Label(root, text="History", font=("Arial", 12), bg="white", fg="black", anchor="w")
history_label.grid(row=1, column=0, columnspan=4, sticky="w", padx=10)

history_frame = tk.Frame(root, bg="white", bd=2, relief="groove")
history_frame.grid(row=2, column=0, columnspan=4, pady=5, padx=10, sticky="nsew")

history = tk.Listbox(history_frame, height=5, font=("Arial", 12), bg="white", fg="black", selectbackground="#E0E0E0")
history.pack(fill="both", expand=True)

clear_button = tk.Button(root, text="Clear History", font=("Arial", 12), bg="#F8F8F8", fg="black", command=clear_history)
clear_button.grid(row=3, column=0, columnspan=4, pady=5)

# Button layout
buttons = [
    ("C", 4, 0), ("←", 4, 1), ("%", 4, 2), ("/", 4, 3),
    ("7", 5, 0), ("8", 5, 1), ("9", 5, 2), ("*", 5, 3),
    ("4", 6, 0), ("5", 6, 1), ("6", 6, 2), ("-", 6, 3),
    ("1", 7, 0), ("2", 7, 1), ("3", 7, 2), ("+", 7, 3),
    ("0", 8, 0), (".", 8, 1), ("=", 8, 2),
]

buttons_list = []
for (text, row, col) in buttons:
    button = tk.Button(root, text=text, font=("Arial", 18), bg="#F8F8F8", fg="black", 
                       activebackground="#E0E0E0", activeforeground="black", command=lambda t=text: press(t))
    button.grid(row=row, column=col, sticky="nsew", padx=5, pady=5)
    buttons_list.append(button)

# Theme toggle button
dark_mode = False
theme_button = tk.Button(root, text="Dark Mode", font=("Arial", 12), bg="#E0E0E0", fg="black", command=toggle_theme)
theme_button.grid(row=9, column=0, columnspan=4, pady=10)

# Configure grid weights for responsive resizing
for i in range(10):
    root.grid_rowconfigure(i, weight=1)
for i in range(4):  # 4 columns for buttons
    root.grid_columnconfigure(i, weight=1)

# Run the application
root.mainloop()
