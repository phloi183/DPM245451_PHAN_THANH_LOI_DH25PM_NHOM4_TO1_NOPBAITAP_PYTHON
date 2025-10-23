#giải bài tập chương 4 câu 10
import time
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

hinh1 = [
"      *       ",
"      * *     ",
"      * * *   ",
"* * * * * * * ",
"* * *         ",
"* *           ",
"*             "
]
hinh2 = [
"      *       ",
"      * *     ",
"      *   *   ",
"* * * * * * * ",
"*   *         ",
"* *           ",
"*             "
]
hinh3 = [
"      * * * *  ",
"      * * *    ",
"      * *      ",
"      *        ",
"    * *        ",
"  * * *        ",
"* * * *        "
]
hinh4 = [
"      * * * *   ",
"      *   *     ",
"      * *       ",
"      *         ",
"    * *         ",
"  *   *         ",
"* * * *         "
]

cac_hinh = [hinh1, hinh2, hinh3, hinh4]

for i, hinh in enumerate(cac_hinh, start=1):
    clear()
    print(f"Hình {i}:")
    for dong in hinh:
        print(dong)
    time.sleep(5)

