# Implement Merge Sort and analyze its time complexity

def merge(lst, low, mid, high):
    temp = []
    i, j = low, mid + 1

    while (i <= mid and j <= high):
        if (lst[i] <= lst[j]):
            temp.append(lst[i])
            i += 1
        else:
            temp.append(lst[j])
            j += 1
    
    while (i <= mid):
        temp.append(lst[i])
        i += 1
    
    while (j <= high):
        temp.append(lst[j])
        j += 1

    for idx in range(len(temp)):
        lst[low + idx] = temp[idx]

def mergeSort(lst, low, high):
    if (low < high):
        mid = (low + high) // 2
        mergeSort(lst, low, mid)
        mergeSort(lst, mid + 1, high)
        merge(lst, low, mid, high)

lst = [1, 9, 7, 5, 3]
mergeSort(lst, 0, len(lst) - 1)
print(lst)

'''
Time Complexity for all three cases is O(n log n).
- it divides the list into halves = log n levels
- each level does linear merging = n work

Space Complexity: O(n) due to temporary list.
'''