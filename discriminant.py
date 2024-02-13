import tkinter as tk
from tkinter import messagebox
import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return "Нету корней"
    elif discriminant == 0:
        x = -b / (2*a)
        return "Один корень:\nx = {:.2f}".format(x)
    else:
        x1 = (-b + math.sqrt(discriminant)) / (2*a)
        x2 = (-b - math.sqrt(discriminant)) / (2*a)
        return "2 корня:\nx1 = {:.2f},\nx2 = {:.2f}".format(x1, x2)

def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())

        text_result.config(state=tk.NORMAL)
        text_result.delete('1.0', tk.END)
        
        text_result.insert(tk.END, "Решение:\n")
        
        result = solve_quadratic(a, b, c)

        text_result.insert(tk.END, result)
        
        text_result.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Ошибка")



root = tk.Tk()
root.geometry("700x380")
root.title("Quadratic Equation Solver")

entry_a = tk.Entry(root, width=10, font=("Arial", 14))
entry_a.grid(row=1, column=1)

label_b = tk.Label(root, text="x²+", font=("Arial", 14))
label_b.grid(row=1, column=2)
entry_b = tk.Entry(root, width=10, font=("Arial", 14))
entry_b.grid(row=1, column=3)

label_c = tk.Label(root, text="x+", font=("Arial", 14))
label_c.grid(row=1, column=4)
entry_c = tk.Entry(root, width=10, font=("Arial", 14))
entry_c.grid(row=1, column=5)

label_c = tk.Label(root, text="=0", font=("Arial", 14))
label_c.grid(row=1, column=6)

calculate_button = tk.Button(root, text="Calculate", bg="green", command=calculate, width=15, height=2, font=("Arial", 14))
calculate_button.grid(row=1, column=7, padx=5, pady=5)

label_solution = tk.Label(root, text="Решение функции", bg="blue", fg="green", font=("Arial", 16, "bold"))
label_solution.grid(row=0, column=3)

text_result = tk.Text(root, bg="yellow", width=60, height=5, font=("Arial", 12), state=tk.DISABLED)
text_result.grid(row=2, column=1, columnspan=7, padx=10, pady=10)

root.mainloop()
