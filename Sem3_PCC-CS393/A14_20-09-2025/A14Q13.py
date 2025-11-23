# Find the frequency of each element in an array and display the elements along with their frequencies.

arr = []
n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr += [val]

visited = []
for i in range(n):
    already = False
    for v in visited:
        if arr[i] == v:
            already = True
            break
    if not already:
        count = 0
        for j in range(n):
            if arr[i] == arr[j]:
                count += 1
        print(arr[i], "->", count)
        visited += [arr[i]]
