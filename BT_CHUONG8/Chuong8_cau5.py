from tkinter import *
from tkinter import messagebox

def check_password():
    old_pw = old_pass.get()
    new_pw = new_pass.get()
    re_pw  = re_pass.get()

    if old_pw != "12345":
        messagebox.showerror("Error", "Old password không đúng!")
        return

    if new_pw == "":
        messagebox.showwarning("Warning", "New password không được để trống!")
        return

    if new_pw != re_pw:
        messagebox.showerror("Error", "Mật khẩu nhập lại không khớp!")
        return

    messagebox.showinfo("Success", "Đổi mật khẩu thành công!")
    root.destroy()

def cancel_action():
    root.destroy()

root = Tk()
root.title("Enter New Password")
root.resizable(False, False)
root.minsize(height=130, width=350)

Label(root, text="Old Password:").grid(row=0, column=0, padx=10, pady=5, sticky="e")
old_pass = Entry(root, show="*", width=25)
old_pass.grid(row=0, column=1, padx=10, pady=5)

Label(root, text="New Password:").grid(row=1, column=0, padx=10, pady=5, sticky="e")
new_pass = Entry(root, show="*", width=25)
new_pass.grid(row=1, column=1, padx=10, pady=5)

Label(root, text="Enter New Password Again:").grid(row=2, column=0, padx=10, pady=5, sticky="e")
re_pass = Entry(root, show="*", width=25)
re_pass.grid(row=2, column=1, padx=10, pady=5)

frame_btn = Frame(root)
Button(frame_btn, text="OK", width=10, command=check_password).pack(side=LEFT, padx=5)
Button(frame_btn, text="Cancel", width=10, command=cancel_action).pack(side=LEFT, padx=5)
frame_btn.grid(row=3, column=1, pady=10)

root.mainloop()
