import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operation = operation_var.get()
        
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
        elif operation == "Floor Division":
            if num2 != 0:
                result = num1 // num2
            else:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
        elif operation == "Modulus":
            result = num1 % num2
        elif operation == "Exponentiation":
            result = num1 ** num2
        else:
            messagebox.showerror("Error", "Please select a valid operation.")
            return
        
        result_label.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Please enter valid numbers.")

# GUI Setup
root = tk.Tk()
root.title("Calculator App")

frame = tk.Frame(root)
frame.pack(pady=20)

tk.Label(frame, text="Enter first number:").grid(row=0, column=0)
entry1 = tk.Entry(frame)
entry1.grid(row=0, column=1)

tk.Label(frame, text="Enter second number:").grid(row=1, column=0)
entry2 = tk.Entry(frame)
entry2.grid(row=1, column=1)

operations = ["Addition", "Subtraction", "Multiplication", "Division", "Floor Division", "Modulus", "Exponentiation"]
operation_var = tk.StringVar()
operation_var.set("Addition")

tk.Label(frame, text="Select operation:").grid(row=2, column=0)
tk.OptionMenu(frame, operation_var, *operations).grid(row=2, column=1)

tk.Button(frame, text="Calculate", command=calculate).grid(row=3, columnspan=2, pady=10)

result_label = tk.Label(frame, text="Result: ")
result_label.grid(row=4, columnspan=2)

root.mainloop()
