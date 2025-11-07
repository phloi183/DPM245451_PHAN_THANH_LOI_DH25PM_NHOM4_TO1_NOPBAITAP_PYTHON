# Câu 8
def sap_xep_giam_dan(n):
    lst = []
    for i in range(n):
        while True:
            try:
                x = float(input(f"Nhập M[{i}]: "))
                lst.append(x)
                break
            except ValueError:
                print(" Nhập sai kiểu dữ liệu, mời nhập lại.")
    lst.sort(reverse=True)
    return lst
n = int(input("Nhập số phần tử: "))
day = sap_xep_giam_dan(n)
print("Dãy sau khi sắp xếp giảm dần:", day)
