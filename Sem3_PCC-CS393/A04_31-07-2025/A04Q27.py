# Print all perfect squares between 1 and N

n = int(input("Enter N: "))
print("Perfect squares between 1 and", n, ":")
i = 1
while i * i <= n:
    print(i * i, end=" ")
    i += 1
