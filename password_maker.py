import tkinter as tk
from tkinter import messagebox
import random

letters = list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
numbers = list('0123456789')
symbols = list('!#$%&()*+')

class PasswordGeneratorGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        tk.Label(root, text="Welcome to the Password Generator!").grid(row=0, column=0, columnspan=2, pady=10)
        tk.Label(root, text="Number of letters: ").grid(row=1, column=0, sticky="e")
        tk.Label(root, text="Number of symbols: ").grid(row=2, column=0, sticky="e")
        tk.Label(root, text="Number of numbers: ").grid(row=3, column=0, sticky="e")

        self.entry_letters = tk.Entry(root)
        self.entry_symbols = tk.Entry(root)
        self.entry_numbers = tk.Entry(root)

        self.entry_letters.grid(row=1, column=1, pady=2)
        self.entry_symbols.grid(row=2, column=1, pady=2)
        self.entry_numbers.grid(row=3, column=1, pady=2)

        self.entry_letters.bind('<Return>', lambda event: self.entry_symbols.focus_set())
        self.entry_symbols.bind('<Return>', lambda event: self.entry_numbers.focus_set())
        self.entry_numbers.bind('<Return>', lambda event: self.generate_password())

        self.generate_button = tk.Button(root, text="Generate Password", command=self.generate_password)
        self.generate_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.password_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
        self.password_label.grid(row=5, column=0, columnspan=2)

    def generate_password(self):
        try:
            n_letters = int(self.entry_letters.get())
            n_symbols = int(self.entry_symbols.get())
            n_numbers = int(self.entry_numbers.get())
        except ValueError:
            messagebox.showerror("Input error", "Please enter valid integer values.")
            return

        password_list = []
        for _ in range(n_letters):
            password_list.append(random.choice(letters))
        for _ in range(n_symbols):
            password_list.append(random.choice(symbols))
        for _ in range(n_numbers):
            password_list.append(random.choice(numbers))

        random.shuffle(password_list)
        password = ''.join(password_list)
        self.password_label.config(text=f"Your password is: {password}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorGUI(root)
    root.mainloop()
