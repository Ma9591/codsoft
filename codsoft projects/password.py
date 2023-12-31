import tkinter as tk
from tkinter import ttk
import secrets
import string

def generate_password():
    password_length = int(length_var.get())

    if password_length <= 0:
        result_var.set("Invalid length")
        return

    password_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(password_characters) for i in range(password_length))
    result_var.set(password)


app = tk.Tk()
app.title("Password Generator")
app.geometry("500x700")  # Set the window size

style = ttk.Style()
style.configure("TButton", font=("Helvetica", 14), padding=10)

instruction_label = tk.Label(app, text="Enter the password length:", font=("Helvetica", 14))
instruction_label.pack(pady=10)


length_var = tk.StringVar()
length_entry = ttk.Entry(app, textvariable=length_var, font=("Helvetica", 14), justify="center")
length_entry.pack(pady=10)


generate_button = ttk.Button(app, text="create Password", command=generate_password, style="TButton")
generate_button.pack(pady=10)


result_var = tk.StringVar()
result_label = tk.Label(app, textvariable=result_var, font=("Courier", 16), wraplength=350, justify="center", bd=5,
                        relief="solid")
result_label.pack(pady=10, padx=20, fill=tk.BOTH, expand=True)  # Make the label resizable

app.mainloop()