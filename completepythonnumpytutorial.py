#Complete Python NumPy Tutorial (Creating Arrays, Indexing, Math, Statistics, Reshaping) [720p]
#keithgalli
#NumPy is a multi-dimensional array library.  One dimensional array shape(4,) four across or four columns.  Two dimensional array shape(2,3) two down, three across or two rows, three columns.  Three dimensional array shape(4,3,2) four down, three towards you, two away.
#Lists and Numpy both insert, delete, append, concatenate, etc.  Numpy does lots more.  e.g., a=[1,3,5] b=[1,2,3] a*b=error.  a=np.array([1,3,5]) b=np.array([1,2,3]) a*b=np.array([1,6,15])
#NumPy applications:  MATLAB replacement, plotting (Matplotlib), Backend (Pandas, Connect 4, Digital Photography store images), Machine Learning.
import numpy as np

a = np.array([1,2,3])
print(a) #print [1 2 3]
b = np.array([[9.0,8.0,7.0],[6.0, 5.0, 4.0]])
print(b)
'''
[[ 9.  8.  7.]
 [ 6.  5.  4.]]
'''
#number of dimensions
print(a.ndim) #print 1
print(b.ndim) #print 2
#numpy array shape count rows count columns
print(a.shape) #print (3,)
print(b.shape) #print (2, 3)
#numpy number of elements
print(a.size) #print 3
print(b.size) #print 6
#get data type
print(a.dtype) #print int64
print(b.dtype) #print float64
#array size, array memory size
print(a.itemsize) #print 8.  Memory size each item.
print(a.size) #print 3.  Total number of elements.
print(a.nbytes) #print 24.  Total memory size or itemsize*size.
print(b.itemsize) #print 8.  Memory size each item.
print(b.size) #print 6.  Total number of elements.
print(b.nbytes) #print 48.  Total memory size or itemsize*size.
#assign data type.  Reduce memory size for integers.
a2 = np.array([1,2,3], dtype=np.int16)
print(a2.dtype) #print int16
print("\n")

#slicing
a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
print(a)
'''
[[ 1  2  3  4  5  6  7]
 [ 8  9 10 11 12 13 14]]
'''
print(a.shape) #print (2, 7)
print(a[1,5]) #print 13
print(a[1,-2]) #print 13
print(a[0]) #print [1 2 3 4 5 6 7]
print(a[0,:]) #print [1 2 3 4 5 6 7]
print(a[0:,2]) #print [ 3 10]
print(a[:,2]) #print [ 3 10]
print(a[0,1:6:2]) #print [2 4 6].  Skip elements in a row.  Row zero.  Start index one.  End index five.  Skip one element or include every other element.
print(a[0,1:-1:2]) #print [2 4 6].  Skip elements in a row.  Row zero.  Start index one.  End index five.  Skip one element or include every other element.

#updating, editing, change
a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
print(a)
'''
[[ 1  2  3  4  5  6  7]
 [ 8  9 10 11 12 13 14]]
'''
a[1,5] = 20
print(a)
'''
[[ 1  2  3  4  5  6  7]
 [ 8  9 10 11 12 20 14]]
'''
a[0:,2] = 5
print(a)
'''
[[ 1  2  5  4  5  6  7]
 [ 8  9  5 11 12 20 14]]
'''
a[0:,2] = [100, 200]
print(a)
'''
[[  1   2 100   4   5   6   7]
 [  8   9 200  11  12  20  14]]
'''

#3-d three dimension array
b = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(b)
'''
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
'''
#work outside in
print(b[0,1,1]) #print 4
print(b[:,1,:])
'''
[[3 4]
 [7 8]]
'''
print(b[:,0,:])
'''
[[1 2]
 [5 6]]
'''
print(b[:,0,0]) #print [1 5]
b[:,1,:] = [[9,9], [8,8]]
print(b)
'''
[[[1 2]
  [9 9]]

 [[5 6]
  [8 8]]]
'''

a = np.zeros(5)
print(a) #print [ 0.  0.  0.  0.  0.]
aint32 = np.zeros(5, dtype=np.int32)
print(aint32) #print [0 0 0 0 0]
a = np.zeros([2,3])
print(a)
'''
[[ 0.  0.  0.]
 [ 0.  0.  0.]]
'''
a = np.ones([4,4])
print(a)
'''
[[ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]]
'''
a = np.full([2,2], 99, dtype=np.float32)
print(a)
'''
[[ 99.  99.]
 [ 99.  99.]]
'''
a = np.array([[1,2,3,4,5,6,7], [8,9,10,11,12,13,14]])
print(a)
'''
[[ 1  2  3  4  5  6  7]
 [ 8  9 10 11 12 13 14]]
'''
alike = np.full_like(a, 4)
print(alike)
'''
[[4 4 4 4 4 4 4]
 [4 4 4 4 4 4 4]]
'''
alike = np.full_like(a, .9, dtype=np.float)
print(alike)
'''
[[ 0.9  0.9  0.9  0.9  0.9  0.9  0.9]
 [ 0.9  0.9  0.9  0.9  0.9  0.9  0.9]]
'''
a = np.random.random([4,2])
print(a)
'''
[[ 0.54789021  0.34317282]
 [ 0.93810684  0.88204281]
 [ 0.80214372  0.873687  ]
 [ 0.01499133  0.34825153]]
'''
a = np.array([[1,2,3,4,5,6,7],[8,9,10,11,12,13,14]])
print(a)
'''
[[ 1  2  3  4  5  6  7]
 [ 8  9 10 11 12 13 14]]
'''
print(a.shape)
a = np.random.random(a.shape)
print(a) #print (2, 7)
'''
[[ 0.16428964  0.34438615  0.06215844  0.56664062  0.24604828  0.26907974
   0.53226375]
 [ 0.09890719  0.31920714  0.02603717  0.50141899  0.10801047  0.96546719
   0.20916181]]
'''
a = np.random.randint(7, size=[4,2]) #number is from 0 to 7 exclusive
print(a)
'''
[[6 2]
 [6 5]
 [0 3]
 [4 6]]
'''
a = np.random.randint(20, 31, size=[2,2]) #number is from 20 to 31 exclusive
print(a)
'''
[[20 30]
 [29 28]]
'''
#an identity matrix is a square matrix
a = np.identity(3)
print(a)
'''
[[ 1.  0.  0.]
 [ 0.  1.  0.]
 [ 0.  0.  1.]]
'''
a = np.identity(3, dtype="int")
print(a)
'''
[[1 0 0]
 [0 1 0]
 [0 0 1]]
'''
a = np.array([1,2,3])
print(a) #print [1 2 3]
repeata = np.repeat(a,3)
print(repeata) #print [1 1 1 2 2 2 3 3 3]
repeata = np.repeat(a,5)
print(repeata) #print [1 1 1 1 1 2 2 2 2 2 3 3 3 3 3]
a = np.array([[1,2,3]])
print(a) #print [[1 2 3]]
repeata = np.repeat(a,3, axis=0)
print(repeata)
'''
[[1 2 3]
 [1 2 3]
 [1 2 3]]
'''
repeata = np.repeat(a,3, axis=1)
print(repeata) #print [[1 1 1 2 2 2 3 3 3]]

exercise = np.ones([5,5], dtype=np.int)
exercise[2,2] = 9
exercise[1,1:4] = 0
exercise[2,1] = 0
exercise[2,3] = 0
exercise[3,1:4] = 0
print(exercise)
'''
[[1 1 1 1 1]
 [1 0 0 0 1]
 [1 0 9 0 1]
 [1 0 0 0 1]
 [1 1 1 1 1]]
'''
#there must be a faster solution.  Instructor's solution.
output = np.ones([5,5], dtype=np.int)
z = np.zeros([3,3], dtype=np.int)
z[1,1] = 9
output[1:4,1:4] =  z  #replace rows 1-3 and columns 1-3 with z.  Ending number is exclusive.  output[1:-1,1:-1] =  z also works.
print(output)
'''
[[1 1 1 1 1]
 [1 0 0 0 1]
 [1 0 9 0 1]
 [1 0 0 0 1]
 [1 1 1 1 1]]
'''

#use .copy() when copying arrays.  Keep the copied array separate from original source.
a = np.array([1,2,3])
b = a
b[0] = 100
print(a) #print [100   2   3]
a = np.array([1,2,3])
b = a.copy()
b[0] = 100
print(a) #print [1   2   3]
print(b) #print [100   2   3]

#Mathematics
a = np.array([1,2,3,4])
print(a) #print [1 2 3 4]
print(a+2) #print [3 4 5 6]
print(a-2) #print [-1  0  1  2]
print(a*2) #print [2 4 6 8]
print(a/2) #print [ 0.5  1.   1.5  2. ]
b = np.array([1,0,1,0])
print(a+b) #print [2 2 4 4]
print(a**2) #print [ 1  4  9 16]
print(np.sin(a)) #print [ 0.84147098  0.90929743  0.14112001 -0.7568025 ]
#Just watched Linear Algebra
stats = np.array([[1,2,3],[6,5,4]])
print(stats)
'''
[[1 2 3]
 [6 5 4]]
'''
print(np.min(stats)) #print 1
print(np.max(stats)) #print 6
print(np.min(stats, axis=0)) #print [1 2 3]
print(np.min(stats, axis=1)) #print [1 4]
print(np.sum(stats)) #print 21
print(np.sum(stats, axis=0)) #print [7 7 7]
print(np.sum(stats, axis=1)) #print [ 6 15]

before = np.array([[1,2,3,4],[5,6,7,8]])
print(before)
'''
[[1 2 3 4]
 [5 6 7 8]]
'''
after81 = before.reshape((8,1))
print(after81)
'''
[[1]
 [2]
 [3]
 [4]
 [5]
 [6]
 [7]
 [8]]
'''
after42 = before.reshape((4,2))
print(after42)
'''
[[1 2]
 [3 4]
 [5 6]
 [7 8]]
'''
v1 = np.array([1,2,3,4])
v2 = np.array([5,6,7,8])
print(np.vstack([v1,v2]))
'''
[[1 2 3 4]
 [5 6 7 8]]
'''
print(np.vstack([v1,v2,v2,v2]))
'''
[[1 2 3 4]
 [5 6 7 8]
 [5 6 7 8]
 [5 6 7 8]]
'''
print(np.hstack([v1,v2])) #print [1 2 3 4 5 6 7 8]
h1 = np.ones((2,4), dtype=np.int)
h2 = np.zeros((2,2), dtype=np.int)
print(np.hstack((h1,h2)))
'''
[[1 1 1 1 0 0]
 [1 1 1 1 0 0]]
'''

numberstext = (np.genfromtxt('data.txt', delimiter=','))
print(numberstext)
'''
[[   1.   13.   21.   11.  196.   75.    4.    3.   34.    6.    7.    8.
     0.    1.    2.    3.    4.    5.]
 [   3.   42.   12.   33.  766.   75.    4.   55.    6.    4.    3.    4.
     5.    6.    7.    0.   11.   12.]
 [   1.   22.   33.   11.  999.   11.    2.    1.   78.    0.    1.    2.
     9.    8.    7.    1.   76.   88.]]     
'''
print(numberstext.astype('int32'))
'''
[[  1  13  21  11 196  75   4   3  34   6   7   8   0   1   2   3   4   5]
 [  3  42  12  33 766  75   4  55   6   4   3   4   5   6   7   0  11  12]
 [  1  22  33  11 999  11   2   1  78   0   1   2   9   8   7   1  76  88]]
'''
print(np.hstack(numberstext))
'''
[   1.   13.   21.   11.  196.   75.    4.    3.   34.    6.    7.    8.
    0.    1.    2.    3.    4.    5.    3.   42.   12.   33.  766.   75.
    4.   55.    6.    4.    3.    4.    5.    6.    7.    0.   11.   12.
    1.   22.   33.   11.  999.   11.    2.    1.   78.    0.    1.    2.
    9.    8.    7.    1.   76.   88.]
'''
numberstextinteger = (np.genfromtxt('data.txt', delimiter=',', dtype=np.int))
print(np.hstack(numberstextinteger))
'''
[  1  13  21  11 196  75   4   3  34   6   7   8   0   1   2   3   4   5
   3  42  12  33 766  75   4  55   6   4   3   4   5   6   7   0  11  12
   1  22  33  11 999  11   2   1  78   0   1   2   9   8   7   1  76  88]
'''
for eachnumberstextinteger in numberstextinteger:
	print(eachnumberstextinteger)
	'''
	[  1  13  21  11 196  75   4   3  34   6   7   8   0   1   2   3   4   5]
	[  3  42  12  33 766  75   4  55   6   4   3   4   5   6   7   0  11  12]
	[  1  22  33  11 999  11   2   1  78   0   1   2   9   8   7   1  76  88]
	'''
print(numberstextinteger.shape) #print (3, 18)
print(numberstextinteger.shape[0]) #print 3
for eachrow in range(0,numberstextinteger.shape[0]):
	for eachindex in range(0,numberstextinteger.shape[1]):
		print(numberstextinteger[eachrow,eachindex], end=",") #print 1,13,21,11,196,75,4,3,34,6,7,8,0,1,2,3,4,5,3,42,12,33,766,75,4,55,6,4,3,4,5,6,7,0,11,12,1,22,33,11,999,11,2,1,78,0,1,2,9,8,7,1,76,88,
print("\n")

#boolean masking and advanced indexing
filedata = (np.genfromtxt('data.txt', delimiter=','))
print(filedata)
'''
[[   1.   13.   21.   11.  196.   75.    4.    3.   34.    6.    7.    8.
     0.    1.    2.    3.    4.    5.]
 [   3.   42.   12.   33.  766.   75.    4.   55.    6.    4.    3.    4.
     5.    6.    7.    0.   11.   12.]
 [   1.   22.   33.   11.  999.   11.    2.    1.   78.    0.    1.    2.
     9.    8.    7.    1.   76.   88.]]
'''
print(filedata > 50)
'''
[[False False False False  True  True False False False False False False
  False False False False False False]
 [False False False False  True  True False  True False False False False
  False False False False False False]
 [False False False False  True False False False  True False False False
  False False False False  True  True]]
'''
print(filedata[filedata > 50]) #print [ 196.   75.  766.   75.   55.  999.   78.   76.   88.]
print(np.any(filedata > 50, axis=0)) #print [False False False False  True  True False  True  True False False False False False False False  True  True] #Looking at each column is any number greater than 50
print(np.all(filedata > 50, axis=0)) #print[False False False False  True False False False False False False False False False False False False False] #Looking at each column is all numbers greater than 50
print(np.all(filedata > 50, axis=1)) #print[False False False] #Looking at each row is all numbers greater than 50
print(((filedata > 50) & (filedata < 100)))
'''
[[False False False False False  True False False False False False False
  False False False False False False]
 [False False False False False  True False  True False False False False
  False False False False False False]
 [False False False False False False False False  True False False False
  False False False False  True  True]]
'''
print(~((filedata > 50) & (filedata < 100))) #tilda ~ is not or opposite
'''
[[ True  True  True  True  True False  True  True  True  True  True  True
   True  True  True  True  True  True]
 [ True  True  True  True  True False  True False  True  True  True  True
   True  True  True  True  True  True]
 [ True  True  True  True  True  True  True  True False  True  True  True
   True  True  True  True False False]]
'''
print([(filedata > 50) & (filedata < 100)])
'''
[array([[False, False, False, False, False,  True, False, False, False,
        False, False, False, False, False, False, False, False, False],
       [False, False, False, False, False,  True, False,  True, False,
        False, False, False, False, False, False, False, False, False],
       [False, False, False, False, False, False, False, False,  True,
        False, False, False, False, False, False, False,  True,  True]], dtype=bool)]
'''
print(filedata[(filedata > 50) & (filedata < 100)])  #print [ 75.  75.  55.  78.  76.  88.]

#you can index with a list in NumPy
a = np.arange(1,10)
print(a) #print [1 2 3 4 5 6 7 8 9]
print(a[[1,2,8]]) #print [2 3 9]
print(a[[False, False, False, True, False, False, False, True, True]]) #print [4 8 9]

thirty = np.arange(1,31)
print(thirty) #print [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30]
thirty65 = thirty.reshape(6,5)
print(thirty65)
'''
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]
 [11 12 13 14 15]
 [16 17 18 19 20]
 [21 22 23 24 25]
 [26 27 28 29 30]]
'''
print(thirty65[2:4,0:2])
'''
[[11 12]
 [16 17]]
'''
print(thirty65[[0,1],[1,2]]) #print [2 8]
#print(thirty65[[0,1],[1,2],[2,3],[3,4]]) #error message
print(thirty65[[0,1,2,3],[1,2,3,4]]) #print [ 2  8 14 20]
print(thirty65[[0,0,4,4,5,5],[3,4,3,4,3,4]]) #print [ 4  5 24 25 29 30]
print(thirty65[[0,4,5],3:])
'''
[[ 4  5]
 [24 25]
 [29 30]]
'''