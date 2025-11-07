from tkinter import *
from math import sqrt

def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringHSC.set("")
    stringKQ.set("")

def giaiAction():
    try:
        a = float(stringHSA.get())
        b = float(stringHSB.get())
        c = float(stringHSC.get())

        if a == 0:
            if b == 0 and c == 0:
                stringKQ.set("Vô số nghiệm")
            elif b == 0 and c != 0:
                stringKQ.set("Vô nghiệm")
            else:
                x = -c / b
                stringKQ.set(f"Nghiệm: x = {x}")
            return

        delta = b*b - 4*a*c
        if delta < 0:
            stringKQ.set("Vô nghiệm")
        elif delta == 0:
            x = -b / (2*a)
            stringKQ.set(f"Δ=0 → Nghiệm kép: x1=x2={x}")
        else:
            x1 = (-b - sqrt(delta)) / (2*a)
            x2 = (-b + sqrt(delta)) / (2*a)
            stringKQ.set(f"Δ={delta} → x1={x1}, x2={x2}")
    except ValueError:
        stringKQ.set("Vui lòng nhập số hợp lệ!")

root = Tk()
root.title("PTB2 - Phương Trình Bậc 2")
root.minsize(height=180, width=320)
root.resizable(True, True)

stringHSA = StringVar()
stringHSB = StringVar()
stringHSC = StringVar()
stringKQ  = StringVar()

Label(root, text="Phương Trình Bậc 2", fg="red",
      font=("Tahoma", 16), justify=CENTER).grid(row=0, column=0, columnspan=2, pady=6)

Label(root, text="Hệ số a:").grid(row=1, column=0, sticky="e", padx=6, pady=2)
Entry(root, width=30, textvariable=stringHSA).grid(row=1, column=1, padx=6, pady=2)

Label(root, text="Hệ số b:").grid(row=2, column=0, sticky="e", padx=6, pady=2)
Entry(root, width=30, textvariable=stringHSB).grid(row=2, column=1, padx=6, pady=2)

Label(root, text="Hệ số c:").grid(row=3, column=0, sticky="e", padx=6, pady=2)
Entry(root, width=30, textvariable=stringHSC).grid(row=3, column=1, padx=6, pady=2)

frameButton = Frame(root)
Button(frameButton, text="Giải",  command=giaiAction).pack(side=LEFT, padx=5)
Button(frameButton, text="Tiếp",  command=tiepAction).pack(side=LEFT, padx=5)
Button(frameButton, text="Thoát", command=root.quit).pack(side=LEFT, padx=5)
frameButton.grid(row=4, column=0, columnspan=2, pady=6)

Label(root, text="Kết quả:").grid(row=5, column=0, sticky="e", padx=6, pady=2)
Entry(root, width=30, textvariable=stringKQ).grid(row=5, column=1, padx=6, pady=2)

root.mainloop()
