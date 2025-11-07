from tkinter import *
from tkinter import messagebox

CAN = ["Giáp","Ất","Bính","Đinh","Mậu","Kỷ","Canh","Tân","Nhâm","Quý"]
CHI = ["Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi","Thân","Dậu","Tuất","Hợi"]

def chuyen_can_chi(nam_duong: int) -> str:

    offset = nam_duong - 1984
    can = CAN[offset % 10]
    chi = CHI[offset % 12]
    return f"{can} {chi}"

def handle_convert():
    s = year_var.get().strip()
    if not s.isdigit():
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên năm dương hợp lệ!")
        return
    y = int(s)
    if y <= 0:
        messagebox.showerror("Lỗi", "Năm phải > 0!")
        return
    result_var.set(chuyen_can_chi(y))

root = Tk()
root.title("Chuyển Dương lịch → Âm lịch (Can Chi)")
root.resizable(False, False)

frame = Frame(root, bg="#FFEE33", bd=2, relief="groove", padx=10, pady=10)
frame.grid(row=0, column=0, padx=12, pady=12)

Label(frame, text="Nhập năm dương:", bg="#FFEE33", font=("Segoe UI", 10)).grid(row=0, column=0, sticky="e", pady=4)

year_var = StringVar(value="1982")
Entry(frame, width=18, textvariable=year_var, justify=RIGHT).grid(row=0, column=1, padx=6, pady=4)

Button(frame, text="Chuyển", width=10, command=handle_convert).grid(row=0, column=2, padx=4)

Label(frame, text="Năm âm:", bg="#FFEE33", font=("Segoe UI", 10)).grid(row=1, column=0, sticky="e", pady=8)

result_var = StringVar(value="")
Label(frame, textvariable=result_var, bg="#FFEE33", fg="black",
      font=("Segoe UI", 11, "bold")).grid(row=1, column=1, columnspan=2, sticky="w")

root.mainloop()
