# Display all Prime numbers within a given range.

low = int(input("Enter lower bound: "))
high = int(input("Enter upper bound: "))
for num in range(low, high + 1):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            print(num, end=' ')
