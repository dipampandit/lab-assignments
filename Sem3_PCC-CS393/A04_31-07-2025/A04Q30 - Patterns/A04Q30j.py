# Pattern:
#     *
#    * *
#   *   *
#  *     *
# * * * * *

n = 5
for i in range(1, n + 1):
    for _ in range(n - i):
        print(" ", end="")

    if i == 1:
        print("*")
    elif i < n:
        print("*", end="")
        for _ in range(2 * i - 3):
            print(" ", end="")
        print("*") 
    else:
        for k in range(2 * n - 1):
            if k % 2 == 0:
                print("*", end="")
            else:
                print(" ", end="")
        print()
