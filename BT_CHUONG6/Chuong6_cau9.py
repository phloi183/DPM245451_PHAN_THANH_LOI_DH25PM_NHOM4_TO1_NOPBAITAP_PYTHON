def la_nguyen_to(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
M = list(map(int, input("Nhập các số tự nhiên (cách nhau bởi dấu cách): ").split()))
le = [x for x in M if x % 2 != 0]
tong_le = sum(le)
print("Các số lẻ:", le, "→ Tổng:", tong_le, "→ Có", len(le), "số lẻ")
chan = [x for x in M if x % 2 == 0]
tong_chan = sum(chan)
print("Các số chẵn:", chan, "→ Tổng:", tong_chan, "→ Có", len(chan), "số chẵn")
nguyento = [x for x in M if la_nguyen_to(x)]
print("Các số nguyên tố:", nguyento)
khong_nt = [x for x in M if not la_nguyen_to(x)]
print("Các số không phải là nguyên tố:", khong_nt)
