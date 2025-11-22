# Given a list of integers, write a code to rotate the array to the right by a given number of positions.

def rotate_right(nums, k):
    n = len(nums)
    if n == 0:
        return nums

    k = k % n
    return nums[-k:] + nums[:-k]

# Example
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print("Rotated:", rotate_right(nums, k))            # [5, 6, 7, 1, 2, 3, 4]
