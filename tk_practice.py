import tkinter as tk
from tkinter import messagebox
import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    elif discriminant == 0:
        x = -b / (2*a)
        return x
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return x1, x2

def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        result = solve_quadratic(a, b, c)
        if result is None:
            messagebox.showinfo("Result", "No real roots")
        else:
            if isinstance(result, tuple):
                messagebox.showinfo("Result", "Roots: x1 = {:.2f}, x2 = {:.2f}".format(result[0], result[1]))
            else:
                messagebox.showinfo("Result", "Root: x = {:.2f}".format(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid input")

# Create the main window
root = tk.Tk()
root.title("Quadratic Equation Solver")

# Set the width and height of the window
window_width = 700
window_height = 280
root.geometry(f"{window_width}x{window_height}")

# Create labels and entry widgets for coefficients
label_a = tk.Label(root, text="a:")
label_a.grid(row=0, column=0, sticky="e")

entry_a = tk.Entry(root, width=5)
entry_a.grid(row=0, column=1, sticky="w")

label_b = tk.Label(root, text="x� +")
label_b.grid(row=0, column=2)

entry_b = tk.Entry(root, width=5)
entry_b.grid(row=0, column=3)

label_c = tk.Label(root, text="x +")
label_c.grid(row=0, column=4)

entry_c = tk.Entry(root, width=5)
entry_c.grid(row=0, column=5)

label_equal = tk.Label(root, text="= 0")
label_equal.grid(row=0, column=6)

# Create a button to calculate the roots
calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=0, column=7, padx=5, pady=5, sticky="w")

# Configure grid to stretch content
for i in range(8):
    root.grid_columnconfigure(i, weight=1)
root.grid_rowconfigure(0, weight=1)

# Start the Tkinter event loop
root.mainloop()
