# Implement Binary Search iteratively

def binarySearch(lst, low, high, key):
    while (low <= high):
        mid = (low + high) // 2
        if (lst[mid] == key):
            return mid
        elif (lst[mid] < key):
            low = mid + 1
        else:
            high = mid - 1
    return -1

lst = [1, 2, 3, 4, 5]
key = 4

result = binarySearch(lst, 0, len(lst) - 1, key)
if (result != -1):
    print("Element found at index ", result)
else:
    print("Element not found")
