# Implement Quick Sort with in-place partitioning

def partition(lst, low, high):
    pivot = lst[low]
    i, j = low, high

    while (i < j):
        while i <= high - 1 and lst[i] <= pivot:
            i += 1
        while j >= low + 1 and lst[j] > pivot:
            j -= 1

        if (i < j):
            lst[i], lst[j] = lst[j], lst[i]

    lst[low], lst[j] = lst[j], lst[low]
    return j

def quickSort(lst, low, high):
    if (low < high):
        partitionIndex = partition(lst, low, high)
        quickSort(lst, low, partitionIndex - 1)
        quickSort(lst, partitionIndex + 1, high)

lst = [1, 9, 7, 5, 3]
quickSort(lst, 0, len(lst) - 1)
print(lst)
