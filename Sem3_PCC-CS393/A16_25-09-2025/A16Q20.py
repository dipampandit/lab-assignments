# Convert a decimal number to binary
def decimal_to_binary(n):
    if n == 0:
        return ""
    return decimal_to_binary(n // 2) + str(n % 2)

print(decimal_to_binary(10))  # Output: "1010"
