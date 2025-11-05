#CHUONG 5 CÂU 1
def checkdoixung (s):
    flag = True
    for i in range ( len(s)):
        if s [i] != s [len(s) - i - 1]:
            flag = False
            break
    return flag
def main():
    print("nhap 1 chuoi: ")
    s = input()
    if checkdoixung(s):
        print("chuỗi bạn nhập đối xứng")
    else:
        print("chuỗi bạn nhập không đối xứng")
while True:
    main()
    print(" bạn có muốn tiếp tục ? (c/k) : ")
    s= input()
    if s == 'k':
        break
print("cảm ơn bạn")