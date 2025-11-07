def nhap_matrix(ten):
    r = int(input(f"Nhập số hàng của ma trận {ten}: "))
    c = int(input(f"Nhập số cột của ma trận {ten}: "))
    print(f"Nhập các phần tử cho ma trận {ten}:")
    matrix = []
    for i in range(r):
        hang = list(map(float, input(f"  Hàng {i+1}: ").split()))
        matrix.append(hang)
    return matrix
def in_matrix(M, name="Matrix"):
    print(f"{name}:")
    for row in M:
        print("  ", row)

def cong_matrix(A, B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        raise ValueError("Hai ma trận phải cùng kích thước!")
    C = []
    for i in range(len(A)):
        hang = [A[i][j] + B[i][j] for j in range(len(A[0]))]
        C.append(hang)
    return C

def hoanvi_matrix(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

A = nhap_matrix("A")
B = nhap_matrix("B")

print("\n--- Ma trận A ---")
in_matrix(A, "A")
print("\n--- Ma trận B ---")
in_matrix(B, "B")

C = cong_matrix(A, B)
print("\n--- Kết quả A + B ---")
in_matrix(C, "A + B")

AT = hoanvi_matrix(A)
BT = hoanvi_matrix(B)
print("\n--- Hoán vị của A ---")
in_matrix(AT, "A^T")
print("\n--- Hoán vị của B ---")
in_matrix(BT, "B^T")
