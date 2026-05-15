import tkinter as tk
from tkinter import messagebox

# Backend Logic for Calculations
def calculate_result():
    try:
        number1 = float(entry_1.get())
        number2 = float(entry_2.get())
        op_type = operation_var.get()
        
        if op_type == "+":
            final_output = number1 + number2
        elif op_type == "-":
            final_output = number1 - number2
        elif op_type == "*":
            final_output = number1 * number2
        elif op_type == "/":
            if number2 != 0:
                final_output = number1 / number2
            else:
                messagebox.showerror("Math Error", "Division by zero is not allowed.")
                return
        
        result_display.config(text=f"Result: {final_output}", fg="#2ecc71")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numerical values.")

# GUI Layout Settings
app_window = tk.Tk()
app_window.title("Ubaidullah's Portfolio Project")
app_window.geometry("350x450")
app_window.configure(bg="#1a1a1a")

# Header Section
tk.Label(app_window, text="PROFESSIONAL CALCULATOR", font=("Verdana", 14, "bold"), 
         bg="#1a1a1a", fg="#ffffff").pack(pady=20)

# Input Fields
entry_1 = tk.Entry(app_window, font=("Arial", 12), justify="center")
entry_1.pack(pady=10)

entry_2 = tk.Entry(app_window, font=("Arial", 12), justify="center")
entry_2.pack(pady=10)

# Selection of Operations
operation_var = tk.StringVar(value="+")
frame_ops = tk.Frame(app_window, bg="#1a1a1a")
frame_ops.pack(pady=15)

for symbol in ["+", "-", "*", "/"]:
    tk.Radiobutton(frame_ops, text=symbol, variable=operation_var, value=symbol, 
                   bg="#1a1a1a", fg="#ffffff", font=("Arial", 12), 
                   selectcolor="#333333").pack(side="left", padx=5)

# Action Button
btn_calc = tk.Button(app_window, text="RUN CALCULATION", command=calculate_result, 
                     bg="#3498db", fg="white", font=("Arial", 10, "bold"), 
                     width=20, height=2)
btn_calc.pack(pady=25)

# Result Output
result_display = tk.Label(app_window, text="Result: 0", font=("Verdana", 12), 
                          bg="#1a1a1a", fg="#f1c40f")
result_display.pack(pady=10)

# Footer
tk.Label(app_window, text="Developed by Ubaidullah", font=("Arial", 8), 
         bg="#1a1a1a", fg="#555555").pack(side="bottom", pady=10)

app_window.mainloop()
