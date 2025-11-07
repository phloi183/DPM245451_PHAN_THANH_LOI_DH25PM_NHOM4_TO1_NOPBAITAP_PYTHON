from tkinter import *
from tkinter import messagebox

def chuyen_do():
    try:
        doF = float(entryF.get())
        doC = (doF - 32) * 5 / 9
        result_var.set(f"{doC:.2f} °C")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")


root = Tk()
root.title("Chuyển độ F sang độ C")
root.resizable(False, False)

frame = Frame(root, bg="yellow", bd=2, relief="groove", padx=10, pady=10)
frame.grid(row=0, column=0, padx=10, pady=10)

Label(frame, text="Nhập độ F:", bg="yellow", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="e", pady=5)
entryF = Entry(frame, width=15, justify=RIGHT)
entryF.grid(row=0, column=1, padx=5)
entryF.insert(0, "350")

Button(frame, text="Chuyển", bg="blue", fg="white", width=10, command=chuyen_do).grid(row=0, column=2, padx=5)

Label(frame, text="Độ C:", bg="yellow", font=("Segoe UI", 10)).grid(row=1, column=0, sticky="e", pady=10)
result_var = StringVar(value="Độ C ở đây")
Label(frame, textvariable=result_var, bg="yellow", font=("Segoe UI", 11, "bold")).grid(row=1, column=1, columnspan=2, sticky="w")

root.mainloop()
