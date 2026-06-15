import numpy as np

# 1. Create a 1D NumPy array of integers from 0 to 9.
arr1 = np.arange(10)
print(arr1)


# 2. Create a 2x3 NumPy array filled with zeros (integers).
arr2 = np.zeros((2, 3), dtype=int)
print(arr2)


# 3. Create a 3x3 identity matrix using NumPy.
arr3 = np.eye(3)
print(arr3)


# 4. Use arange to make an array of even numbers from 2 to 20.
arr4 = np.arange(2, 21, 2)
print(arr4)


# 5. Use linspace to create 5 values between 0 and 1 inclusive.
arr5 = np.linspace(0, 1, 5)
print(arr5)


# 6. Create a 4x4 array filled with ones of type int64.
arr6 = np.ones((4, 4), dtype=np.int64)
print(arr6)


# 7. Make an array of shape (3,2) containing numbers 1–6 using reshape.
arr7 = np.arange(1, 7).reshape(3, 2)
print(arr7)


# 8. Convert a Python list [1,2,3,4] to a NumPy array.
list_data = [1, 2, 3, 4]
arr8 = np.array(list_data)
print(arr8)


# 9. Check the dtype, shape, size, and ndim of an array and print them.
arr9 = np.array([[1, 2, 3], [4, 5, 6]])

print(arr9.dtype)
print(arr9.shape)
print(arr9.size)
print(arr9.ndim)


# 10. Change an array’s dtype from float64 to int32.
arr10 = np.array([1.1, 2.2, 3.3], dtype=np.float64)
arr10_int = arr10.astype(np.int32)

print(arr10)
print(arr10.dtype)

print(arr10_int)
print(arr10_int.dtype)


# 11. Create a 1D boolean array from a mixed list like [True, False, 1, 0].
arr11 = np.array([True, False, 1, 0], dtype=bool)
print(arr11)


# 12. Use zeros to make a 3x3 float array and assign a value to element (1,2).
arr12 = np.zeros((3, 3), dtype=float)
arr12[1, 2] = 7.5
print(arr12)


# 13. Create an array of 10 random floats between 0 and 1 using np.random.rand.
arr13 = np.random.rand(10)
print(arr13)


# 14. Generate a 5x5 array of random integers between 0 and 9.
arr14 = np.random.randint(0, 10, size=(5, 5))
print(arr14)


# 15. Seed the random generator and show reproducibility for np.random.rand(3).
np.random.seed(42)
arr15_a = np.random.rand(3)

np.random.seed(42)
arr15_b = np.random.rand(3)

print(arr15_a)
print(arr15_b)


# 16. Use np.arange and reshape to construct a 3D array of shape (2,3,4).
arr16 = np.arange(24).reshape(2, 3, 4)
print(arr16)


# 17. Compute element-wise addition for two arrays of the same shape.
a17 = np.array([1, 2, 3])
b17 = np.array([4, 5, 6])

result17 = a17 + b17
print(result17)


# 18. Multiply two arrays element-wise and then compute the dot product.
a18 = np.array([1, 2, 3])
b18 = np.array([4, 5, 6])

elementwise18 = a18 * b18
dot18 = np.dot(a18, b18)

print(elementwise18)
print(dot18)


# 19. Demonstrate broadcasting by adding scalar 5 to a 2x4 array.
arr19 = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]])

result19 = arr19 + 5
print(result19)


# 20. Broadcast add a 1D array of length 3 to a 2x3 matrix.
matrix20 = np.array([[1, 2, 3],
                     [4, 5, 6]])

vector20 = np.array([10, 20, 30])

result20 = matrix20 + vector20

print(result20)


# 21. Use np.where to replace negative values in an array with zero.
arr21 = np.array([3, -1, 7, -5, 2])

result21 = np.where(arr21 < 0, 0, arr21)
print(result21)


# 22. Compute np.sum, np.mean, np.std, and np.var for a 1D array.
arr22 = np.array([1, 2, 3, 4, 5])

print(np.sum(arr22))
print(np.mean(arr22))
print(np.std(arr22))
print(np.var(arr22))


# 23. For a 2x4 array, compute column-wise and row-wise sums.
arr23 = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8]])

print(np.sum(arr23, axis=0))  # Column-wise sum
print(np.sum(arr23, axis=1))  # Row-wise sum


# 24. Compute cumulative sum and cumulative product for a 1D array.
arr24 = np.array([1, 2, 3, 4])

print(np.cumsum(arr24))
print(np.cumprod(arr24))


# 25. Use np.sqrt, np.log, and np.exp on a float array and interpret results.
arr25 = np.array([1.0, 4.0, 9.0])

print(np.sqrt(arr25))
print(np.log(arr25))
print(np.exp(arr25))


# 26. Compute np.sin and np.cos on an array of angles in radians.
angles26 = np.array([0, np.pi/2, np.pi])

print(np.sin(angles26))
print(np.cos(angles26))


# 27. Given arrays a and b, compute a ** b (element-wise exponentiation).
a27 = np.array([2, 3, 4])
b27 = np.array([3, 2, 1])

print(a27 ** b27)


# 28. Compute element-wise modulus for two integer arrays.
a28 = np.array([10, 20, 30])
b28 = np.array([3, 7, 4])

print(a28 % b28)


# 29. Create an array of the first 12 Fibonacci numbers using NumPy operations.
fib29 = np.zeros(12, dtype=int)

fib29[0] = 0
fib29[1] = 1

for i in range(2, 12):
    fib29[i] = fib29[i - 1] + fib29[i - 2]

print(fib29)


# 30. Use boolean indexing to select elements greater than 10 from an array.
arr30 = np.array([4, 11, 7, 15, 20, 3])

print(arr30[arr30 > 10])


# 31. Flip an array vertically and horizontally using slicing.
arr31 = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print(arr31[::-1])      # Vertical flip
print(arr31[:, ::-1])   # Horizontal flip


# 32. Extract the last column of a 2D array using slicing.
arr32 = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print(arr32[:, -1])


# 33. Extract middle rows (1:-2) of a 2D array using negative indices.
arr33 = np.array([[1, 2],
                  [3, 4],
                  [5, 6],
                  [7, 8],
                  [9, 10]])

print(arr33[1:-2])


# 34. Reverse every row of a 2D array while preserving row order.
arr34 = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print(arr34[:, ::-1])


# 35. Given a 3x3 matrix, get the main diagonal and anti-diagonal.
arr35 = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print(np.diag(arr35))
print(np.diag(np.fliplr(arr35)))


# 36. Compute the trace of a square matrix using np.trace.
arr36 = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print(np.trace(arr36))


# 37. Compute matrix transpose and confirm A.T.T == A.
arr37 = np.array([[1, 2],
                  [3, 4]])

transpose37 = arr37.T

print(transpose37)
print(np.array_equal(arr37.T.T, arr37))


# 38. Compute np.dot(A, B) for two compatible matrices and check shape.
A38 = np.array([[1, 2],
                [3, 4]])

B38 = np.array([[5, 6],
                [7, 8]])

dot38 = np.dot(A38, B38)

print(dot38)
print(dot38.shape)


# 39. Solve Ax = b for a 2x2 linear system using np.linalg.solve.
A39 = np.array([[2, 1],
                [1, 3]])

b39 = np.array([8, 13])

x39 = np.linalg.solve(A39, b39)

print(x39)


# 40. Compute determinant and inverse of a 3x3 matrix (if invertible).
arr40 = np.array([[1, 2, 3],
                  [0, 1, 4],
                  [5, 6, 0]])

det40 = np.linalg.det(arr40)

print(det40)

if det40 != 0:
    inv40 = np.linalg.inv(arr40)
    print(inv40)
else:
    print("Matrix is not invertible")


# 41. Compute eigenvalues and eigenvectors of a 2x2 matrix.
arr41 = np.array([[4, 2],
                  [1, 3]])

eigenvalues41, eigenvectors41 = np.linalg.eig(arr41)

print(eigenvalues41)
print(eigenvectors41)


# 42. Use np.cross and np.dot for vector calculations.
a42 = np.array([1, 2, 3])
b42 = np.array([4, 5, 6])

print(np.cross(a42, b42))
print(np.dot(a42, b42))


# 43. Compute outer product and explain difference from dot product.
a43 = np.array([1, 2, 3])
b43 = np.array([4, 5, 6])

print(np.outer(a43, b43))


# 44. Compute Kronecker product using np.kron.
a44 = np.array([[1, 2],
                [3, 4]])

b44 = np.array([[0, 5],
                [6, 7]])

print(np.kron(a44, b44))


# 45. Use np.linalg.norm to compute vector magnitude.
arr45 = np.array([3, 4])

print(np.linalg.norm(arr45))


# 46. Perform SVD on a matrix and reconstruct it from U @ S @ Vt.
arr46 = np.array([[1, 2],
                  [3, 4]])

U46, S46, Vt46 = np.linalg.svd(arr46)

S_matrix46 = np.diag(S46)

reconstructed46 = U46 @ S_matrix46 @ Vt46

print(U46)
print(S46)
print(Vt46)
print(reconstructed46)


# 47. Use np.unique to find unique elements and their counts in an array.
arr47 = np.array([1, 2, 2, 3, 4, 4, 4, 5])

unique47, counts47 = np.unique(arr47, return_counts=True)

print(unique47)
print(counts47)


# 48. Sort each row of a 2D array independently with np.sort.
arr48 = np.array([[3, 1, 2],
                  [9, 7, 8]])

print(np.sort(arr48, axis=1))


# 49. Find the indices that would sort an array using np.argsort.
arr49 = np.array([40, 10, 30, 20])

print(np.argsort(arr49))


# 50. Use np.argmax and np.argmin on a multi-dimensional array with axis.
arr50 = np.array([[1, 9, 3],
                  [7, 2, 6]])

print(np.argmax(arr50, axis=0))
print(np.argmin(arr50, axis=1))


# 51. Use boolean masks to select rows in a 2D array where column 0 > 5.
arr51 = np.array([[1, 2],
                  [6, 7],
                  [8, 9],
                  [3, 4]])

print(arr51[arr51[:, 0] > 5])


# 52. Use fancy indexing to pick rows [0,2,4] and columns [1,3] from a 5x5 array.
arr52 = np.arange(25).reshape(5, 5)

print(arr52[[0, 2, 4]][:, [1, 3]])


# 53. Stack two 1D arrays vertically and horizontally.
a53 = np.array([1, 2, 3])
b53 = np.array([4, 5, 6])

print(np.vstack((a53, b53)))
print(np.hstack((a53, b53)))


# 54. Use np.vstack, np.hstack, and np.column_stack on sample arrays.
a54 = np.array([1, 2, 3])
b54 = np.array([4, 5, 6])

print(np.vstack((a54, b54)))
print(np.hstack((a54, b54)))
print(np.column_stack((a54, b54)))


# 55. Use np.stack to create a new axis and explain axis parameter.
a55 = np.array([1, 2, 3])
b55 = np.array([4, 5, 6])

print(np.stack((a55, b55), axis=0))
print(np.stack((a55, b55), axis=1))


# 56. Split a 1D array into three equal parts using np.array_split.
arr56 = np.arange(9)

print(np.array_split(arr56, 3))


# 57. Split a 2D array vertically and horizontally with vsplit and hsplit.
arr57 = np.arange(16).reshape(4, 4)

print(np.vsplit(arr57, 2))
print(np.hsplit(arr57, 2))


# 58. Use np.repeat and np.tile to expand and tile arrays.
arr58 = np.array([1, 2, 3])

print(np.repeat(arr58, 2))
print(np.tile(arr58, 3))


# 59. Demonstrate np.ravel() vs np.flatten().
arr59 = np.array([[1, 2],
                  [3, 4]])

ravel59 = arr59.ravel()
flatten59 = arr59.flatten()

ravel59[0] = 100

print(arr59)
print(ravel59)
print(flatten59)


# 60. Use np.squeeze and np.expand_dims to change array dimensions.
arr60 = np.array([[[1, 2, 3]]])

print(np.squeeze(arr60))

expanded60 = np.expand_dims(np.array([1, 2, 3]), axis=0)

print(expanded60)


# 61. Reshape a (12,) array into (3,4) and then to (-1,2) using -1 inference.
arr61 = np.arange(12)

reshaped61 = arr61.reshape(3, 4)
print(reshaped61)

reshaped_again61 = reshaped61.reshape(-1, 2)
print(reshaped_again61)


# 62. Demonstrate np.resize vs ndarray.resize.
arr62 = np.array([1, 2, 3, 4])

print(np.resize(arr62, (8,)))

arr62.resize((6,))
print(arr62)


# 63. Use np.moveaxis and np.swapaxes on a shape (2,3,4) array.
arr63 = np.arange(24).reshape(2, 3, 4)

print(np.moveaxis(arr63, 0, -1).shape)
print(np.swapaxes(arr63, 0, 1).shape)


# 64. Use np.copy to create a deep copy and show modifying one doesn’t affect the other.
arr64 = np.array([1, 2, 3])

copy64 = np.copy(arr64)

copy64[0] = 100

print(arr64)
print(copy64)


# 65. Make a view of an array and demonstrate that changing the view changes original.
arr65 = np.array([1, 2, 3, 4])

view65 = arr65.view()

view65[0] = 999

print(arr65)
print(view65)


# 66. Use np.broadcast_to to expand a smaller array for arithmetic.
arr66 = np.array([1, 2, 3])

broadcast66 = np.broadcast_to(arr66, (3, 3))

print(broadcast66)


# 67. Given an array, use slicing to create a subarray and then update the original via the view.
arr67 = np.array([1, 2, 3, 4, 5])

sub67 = arr67[1:4]

sub67[0] = 200

print(arr67)
print(sub67)


# 68. Create a structured array with dtype fields.
arr68 = np.array([
    ("Alice", 21),
    ("Bob", 25),
    ("Charlie", 22)
], dtype=[("name", "U10"), ("age", "i4")])

print(arr68)
print(arr68["name"])
print(arr68["age"])


# 69. Convert a NumPy array to a Python list and back.
arr69 = np.array([1, 2, 3, 4])

list69 = arr69.tolist()
print(list69)

new_arr69 = np.array(list69)
print(new_arr69)


# 70. Compute correlation matrix of a 2D dataset using NumPy.
arr70 = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9]
])

print(np.corrcoef(arr70))


# 71. Center and scale a dataset using broadcasting.
arr71 = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

mean71 = np.mean(arr71, axis=0)
std71 = np.std(arr71, axis=0)

scaled71 = (arr71 - mean71) / std71

print(scaled71)


# 72. Compute rolling mean of a 1D array using convolution.
arr72 = np.array([1, 2, 3, 4, 5])

kernel72 = np.ones(3) / 3

rolling_mean72 = np.convolve(arr72, kernel72, mode='valid')

print(rolling_mean72)


# 73. Compute percentiles (25th, 50th, 75th) using np.percentile.
arr73 = np.array([10, 20, 30, 40, 50])

print(np.percentile(arr73, 25))
print(np.percentile(arr73, 50))
print(np.percentile(arr73, 75))


# 74. Use np.digitize to bin data into intervals.
data74 = np.array([5, 15, 25, 35, 45])

bins74 = [10, 20, 30, 40]

print(np.digitize(data74, bins74))


# 75. Generate normally distributed random numbers with given mean and std.
arr75 = np.random.normal(loc=50, scale=5, size=10)

print(arr75)


# 76. Draw samples from binomial, Poisson, and exponential distributions.
binomial76 = np.random.binomial(n=10, p=0.5, size=5)
poisson76 = np.random.poisson(lam=3, size=5)
exponential76 = np.random.exponential(scale=2, size=5)

print(binomial76)
print(poisson76)
print(exponential76)


# 77. Demonstrate np.random.choice with and without replacement.
arr77 = np.array([1, 2, 3, 4, 5])

print(np.random.choice(arr77, size=3, replace=True))
print(np.random.choice(arr77, size=3, replace=False))


# 78. Shuffle a 1D array in-place and show difference from np.random.permutation.
arr78 = np.array([1, 2, 3, 4, 5])

np.random.shuffle(arr78)
print(arr78)

perm78 = np.random.permutation(arr78)
print(perm78)


# 79. Explain seeding and reproducibility using np.random.seed.
np.random.seed(10)
print(np.random.rand(5))

np.random.seed(10)
print(np.random.rand(5))


# 80. Implement Monte Carlo estimation of π using NumPy random sampling.
points80 = 100000

x80 = np.random.rand(points80)
y80 = np.random.rand(points80)

inside80 = (x80**2 + y80**2) <= 1

pi_estimate80 = 4 * np.sum(inside80) / points80

print(pi_estimate80)


import time

# 81. Use vectorized code to compute pairwise Euclidean distances between row vectors.
arr81 = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

dist81 = np.sqrt(((arr81[:, np.newaxis] - arr81) ** 2).sum(axis=2))

print(dist81)


# 82. Compute pairwise cosine similarity of rows in a matrix (vectorized).
arr82 = np.array([
    [1, 0],
    [0, 1],
    [1, 1]
])

dot82 = arr82 @ arr82.T

norm82 = np.linalg.norm(arr82, axis=1)

cosine82 = dot82 / (norm82[:, None] * norm82)

print(cosine82)


# 83. Implement element-wise clipping of values between min and max.
arr83 = np.array([-10, 5, 15, 25, 35])

print(np.clip(arr83, 0, 20))


# 84. Work with complex dtype: create complex128 array and compute conjugates.
arr84 = np.array([1+2j, 3+4j, 5+6j], dtype=np.complex128)

print(arr84)
print(np.conjugate(arr84))


# 85. Create structured arrays and sort them by a field.
arr85 = np.array([
    ("Alice", 25),
    ("Bob", 20),
    ("Charlie", 23)
], dtype=[("name", "U10"), ("age", "i4")])

sorted85 = np.sort(arr85, order="age")

print(sorted85)


# 86. Use masked arrays (np.ma) to ignore invalid entries in computations.
arr86 = np.array([1, 2, -999, 4, -999, 6])

masked86 = np.ma.masked_equal(arr86, -999)

print(masked86)
print(masked86.mean())


# 87. Build a boolean mask for prime numbers up to N using vectorized operations.
N87 = 30

prime87 = np.ones(N87 + 1, dtype=bool)

prime87[:2] = False

for i in range(2, int(np.sqrt(N87)) + 1):
    if prime87[i]:
        prime87[i*i:N87+1:i] = False

print(np.where(prime87)[0])


# 88. Benchmark list comprehension vs NumPy vectorized operations for large array multiplication.
size88 = 1000000

list88 = list(range(size88))
array88 = np.arange(size88)

start88 = time.time()
result_list88 = [x * 2 for x in list88]
end88 = time.time()

print(end88 - start88)

start88 = time.time()
result_array88 = array88 * 2
end88 = time.time()

print(end88 - start88)


# 89. Measure memory usage of a Python list vs NumPy array for 1 million integers.
import sys

list89 = list(range(1000000))
array89 = np.arange(1000000)

print(sys.getsizeof(list89))
print(array89.nbytes)


# 90. Show behavior of integer division vs float division with arrays and dtype.
arr90_a = np.array([5, 10, 15])
arr90_b = np.array([2, 2, 2])

print(arr90_a // arr90_b)
print(arr90_a / arr90_b)


# 91. Demonstrate overflow behavior for int8 by creating values beyond 127.
arr91 = np.array([127], dtype=np.int8)

print(arr91)

overflow91 = arr91 + 1

print(overflow91)


# 92. Show precision differences between float32 and float64 with cumulative sum.
arr92_float32 = np.ones(1000000, dtype=np.float32) * 0.1
arr92_float64 = np.ones(1000000, dtype=np.float64) * 0.1

print(np.sum(arr92_float32))
print(np.sum(arr92_float64))


# 93. Use np.set_printoptions to control display precision and suppression of scientific notation.
np.set_printoptions(precision=2, suppress=True)

arr93 = np.array([1.123456789, 123456789.123456789])

print(arr93)


# 94. Flatten a 3D array to 1D and reshape back while preserving order.
arr94 = np.arange(24).reshape(2, 3, 4)

flat94 = arr94.flatten()

print(flat94)

reshaped94 = flat94.reshape(2, 3, 4)

print(reshaped94)


# 95. Reorder axes so that axis 0 becomes last using np.transpose.
arr95 = np.arange(24).reshape(2, 3, 4)

transposed95 = np.transpose(arr95, (1, 2, 0))

print(transposed95.shape)


# 96. Use np.einsum to compute matrix multiplication.
a96 = np.array([[1, 2],
                [3, 4]])

b96 = np.array([[5, 6],
                [7, 8]])

result96 = np.einsum('ij,jk->ik', a96, b96)

print(result96)


# 97. Use np.einsum to compute trace, outer product, and sum along axes.
arr97 = np.array([[1, 2],
                  [3, 4]])

print(np.einsum('ii', arr97))

a97 = np.array([1, 2, 3])
b97 = np.array([4, 5])

print(np.einsum('i,j->ij', a97, b97))

print(np.einsum('ij->i', arr97))


# 98. Optimize a simple numeric algorithm by replacing Python loops with NumPy vectorization.
list98 = list(range(1000000))

start98 = time.time()

squares98 = [x**2 for x in list98]

end98 = time.time()

print(end98 - start98)

array98 = np.arange(1000000)

start98 = time.time()

squares_np98 = array98**2

end98 = time.time()

print(end98 - start98)


# 99. Compare performance of np.sum(arr) vs arr.sum() vs Python sum() on an array.
arr99 = np.arange(1000000)

start99 = time.time()
print(np.sum(arr99))
print(time.time() - start99)

start99 = time.time()
print(arr99.sum())
print(time.time() - start99)

start99 = time.time()
print(sum(arr99))
print(time.time() - start99)


# 100. Demonstrate using np.add.reduce and compare to np.sum.
arr100 = np.array([1, 2, 3, 4, 5])

print(np.add.reduce(arr100))
print(np.sum(arr100))


# 101. Use np.apply_along_axis to apply a function to rows and explain performance caveats.
arr101 = np.array([[1, 2, 3], [4, 5, 6]])

result101 = np.apply_along_axis(lambda row: np.sum(row), 1, arr101)

print(result101)


# 102. Given two sorted arrays, find intersection using np.intersect1d.
arr102_a = np.array([1, 2, 3, 4, 5])
arr102_b = np.array([3, 4, 5, 6, 7])

print(np.intersect1d(arr102_a, arr102_b))


# 103. Given two arrays, find elements in A not in B using np.setdiff1d.
arr103_a = np.array([1, 2, 3, 4, 5])
arr103_b = np.array([3, 4, 6])

print(np.setdiff1d(arr103_a, arr103_b))


# 104. Reconstruct a matrix from its flattened form index mapping (ravel multi-index conversion).
arr104 = np.array([[10, 20], [30, 40]])

flat104 = arr104.ravel()

indices104 = np.unravel_index([0, 1, 2, 3], arr104.shape)

print(flat104)
print(indices104)


# 105. Demonstrate type promotion rules when combining int32 and float64.
arr105_int = np.array([1, 2, 3], dtype=np.int32)
arr105_float = np.array([1.5, 2.5, 3.5], dtype=np.float64)

result105 = arr105_int + arr105_float

print(result105)
print(result105.dtype)


# 106. Create an array of datetime64 values and convert to string representations.
dates106 = np.array(['2025-01-01', '2025-01-02', '2025-01-03'], dtype='datetime64')

print(dates106)
print(dates106.astype(str))


# 107. Compute differences between consecutive dates using np.diff on datetime64 array.
dates107 = np.array(['2025-01-01', '2025-01-03', '2025-01-06'], dtype='datetime64')

diff107 = np.diff(dates107)

print(diff107)


# 108. Convert unix timestamps to datetime64[s] and extract year/month/day numerically.
timestamps108 = np.array([1700000000, 1710000000], dtype='int64')

dates108 = timestamps108.astype('datetime64[s]')

print(dates108)

years108 = dates108.astype('datetime64[Y]').astype(int) + 1970
months108 = dates108.astype('datetime64[M]').astype(int) % 12 + 1
days108 = (dates108.astype('datetime64[D]') - dates108.astype('datetime64[M]')).astype(int) + 1

print(years108)
print(months108)
print(days108)


# 109. Compare np.log1p(x) vs np.log(1 + x) on tiny x values numerically.
x109 = np.array([1e-10, 1e-15, 1e-20])

print(np.log1p(x109))
print(np.log(1 + x109))


# 110. Use np.expm1 and explain when it’s preferable to np.exp(x) - 1.
x110 = np.array([1e-10, 1e-15, 1e-20])

print(np.expm1(x110))
print(np.exp(x110) - 1)


# 111. Build a function that computes stable log-sum-exp across axis.
arr111 = np.array([[1, 2, 3], [4, 5, 6]])

def stable_logsumexp(x, axis=None):
    max_x = np.max(x, axis=axis, keepdims=True)
    return np.log(np.sum(np.exp(x - max_x), axis=axis)) + np.squeeze(max_x)

print(stable_logsumexp(arr111, axis=1))


# 112. Compute element-wise np.maximum between arrays and explain broadcasting rules.
arr112_a = np.array([1, 5, 3])
arr112_b = np.array([2, 2, 4])

print(np.maximum(arr112_a, arr112_b))


# 113. Use np.select to implement multi-condition piecewise array computation.
arr113 = np.array([5, 15, 25, 35])

conditions113 = [
    arr113 < 10,
    (arr113 >= 10) & (arr113 < 30),
    arr113 >= 30
]

choices113 = ['Low', 'Medium', 'High']

result113 = np.select(conditions113, choices113)

print(result113)


# 114. Use np.nonzero and np.where to find indices of elements satisfying condition.
arr114 = np.array([10, 15, 20, 25, 30])

print(np.nonzero(arr114 > 20))
print(np.where(arr114 % 10 == 0))


# 115. Implement topological sort checking using adjacency matrices (small graph).
adj115 = np.array([
    [0, 1, 1],
    [0, 0, 1],
    [0, 0, 0]
])

in_degree115 = np.sum(adj115, axis=0)

print(in_degree115)

print(np.where(in_degree115 == 0)[0])


# 116. Use boolean algebra with NumPy arrays to compute union/intersection of masks.
arr116 = np.array([1, 2, 3, 4, 5, 6])

mask116_a = arr116 % 2 == 0
mask116_b = arr116 > 3

print(mask116_a | mask116_b)   # Union
print(mask116_a & mask116_b)   # Intersection


# 117. Write a function that computes pairwise Pearson correlation coefficients between columns.
arr117 = np.array([
    [1, 2, 3],
    [2, 4, 6],
    [3, 6, 9],
    [4, 8, 12]
])

def pairwise_corrcoef(arr):
    return np.corrcoef(arr, rowvar=False)

print(pairwise_corrcoef(arr117))
