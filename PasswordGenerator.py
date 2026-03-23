import tkinter as tk
import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;:,.<>?/~`"

def generate():
    try:
        number_of_passwords = int(entry.get())
        output.delete("1.0", tk.END)

        for _ in range(number_of_passwords):
            password_length = random.randint(14, 24)
            password = "".join(random.choice(characters) for _ in range(password_length))
            output.insert(tk.END, password + "\n")

    except ValueError:
        output.delete("1.0", tk.END)
        output.insert(tk.END, "Please enter a valid number.")

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

label = tk.Label(root, text="Number of passwords to generate:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Generate Passwords", command=generate)
button.pack(pady=10)

output = tk.Text(root, height=10, width=50)
output.pack(pady=10)

root.mainloop()