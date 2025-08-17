# Pattern:
#         1 
#       A B C 
#     2 3 4 5 6 
#   D E F G H I J 
# 7 8 9 1 2 3 4 5 6

num = 5

val = 1
ch = ord('A')

for i in range(1, num + 1):
    print(" " * (num - i) * 2, end = "")
    if i % 2 != 0:
        for j in range(2 * i - 1):
            print(val, end = " ")
            val += 1
            if val > 9:
                val = 1
    else:
        for j in range(2 * i - 1):
            print(chr(ch), end = " ")
            ch += 1
    print()
