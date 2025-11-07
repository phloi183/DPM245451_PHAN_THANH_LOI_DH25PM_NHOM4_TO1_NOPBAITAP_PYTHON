from tkinter import *

ALLOWED = set("0123456789+-*/().")

def add_char(ch: str):
    cur = expr_var.get()
    expr_var.set(cur + ch)

def clear_all():
    expr_var.set("")

def backspace():
    cur = expr_var.get()
    expr_var.set(cur[:-1])

def calculate():
    exp = expr_var.get().replace("×", "*").replace("÷", "/")
    if not set(exp) <= ALLOWED:
        expr_var.set("Lỗi cú pháp")
        return
    try:
        result = eval(exp, {"__builtins__": None}, {})
        expr_var.set(str(result))
    except Exception:
        expr_var.set("Lỗi")

root = Tk()
root.title("Calculator")
root.resizable(False, False)

expr_var = StringVar()

e = Entry(root, textvariable=expr_var, justify=RIGHT, font=("Segoe UI", 16), width=15)
e.grid(row=0, column=0, columnspan=4, padx=6, pady=6)
e.focus_set()

Button(root, text="1", width=4, height=2, command=lambda: add_char("1")).grid(row=1, column=0)
Button(root, text="2", width=4, height=2, command=lambda: add_char("2")).grid(row=1, column=1)
Button(root, text="3", width=4, height=2, command=lambda: add_char("3")).grid(row=1, column=2)
Button(root, text="÷", width=4, height=2, command=lambda: add_char("/")).grid(row=1, column=3)

Button(root, text="4", width=4, height=2, command=lambda: add_char("4")).grid(row=2, column=0)
Button(root, text="5", width=4, height=2, command=lambda: add_char("5")).grid(row=2, column=1)
Button(root, text="6", width=4, height=2, command=lambda: add_char("6")).grid(row=2, column=2)
Button(root, text="×", width=4, height=2, command=lambda: add_char("*")).grid(row=2, column=3)

Button(root, text="7", width=4, height=2, command=lambda: add_char("7")).grid(row=3, column=0)
Button(root, text="8", width=4, height=2, command=lambda: add_char("8")).grid(row=3, column=1)
Button(root, text="9", width=4, height=2, command=lambda: add_char("9")).grid(row=3, column=2)
Button(root, text="-", width=4, height=2, command=lambda: add_char("-")).grid(row=3, column=3)

Button(root, text="+", width=4, height=2, command=lambda: add_char("+")).grid(row=4, column=0)
Button(root, text="0", width=4, height=2, command=lambda: add_char("0")).grid(row=4, column=1)
Button(root, text=".", width=4, height=2, command=lambda: add_char(".")).grid(row=4, column=2)
Button(root, text="=", width=4, height=2, command=calculate).grid(row=4, column=3)

Button(root, text="⌫", width=4, height=2, command=backspace).grid(row=5, column=0)
Button(root, text="Clr", width=12, height=2, command=clear_all).grid(row=5, column=1, columnspan=2)
Button(root, text="Thoát", width=4, height=2, command=root.quit).grid(row=5, column=3)

root.mainloop()
