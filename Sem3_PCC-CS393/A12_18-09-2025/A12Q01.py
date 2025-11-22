# Given a list of integers, write a code to find the maximum product of any two integers in the list.

def max_product(nums):
    if len(nums) < 2:
        raise ValueError("Need at least two numbers")

    max1 = max2 = 0

    for x in nums:
        # update largest
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2:
            max2 = x

    return (max1 * max2)

nums = [1, 10, 2, 6, 5, 3]
print("Max product:", max_product(nums))     # 60
