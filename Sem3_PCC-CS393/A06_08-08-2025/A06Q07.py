# Area of rectangle & return perimeter using *args (pairs of length, breadth)
def rectangle(*args):
    results = []
    for i in range(0, len(args), 2):
        length, breadth = args[i], args[i+1]
        area = length * breadth
        perimeter = 2 * (length + breadth)
        results.append((area, perimeter))
    return results

print(rectangle(5, 3, 10, 2))
