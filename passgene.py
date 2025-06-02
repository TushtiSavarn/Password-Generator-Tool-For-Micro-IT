import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    try:
        length = int(length_var.get())
        if length <= 0:
            raise ValueError

        characters = ""
        if use_upper.get(): characters += string.ascii_uppercase
        if use_lower.get(): characters += string.ascii_lowercase
        if use_digits.get(): characters += string.digits
        if use_special.get(): characters += string.punctuation

        if not characters:
            messagebox.showwarning("Warning", "Please select at least one character set!")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        password_var.set(password)
    except:
        messagebox.showerror("Error", "Invalid input!")

def copy_to_clipboard():
    pyperclip.copy(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.config(bg="#f5f5f5")

length_var = tk.StringVar(value="12")
password_var = tk.StringVar()

tk.Label(root, text="Password Length:", bg="#f5f5f5").pack(pady=5)
tk.Entry(root, textvariable=length_var, width=10).pack()

use_upper = tk.BooleanVar(value=True)
use_lower = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_special = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=use_upper, bg="#f5f5f5").pack(anchor="w", padx=30)
tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=use_lower, bg="#f5f5f5").pack(anchor="w", padx=30)
tk.Checkbutton(root, text="Include Digits (0-9)", variable=use_digits, bg="#f5f5f5").pack(anchor="w", padx=30)
tk.Checkbutton(root, text="Include Symbols (!@#...)", variable=use_special, bg="#f5f5f5").pack(anchor="w", padx=30)

tk.Button(root, text="Generate Password", command=generate_password, bg="#4caf50", fg="white").pack(pady=10)
tk.Entry(root, textvariable=password_var, width=40, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack()

root.mainloop()
import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

def generate_password():
    try:
        length = int(length_var.get())
        if length <= 0:
            raise ValueError

        characters = ""
        if use_upper.get(): characters += string.ascii_uppercase
        if use_lower.get(): characters += string.ascii_lowercase
        if use_digits.get(): characters += string.digits
        if use_special.get(): characters += string.punctuation

        if not characters:
            messagebox.showwarning("Warning", "Please select at least one character set!")
            return

        password = ''.join(random.choice(characters) for _ in range(length))
        password_var.set(password)
    except:
        messagebox.showerror("Error", "Invalid input!")

def copy_to_clipboard():
    pyperclip.copy(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x350")
root.config(bg="#f5f5f5")

length_var = tk.StringVar(value="12")
password_var = tk.StringVar()

tk.Label(root, text="Password Length:", bg="#f5f5f5").pack(pady=5)
tk.Entry(root, textvariable=length_var, width=10).pack()

use_upper = tk.BooleanVar(value=True)
use_lower = tk.BooleanVar(value=True)
use_digits = tk.BooleanVar(value=True)
use_special = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Uppercase (A-Z)", variable=use_upper, bg="#f5f5f5").pack(anchor="w", padx=30)
tk.Checkbutton(root, text="Include Lowercase (a-z)", variable=use_lower, bg="#f5f5f5").pack(anchor="w", padx=30)
tk.Checkbutton(root, text="Include Digits (0-9)", variable=use_digits, bg="#f5f5f5").pack(anchor="w", padx=30)
tk.Checkbutton(root, text="Include Symbols (!@#...)", variable=use_special, bg="#f5f5f5").pack(anchor="w", padx=30)

tk.Button(root, text="Generate Password", command=generate_password, bg="#4caf50", fg="white").pack(pady=10)
tk.Entry(root, textvariable=password_var, width=40, font=("Arial", 12)).pack(pady=5)
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard).pack()

root.mainloop()
