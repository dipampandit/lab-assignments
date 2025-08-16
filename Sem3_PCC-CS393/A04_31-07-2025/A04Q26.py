# Check whether a number is an Automorphic number or not
# (Automorphic number = its square ends with the number)

num = int(input("Enter a number: "))
sq = num * num
if str(sq).endswith(str(num)):
    print("Automorphic number")
else:
    print("Not an Automorphic number")
