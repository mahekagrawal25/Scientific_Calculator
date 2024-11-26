import tkinter as tk
import math

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("315x475")
        self.root.resizable(False, False)
        self.root.configure(bg="#292F36")

        self.display = tk.Entry(root, font=("Arial", 20), justify="right", bd=5)
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew" )

        self.entries_label = tk.Label(root, text="Past 5 Entries:", font=("Arial", 12), bg="#74CDD1")
        self.entries_label.grid(row=1, column=0, columnspan=4, sticky="nsew")

        self.entries_text = tk.Text(root, height=5, width=30, font=("Arial", 12), bd=5, bg="#FAF5F1")
        self.entries_text.grid(row=2, column=0, columnspan=4, sticky="nsew")

        buttons1 = [
            ("AC", 3, 0), ("=", 3, 1), ("⌫", 3, 2), ("History", 3, 3),
        ]
       
        buttons2 = [
            ("7", 4, 0), ("8", 4, 1), ("9", 4, 2),
            ("4", 5, 0), ("5", 5, 1), ("6", 5, 2),
            ("1", 6, 0), ("2", 6, 1), ("3", 6, 2),
            (".", 7, 0), ("0", 7, 1)
            ]
       
        buttons3 = [
            ("*", 4, 3), ("-", 5, 3), ("+", 6, 3),
            (".", 7, 0), ("%", 7, 2), ("/", 7, 3)
            ]
       
        buttons4 = [
            ("sin", 8, 0), ("cos", 8, 1), ("tan", 8, 2), ("n!", 8, 3),
            ("π", 9, 0), ("e", 9, 1), ("x^2", 9, 2), ("ln", 9, 3),
            ]
       
        for btn_text, row, col in buttons1:
            button = tk.Button(root, text=btn_text, font=("Arial", 16), bd=3, bg="#FFEECC",
                                command=lambda text=btn_text: self.on_button_click(text))
            button.grid(row=row, column=col, sticky="nsew")
           
        for btn_text, row, col in buttons2:
            button = tk.Button(root, text=btn_text, font=("Arial", 16), bd=3, bg="#FFDDCC",
                                command=lambda text=btn_text: self.on_button_click(text))
            button.grid(row=row, column=col, sticky="nsew")
           
        for btn_text, row, col in buttons3:
            button = tk.Button(root, text=btn_text, font=("Arial", 16), bd=3, bg="#FFCCCC",
                                command=lambda text=btn_text: self.on_button_click(text))
            button.grid(row=row, column=col, sticky="nsew")
           
        for btn_text, row, col in buttons4:
            button = tk.Button(root, text=btn_text, font=("Arial", 16), bd=3, bg="#FFBBCC",
                                command=lambda text=btn_text: self.on_button_click(text))
            button.grid(row=row, column=col, sticky="nsew")

        self.entries = []

    def on_button_click(self, text):
        if text == "AC":
            self.display.delete(0, tk.END)
        elif text == "⌫":
            current_text = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(0, current_text[:-1])
        elif text == "=":
             try:
                 expression=self.display.get()
                 
                 if "%" in expression:
                     x, y= expression.split("%")
                     result = float(x)/100 * float(y)
                     self.display.delete(0, tk.END)
                     self.display.insert(tk.END, str(result))
                 
                 else: 
                     result = eval(self.display.get())
                     self.entries.append(result)
                     self.display.delete(0, tk.END)
                     self.display.insert(tk.END, str(result))
                 
                     
             except:
                 self.display.delete(0, tk.END)
                 self.display.insert(tk.END, "Error")
        elif text == "History":
            if self.entries:
                self.update_entries_text()
            else:
                self.entries_text.delete("1.0", tk.END)
                self.entries_text.insert(tk.END, "No past entries.")
        elif text == "n!":
            try:
                num = int(self.display.get())
                if num < 0:
                    raise ValueError
                elif num > 12:
                    raise OverflowError
                result = math.factorial(num)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except ValueError:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error: Negative number!")
            except OverflowError:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error: Number too large!")
        elif text == "sin":
            try:
                num = float(self.display.get())
                result = math.sin(num)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except ValueError:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error: Invalid input!")
        elif text == "cos":
            try:
                num = float(self.display.get())
                result = math.cos(num)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except ValueError:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error: Invalid input!")
        elif text == "tan":
            try:
                num = float(self.display.get())
                result = math.tan(num)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except ValueError:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error: Invalid input!")
        elif text == "π":
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(math.pi)[:8])  # Display pi up to 6 digits
        elif text == "e":
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, str(math.e)[:8])  # Display e up to 6 digits
        elif text == "x^2":
            try:
                num = float(self.display.get())
                result = num ** 2
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except ValueError:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error: Invalid input!")
        elif text == "ln":
            try:
                num = float(self.display.get())
                result = math.log(num)
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
            except ValueError:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error: Invalid input!")
       
        else:
            if len(self.display.get()) < 12:
                self.display.insert(tk.END, text)
            else:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error: Exceeds 12 digits!")

    def update_entries_text(self):
        self.entries_text.delete("1.0", tk.END)
        for i, entry in enumerate(self.entries[-5:]):
            self.entries_text.insert(tk.END, f"{i+1}. {entry}\n")


if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
