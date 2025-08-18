# Fibonacci series using *args
def fibonacci(*args):
    series_list = []
    for n in args:
        a, b = 0, 1
        series = []
        for _ in range(n):
            series.append(a)
            a, b = b, a+b
        series_list.append(series)
    return series_list

print(fibonacci(5, 7))
