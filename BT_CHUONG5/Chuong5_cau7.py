#chuong5 câu 7
def ToiUuChuoiDanhTu(chuoi):
    tu = chuoi.strip().split()
    tu_viet_hoa = [t.capitalize() for t in tu]
    chuoi_toi_uu = ' '.join(tu_viet_hoa)
    return chuoi_toi_uu
chuoi = input("Nhập vào chuỗi danh từ: ")
print("Chuỗi tối ưu là:", ToiUuChuoiDanhTu(chuoi))
