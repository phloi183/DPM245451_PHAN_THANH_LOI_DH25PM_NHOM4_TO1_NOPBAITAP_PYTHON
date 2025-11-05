# cau 13 chuong 4
def tong_uoc(n):
    s = 0
    for i in range(1, n):
        if n % i == 0:
            s += i
    return s
def kiem_tra_so(n):
    tong = tong_uoc(n)
    if tong == n:
        print(f"{n} là số hoàn thiện (Perfect number).")
    elif tong > n:
        print(f"{n} là số thịnh vượng (Abundant number).")
    else:
        print(f"{n} không phải số hoàn thiện cũng không phải số thịnh vượng.")
n = int(input("Nhập số nguyên dương n: "))
kiem_tra_so(n)
