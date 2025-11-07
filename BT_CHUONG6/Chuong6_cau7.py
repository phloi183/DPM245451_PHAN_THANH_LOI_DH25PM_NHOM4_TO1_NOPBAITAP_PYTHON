# Câu 7
def nhap_day_tang(n):
    a = []
    for i in range(n):
        while True:
            try:
                x = float(input(f"Nhập a[{i}]: "))
                if i == 0 or x > a[-1]:
                    a.append(x)
                    break
                else:
                    print(" Sai! Phải lớn hơn phần tử trước đó.")
            except ValueError:
                print(" Nhập sai kiểu dữ liệu, mời nhập lại.")
    return a

n = int(input("Nhập số phần tử: "))
lst = nhap_day_tang(n)
print("Dãy sau khi nhập:", lst)
