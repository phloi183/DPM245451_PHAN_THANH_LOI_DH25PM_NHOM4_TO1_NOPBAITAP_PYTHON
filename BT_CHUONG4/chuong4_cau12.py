#giải bài tập chương 4 câu 12 
#hàm oscillate
def oscillate(a, b):
    for i in range(a, 2):
        yield i
        yield i
    for i in range(1, a - 5, -1):
        yield i
        yield i
for n in oscillate(-3, 5):
    print(n, end=' ')
