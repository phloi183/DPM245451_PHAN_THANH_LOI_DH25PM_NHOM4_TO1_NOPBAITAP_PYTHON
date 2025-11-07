# chuong 5 cau 5
chuoi = input("Nhập vào một chuỗi bất kỳ: ")
dem_hoa = dem_thuong = dem_so = dem_ktdb = dem_khoangtrang = 0
dem_nguyenam = dem_phuam = 0
nguyen_am = "aeiouAEIOU"

for ch in chuoi:
    if ch.isupper():
        dem_hoa += 1
    elif ch.islower():
        dem_thuong += 1
    elif ch.isdigit():
        dem_so += 1
    elif ch.isspace():
        dem_khoangtrang += 1
    else:
        dem_ktdb += 1
        
    if ch.isalpha():
        if ch in nguyen_am:
            dem_nguyenam += 1
        else:
            dem_phuam += 1

print("Số chữ IN HOA:", dem_hoa)
print("Số chữ in thường:", dem_thuong)
print("Số chữ là chữ số:", dem_so)
print("Số ký tự đặc biệt:", dem_ktdb)
print("Số khoảng trắng:", dem_khoangtrang)
print("Số chữ là nguyên âm:", dem_nguyenam)
print("Số chữ là phụ âm:", dem_phuam)
