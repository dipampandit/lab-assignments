# Pattern:
# 1               1
#   2           2
#     3       3
#       4   4
#         5 
#       4   4
#     3       3
#   2           2
# 1               1

num = 5
for i in range(1, num + 1):
    print(" " * (i - 1) * 2 + str(i) + " " * ((num - i) * 4 - 1) + (str(i) if i != num else " "))

for i in range(num - 1, 0, -1):
    print(" " * (i - 1) * 2 + str(i) + " " * ((num - i) * 4 - 1) + str(i))
