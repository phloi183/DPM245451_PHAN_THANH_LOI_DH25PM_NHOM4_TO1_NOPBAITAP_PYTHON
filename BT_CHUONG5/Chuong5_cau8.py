#chuong5 cau 8
import os
def LayTenFile(duongdan):
    return os.path.basename(duongdan)
def LayTenKhongPhanMoRong(duongdan):
    ten_file = os.path.basename(duongdan)
    ten_khong_duoi = os.path.splitext(ten_file)[0]
    return ten_khong_duoi
duongdan = input("Nhập đường dẫn file nhạc: ")
print("Tên file có phần mở rộng mp3:", LayTenFile(duongdan))
print("Tên file không có phần mở rộng mp3:", LayTenKhongPhanMoRong(duongdan))
