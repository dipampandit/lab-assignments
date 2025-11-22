# 4) Given an array nums and an integer target, return any combination of indices such that the 
# sum of the corresponding elements equals target. Each index can be used at most once. 
# If no such combination exists, return an empty list.
#   Examples from the table:
#   nums = [-10, 15, 3, 7], target = 5  -> [0, 1]
#   nums = [1, 2, 3, 4, 5], target = 6  -> [1, 3] or [0, 4] or [0, 1, 2]
#   nums = [5, 5, 5, 5], target = 10    -> [0, 1] (or any valid pair)

def find_indices_for_target(nums, target):
    n = len(nums)

    # Backtracking to find any subset of indices whose sum == target
    def backtrack(start, current_sum, chosen):
        if current_sum == target:
            return chosen[:]          # found one combination
        if current_sum > target and all(x >= 0 for x in nums[start:]):
            return None               # pruning when remaining are non-negative
        if start == n:
            return None

        # choice 1: include current index
        chosen.append(start)
        res = backtrack(start + 1, current_sum + nums[start], chosen)
        if res is not None:
            return res
        chosen.pop()

        # choice 2: exclude current index
        return backtrack(start + 1, current_sum, chosen)

    result = backtrack(0, 0, [])
    return result if result is not None else []


# Quick tests using the table:
print(find_indices_for_target([-10, 15, 3, 7], 5))          # e.g. [0, 1]
print(find_indices_for_target([1, 2, 3, 4, 5], 6))          # e.g. [1, 3] or [0, 4] or [0, 1, 2]