from tkinter import *

def tiepAction():
    stringHSA.set("")
    stringHSB.set("")
    stringKQ.set("")

def giaiAction():
    try:
        a = float(stringHSA.get())
        b = float(stringHSB.get())
        if a == 0 and b == 0:
            stringKQ.set("Vô số nghiệm")
        elif a == 0 and b != 0:
            stringKQ.set("Vô nghiệm")
        else:
            stringKQ.set("x = " + str(-b / a))
    except ValueError:
        stringKQ.set("Nhập sai định dạng!")

root = Tk()
root.title("Phương trình bậc 1 - facebook.com/duythanhcse")
root.minsize(height=150, width=300)
root.resizable(height=True, width=True)

stringHSA = StringVar()
stringHSB = StringVar()
stringKQ = StringVar()

Label(root, text="Phương Trình Bậc 1", fg="red", font=("Tahoma", 16), justify=CENTER).grid(row=0, columnspan=2, pady=5)

Label(root, text="Hệ số a:").grid(row=1, column=0, sticky=E)
Entry(root, width=30, textvariable=stringHSA).grid(row=1, column=1)

Label(root, text="Hệ số b:").grid(row=2, column=0, sticky=E)
Entry(root, width=30, textvariable=stringHSB).grid(row=2, column=1)

frameButton = Frame(root)
Button(frameButton, text="Giải", command=giaiAction, width=8).pack(side=LEFT, padx=5)
Button(frameButton, text="Tiếp", command=tiepAction, width=8).pack(side=LEFT, padx=5)
Button(frameButton, text="Thoát", command=root.quit, width=8).pack(side=LEFT, padx=5)
frameButton.grid(row=3, columnspan=2, pady=5)

Label(root, text="Kết quả:").grid(row=4, column=0, sticky=E)
Entry(root, width=30, textvariable=stringKQ).grid(row=4, column=1)

root.mainloop()
