# 1. Nested list flattening without/with recursion
#    Input: [1, 2, 3, [4, 5, 6], 7]
#    Output: [1, 2, 3, 4, 5, 6, 7]

# with recursion
def flatten_recursive(nested_list):
    result = []
    for item in nested_list:
        if isinstance(item, list):
            result.extend(flatten_recursive(item))
        else:
            result.append(item)
    return result

# without recursion (using stack)
def flatten_iterative(nested_list):
    result = []
    stack = nested_list[::-1]  # start with reversed for correct order
    while stack:
        item = stack.pop()
        if isinstance(item, list):
            stack.extend(item[::-1])  # extend reversed sublist
        else:
            result.append(item)
    return result

nested_list = [1, 2, 3, [4, 5, 6], 7]
print("Flattened (recursive):", flatten_recursive(nested_list))
print("Flattened (iterative):", flatten_iterative(nested_list))