# Pattern:
# * * * * *
#  *     *
#   *   *
#    * *
#     *

n = 5
for i in range(n, 0, -1):
    for _ in range(n - i):
        print(" ", end="")

    if i == n:
        for k in range(2 * n - 1):
            if k % 2 == 0:
                print("*", end="")
            else:
                print(" ", end="")
        print()
    elif i > 1:
        print("*", end="")
        for _ in range(2 * i - 3):
            print(" ", end="")
        print("*")
    else:
        print("*")
