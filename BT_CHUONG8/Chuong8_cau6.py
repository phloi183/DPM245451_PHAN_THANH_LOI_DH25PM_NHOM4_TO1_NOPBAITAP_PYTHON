from tkinter import *

root = Tk()
root.title("frame 2")
root.resizable(False, False)

styles = ["raised", "sunken", "flat", "ridge", "groove", "solid"]

for bw in range(5):
    Label(root, text=f"borderwidth = {bw}").grid(row=bw, column=0, padx=10, pady=5)
    for i, s in enumerate(styles):
        Button(root, text=s, relief=s, borderwidth=bw, width=8).grid(row=bw, column=i+1, padx=5, pady=5)

root.mainloop()
