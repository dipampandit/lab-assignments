# Maximum & Minimum of N numbers using *args
def max_min(*args):
    return max(args), min(args)

print(max_min(3, 8, 1, 10, 4))
