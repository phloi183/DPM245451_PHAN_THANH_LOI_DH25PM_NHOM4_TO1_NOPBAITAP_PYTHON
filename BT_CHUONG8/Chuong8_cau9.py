from tkinter import *
from tkinter import messagebox

def tinh_bmi():
    try:
        cao = float(entry_cao.get())
        nang = float(entry_nang.get())
        if cao <= 0 or nang <= 0:
            messagebox.showerror("Lỗi", "Chiều cao và cân nặng phải > 0!")
            return

        bmi = nang / (cao * cao)
        bmi_var.set(f"{bmi:.1f}")

        if bmi < 18.5:
            tinhtrang_var.set("Gầy")
            nguyco_var.set("Thấp")
        elif bmi < 25:
            tinhtrang_var.set("Bình thường")
            nguyco_var.set("Trung bình")
        elif bmi < 30:
            tinhtrang_var.set("Hơi Béo")
            nguyco_var.set("Hơi cao")
        else:
            tinhtrang_var.set("Béo phì")
            nguyco_var.set("Rất cao")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

root = Tk()
root.title("Phần mềm tính BMI")
root.resizable(False, False)

frame = Frame(root, bg="yellow", bd=2, relief="groove", padx=10, pady=10)
frame.grid(row=0, column=0, padx=10, pady=10)

Label(frame, text="Nhập chiều cao (m):", bg="yellow", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="e", pady=5)
entry_cao = Entry(frame, width=15, justify=RIGHT)
entry_cao.grid(row=0, column=1, padx=5)
entry_cao.insert(0, "1.8")

Label(frame, text="Nhập cân nặng (kg):", bg="yellow", font=("Segoe UI", 10)).grid(row=1, column=0, sticky="e", pady=5)
entry_nang = Entry(frame, width=15, justify=RIGHT)
entry_nang.grid(row=1, column=1, padx=5)
entry_nang.insert(0, "72")

Button(frame, text="Tính BMI", bg="blue", fg="white", width=10, command=tinh_bmi).grid(row=2, column=1, pady=8)

Label(frame, text="BMI của bạn:", bg="yellow", font=("Segoe UI", 10)).grid(row=3, column=0, sticky="e", pady=5)
bmi_var = StringVar(value="x")
Entry(frame, width=15, textvariable=bmi_var, justify=CENTER).grid(row=3, column=1, pady=5)

Label(frame, text="Tình trạng của bạn:", bg="yellow", font=("Segoe UI", 10)).grid(row=4, column=0, sticky="e", pady=5)
tinhtrang_var = StringVar(value="")
Entry(frame, width=15, textvariable=tinhtrang_var, justify=CENTER, fg="red").grid(row=4, column=1, pady=5)

Label(frame, text="Nguy cơ phát triển bệnh:", bg="yellow", font=("Segoe UI", 10)).grid(row=5, column=0, sticky="e", pady=5)
nguyco_var = StringVar(value="")
Entry(frame, width=15, textvariable=nguyco_var, justify=CENTER, fg="red").grid(row=5, column=1, pady=5)

Button(frame, text="Thoát", bg="orange", width=10, command=root.quit).grid(row=6, column=1, pady=8)

root.mainloop()
