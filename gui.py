import tkinter as tk
import random
import string
from vault.database import Database

class PasswordGeneratorGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Password Generator and Vault")

        self.password_length_label = tk.Label(self.window, text="Desired Password Length:")
        self.password_length_entry = tk.Entry(self.window)
        self.generate_password_button = tk.Button(self.window, text="Generate Password", command=self.generate_password)
        self.generated_password_label = tk.Label(self.window, text="Generated Password: ")

        self.username_label = tk.Label(self.window, text="Username:")
        self.username_entry = tk.Entry(self.window)
        self.ip_label = tk.Label(self.window, text="IP Address:")
        self.ip_entry = tk.Entry(self.window)
        self.domain_label = tk.Label(self.window, text="Domain Name:")
        self.domain_entry = tk.Entry(self.window)
        self.store_password_button = tk.Button(self.window, text="Store Password", command=self.store_password)
        self.stored_password_label = tk.Label(self.window, text="")

        self.remove_username_label = tk.Label(self.window, text="Username:")
        self.remove_username_entry = tk.Entry(self.window)
        self.remove_password_button = tk.Button(self.window, text="Remove Password", command=self.remove_password)
        self.removed_password_label = tk.Label(self.window, text="")

        self.create_layout()

        self.window.mainloop()

    def generate_password(self):
        length = int(self.password_length_entry.get())
        password = self._generate_password(length)
        self.generated_password_label.config(text="Generated Password: " + password)

    def store_password(self):
        username = self.username_entry.get()
        ip_address = self.ip_entry.get()
        domain_name = self.domain_entry.get()

        db = Database()
        db.add_password(username, self.generated_password_label.cget("text"), ip_address, domain_name)
        db.__del__()

        self.stored_password_label.config(text="Stored Password: " + self.generated_password_label.cget("text"))

    def remove_password(self):
        username = self.remove_username_entry.get()

        db = Database()
        db.remove_password(username)
        db.__del__()

        self.removed_password_label.config(text="Password removed for username: " + username)

    def create_layout(self):
        self.password_length_label.grid(row=0, column=0)
        self.password_length_entry.grid(row=0, column=1)
        self.generate_password_button.grid(row=1, column=0, columnspan=2)
        self.generated_password_label.grid(row=2, column=0, columnspan=2)

        self.username_label.grid(row=3, column=0)
        self.username_entry.grid(row=3, column=1)
        self.ip_label.grid(row=4, column=0)
        self.ip_entry.grid(row=4, column=1)
        self.domain_label.grid(row=5, column=0)
        self.domain_entry.grid(row=5, column=1)
        self.store_password_button.grid(row=6, column=0, columnspan=2)
        self.stored_password_label.grid(row=7, column=0, columnspan=2)

        self.remove_username_label.grid(row=8, column=0)
        self.remove_username_entry.grid(row=8, column=1)
        self.remove_password_button.grid(row=9, column=0, columnspan=2)
        self.removed_password_label.grid(row=10, column=0, columnspan=2)

    def _generate_password(self, length=16):
        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        return password

PasswordGeneratorGUI()
