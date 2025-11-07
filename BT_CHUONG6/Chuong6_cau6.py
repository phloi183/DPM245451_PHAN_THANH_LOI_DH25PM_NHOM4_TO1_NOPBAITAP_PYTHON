#chuong6 cau6
import random
def tao_list_khong_trung(n, low=0, high=100):
    if high - low + 1 < n:
        raise ValueError("Khoảng giá trị không đủ để tạo N số khác nhau.")
    return random.sample(range(low, high + 1), n)
n = int(input("Nhập N: "))
low = int(input("Khoảng từ (low): "))
high = int(input("đến (high): "))
lst = tao_list_khong_trung(n, low, high)
print("Danh sách ngẫu nhiên không trùng:", lst)