#giải bài tập chương 4 câu 11
def sum1(n):
    s=0
    while n>0:
        s+=1
        n-=1
    return s
def sum2():
    
    global val
    s = 0
    while val > 0:
        s +=1
        val -= 1
    return s

def sum3():
    s=0
    for i in range(val, 0, -1):
     s+=1
    return s    