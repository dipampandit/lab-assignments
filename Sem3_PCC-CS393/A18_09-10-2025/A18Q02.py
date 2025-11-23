# 2. Re-arrange list in Zig-Zag fashion
#    Input: [4, 3, 7, 8, 6, 2, 1]
#    Output: [3, 7, 4, 8, 2, 6, 1]
#    Condition: a < b > c < d > e < f ...

def zig_zag(arr):
    arr = arr[:]   # creating a copy to avoid modifying the original list
    flag = True    # True means "<" expected, False means ">"
    for i in range(len(arr) - 1):
        if flag:
            # expect arr[i] < arr[i+1]
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        else:
            # expect arr[i] > arr[i+1]
            if arr[i] < arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        flag = not flag
    return arr

lst = [4, 3, 7, 8, 6, 2, 1]
print("Zig-Zag :", zig_zag(lst))