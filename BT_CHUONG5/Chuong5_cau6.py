#chuong5 câu 6
import re

def NegativeNumberInStrings(s):
    numbers = re.findall(r'-\d+', s)

    if numbers:
        print("Các số nguyên âm trong chuỗi là:", ', '.join(numbers))
    else:
        print("Không có số nguyên âm nào trong chuỗi.")

chuoi = input("Nhập vào một chuỗi bất kỳ: ")
NegativeNumberInStrings(chuoi)
