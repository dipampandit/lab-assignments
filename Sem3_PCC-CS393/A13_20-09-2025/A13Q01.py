"""
Problem: Maximum Sum SubList of Size K
A list of integers and a number K, find the maximum sum of a sublist of size K.

Input:  list = [2, 1, 5, 1, 3, 2], K = 3
Output: 9
Explanation: Subarray [5, 1, 3] has the maximum sum 9.
"""

def max_sum_sublist(arr, k):
    n = len(arr)
    if n < k:
        return None
    max_sum = current_sum = sum(arr[:k])
    max_start_index = 0

    for i in range(k, n):
        current_sum += arr[i] - arr[i - k]
        if current_sum > max_sum:
            max_sum = current_sum
            max_start_index = i - k + 1

    return arr[max_start_index:max_start_index + k], max_sum

arr = list(map(int, input("Enter the list elements separated by space: ").split()))
k = int(input("Enter the value of K: "))

result, max_sum = max_sum_sublist(arr, k)
if result:
    print(f"Sublist with max sum of size {k}: {result}")
    print(f"Maximum Sum: {max_sum}")
else:
    print("Sublist of given size not possible.")
