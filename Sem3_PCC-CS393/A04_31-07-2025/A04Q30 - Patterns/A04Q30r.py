# Pattern:
#         E
#       D E
#     C D E
#   B C D E
# A B C D E

n = 5
for i in range(n):
    for s in range(n - i - 1):
        print(" ", end=" ")
    for j in range(i + 1):
        print(chr(65 + n - (i + 1) + j), end=" ")
    print()
