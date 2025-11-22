# 3) Given a list of integers, write a code to find the first missing positive integer from the list. The list can contain both positive and negative integers.

def first_missing_positive(nums):
    seen = set(x for x in nums if x > 0)
    candidate = 1
    while candidate in seen:
        candidate += 1
    return candidate

# Example
nums = [3, 4, -1, 1]
print("First missing positive:", first_missing_positive(nums))   # 2
