#Introduction to Numerical Computing with NumPy SciPy 2019 Tutorial Alex Chabot-Leclerc www.enthought.com

import numpy as np

a = [1, 2, 3, 4, 5]
b = [10, 11, 12, 13, 14]
print(a+b) #print [1, 2, 3, 4, 5, 10, 11, 12, 13, 14]
result = []
for eacha, eachb, in zip(a, b):
	result.append(eacha+eachb)
print(result) #print [11, 13, 15, 17, 19]

a = np.array([1, 2, 3, 4, 5])
print(type(a)) #print <class 'numpy.ndarray'>
print(a.dtype) #print int64  #RM:  integer 64 bit
print("number of dimensions",a.ndim) #print number of dimensions 1

print("shape always returns a tuple shows number of elements across each dimension",a.shape) #print shape always returns a tuple shows number of elements across each dimension (5,)
print("size always returns number of elements",a.size) #print size always returns number of elements 5
print(a[0]) #print 1
a[0] = 10
print(a) #print [10  2  3  4  5]
a[0] = 11.5
print(a) #print [11  2  3  4  5]  #type coercion.  Assign a float to integer truncates decimal part.  Assign an integer to float adds decimal.
f = np.array([1.2, 2.3, 4.5, 5.6, 7.8])
print(f.dtype) #print float64  #RM:  float point or fractional point  64 bit
print(a+f) #print [  12.2   4.3   7.5   9.6  12.8]
print(a/f) #print [ 9.16666667  0.86956522  0.66666667  0.71428571  0.64102564]
print(a**f) #print [  1.77693369e+01   4.92457765e+00   1.40296115e+02   2.35253423e+03   2.83117056e+05]
print(a*f) #print [ 13.2   4.6  13.5  22.4  39. ]
print(a*10) #print [110  20  30  40  50]
print(np.sin(a)) #print [-0.99999021  0.90929743  0.14112001 -0.7568025  -0.95892427]  #RM:  sin from trigonometry

a = np.array([[0, 1, 2, 3], [10, 11, 12, 13]]) #two-dimension array
print(a) #print [[ 0  1  2  3]\n [10 11 12 13]]
print(a[1]) #print [10 11 12 13]
print(a[1, 2]) #print 12
a[0, 3] = 987
print(a[0]) #print [  0   1   2 987]
print("number of dimensions",a.ndim) #number of dimensions 2
print("shape always returns a tuple shows number of elements across each dimension (number of rows, number of elements per dimension)",a.shape) #shape always returns a tuple shows number of elements across each dimension (number of rows, number of elements per dimension) (2, 4)
print("size always returns number of elements",a.size) #print size always returns number of elements 8

#slicing
#Extracts a portion of a sequence by specifying a lower bound and an upper bound.  The lower bound is included.  The upper bound is excluded.  Mathematically [upper:lower).  The step value specifies the stride between elements.
#variable[lower:upper:step]  If skipping or stepping, need two colons.
'''
 -5  -4  -3  -2  -1  negative index
  0   1   2   3   4  positive index
 10  11  12  13  14
'''
indexstringtest = "The quick brown fox jumped over the lazy dog"
print(indexstringtest[11:37]) #print rown fox jumped over the l
print(indexstringtest[11:-7]) #print rown fox jumped over the l
print(indexstringtest[11:37] == indexstringtest[11:-7]) #print True
print(indexstringtest[-33:37]) #print rown fox jumped over the l
a = np.array([10, 11, 12, 13, 14])
print(a) #print [10 11 12 13 14]
print(a[1:3]) #print [11 12]
print(a[1:-2]) #print [11 12]
print(a[-4:3]) #print [11 12]
print(a[:3]) #print [10 11 12]
print(a[-5:-2]) #print [10 11 12]
print(a[-2:]) #print [13 14] 
print(a[3:]) #print [13 14]
print(a[::2]) #print [10 12 14]
print(a[::-2]) #print [14 12 10]
a65 = np.array([[0, 1, 2, 3, 4, 5], [10, 11, 12, 13, 14, 15], [20, 21, 22, 23, 24, 25], [30, 31, 32, 33, 34, 35], [40, 41, 42, 43, 44, 45], [50, 51, 52, 53, 54, 55], [60, 61, 62, 63, 64, 65]])
print(a65)
'''
[[ 0  1  2  3  4  5]
 [10 11 12 13 14 15]
 [20 21 22 23 24 25]
 [30 31 32 33 34 35]
 [40 41 42 43 44 45]
 [50 51 52 53 54 55]
 [60 61 62 63 64 65]
 ]
'''
print(a65.ndim) #print 2
print(a65.shape) #print (7, 6)
print(a65.size) #print 42
print(a65[1, 2:5]) #print [12 13 14]
print(a65[4:, 4:])
'''
[[44 45]
 [54 55]
 [64 65]]
 '''
print(a65[:, 2]) #print [ 2 12 22 32 42 52 62]
print(a65[0:, 2]) #print [ 2 12 22 32 42 52 62]
print(a65[2::2, ::4]) #RM:  same as print(a65[2::2, 0::4])
'''
[[20 24]
 [40 44]
 [60 64]]
'''
practicea = np.arange(25).reshape(5,5)
print(practicea)
'''
[[ 0  1  2  3  4]
 [ 5  6  7  8  9]
 [10 11 12 13 14]
 [15 16 17 18 19]
 [20 21 22 23 24]]
'''
redcolumns = practicea[0:, 1:4:2]
print(redcolumns)
'''
[[ 1  3]
 [ 6  8]
 [11 13]
 [16 18]
 [21 23]]
'''
yellowrow = practicea[4]  #RM:  yellowrow = practicea[-1] or yellowrow = practicea[4, :] is valid
print(yellowrow) #print [20 21 22 23 24]
bluesquares = practicea[1:4:2, 0:4:2]  #RM:  bluesquares = practicea[1::2, :3:2] is valid
print(bluesquares)
'''
[[ 5  7]
 [15 17]]
'''
copyarray = np.array([1, 2, 3, 4])
copiedarray = copyarray[:2]
print(copiedarray) #print [1 2]
copiedarray[0] = -1
print(copiedarray) #print [-1  2]
print(copyarray) #print [-1  2  3  4]  #RM:  copyarray is modified, too.  Index 0 is -1.  copiedarray is new array.  It's not new data.  The new array points to the original array.  Use .copy() to copy an array.
copyarray = np.array([1, 2, 3, 4])
copiedarray = copyarray.copy()  #RM:  copy array
print(copyarray) #print [1 2 3 4]
print(copiedarray) #print [1 2 3 4]
copiedarray[0] = -1
print(copyarray) #print [1 2 3 4]
print(copiedarray) #print [-1 2 3 4]
a = np.arange(0, 5, 1)
print(a) #print [0 1 2 3 4]
a[-2:] = [-1, -2]
print(a) #print [ 0  1  2 -1 -2]
a[-2:] = [99]
print(a) #print [ 0  1  2 99 99]
zerosarray = np.empty((5,7), dtype=np.str)
print(zerosarray)
'''
[['' '' '' '' '' '' '']
 ['' '' '' '' '' '' '']
 ['' '' '' '' '' '' '']
 ['' '' '' '' '' '' '']
 ['' '' '' '' '' '' '']]
'''
zerosarray[1][3] = "X"
zerosarray[2][2:5] = "X"
zerosarray[3][3] = "X"
print(zerosarray)
'''
[['' '' '' '' '' '' '']
 ['' '' '' 'X' '' '' '']
 ['' '' 'X' 'X' 'X' '' '']
 ['' '' '' 'X' '' '' '']
 ['' '' '' '' '' '' '']]
'''
emptyarray = np.empty((5,7), dtype=np.str)
print(emptyarray)
'''
[['' '' '' '' '' '' '']
 ['' '' '' '' '' '' '']
 ['' '' '' '' '' '' '']
 ['' '' '' '' '' '' '']
 ['' '' '' '' '' '' '']]
'''

#Fancing Indexing or Masking or Boolean Indexing
#Index by position and by value.  Numpy returns the values at the given positions or given indicies.  Can replace values, too.
a = np.arange(0, 80, 10)
print(a) #print [ 0 10 20 30 40 50 60 70]
indicesposition = [1, 2, -3]
y = a[indicesposition]
print(y) #print [10 20 50]
a[indicesposition] = 99
print(a) #print [ 0 99 99 30 40 99 60 70]
booleantruefalse = np.array([0, 1, 1, 0, 0, 1, 0, 0], dtype=np.bool)
print(booleantruefalse) #print [False  True  True False False  True False False]
printtruetheones = a[booleantruefalse]
print(printtruetheones) #print [99 99 99]  RM:  dimension must be the same and number of elements must be the same
a = np.array([-1, -3, 1, 4, -6, 9, 3])
negativemask = a < 0
print(negativemask) #print [ True  True False False  True False False]
print(a[negativemask]) #print -1 -3 -6]
a[negativemask] = 0
print(a[negativemask]) #print [0 0 1 4 0 9 3]
print(a) #print [0 0 1 4 0 9 3]
a55 = np.array([[0, 1, 2, 3, 4, 5], [10, 11, 12, 13, 14, 15], [20, 21, 22, 23, 24, 25], [30, 31, 32, 33, 34, 35], [40, 41, 42, 43, 44, 45], [50, 51, 52, 53, 54, 55]])
print(a55)
'''
[[ 0  1  2  3  4  5]
 [10 11 12 13 14 15]
 [20 21 22 23 24 25]
 [30 31 32 33 34 35]
 [40 41 42 43 44 45]
 [50 51 52 53 54 55]]
'''
print(a55[[0, 1, 2, 3, 4],[1, 2, 3, 4, 5]]) #print [ 1 12 23 34 45]
print(a55[3:, [0, 2, 5]])
'''
[[30 32 35]
 [40 42 45]
 [50 52 55]]
'''
mask = np.array([1, 0, 1, 0, 0, 1], dtype = np.bool)
print(a55[mask, 2]) #print [ 2 22 52]
#start 01:13:24

print("\n")
#https://projecteuler.net/problem=18 Maximum path sum I
#By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.  That is, 3 + 7 + 4 + 9 = 23.
"""
3
7 4
2 4 6
8 5 9 3
"""
adjacent = np.array([[3, 0, 0, 0], [7, 4, 0, 0], [2, 4, 6, 0], [8, 5, 9, 3]])
print(adjacent)
print(adjacent[:, 0])
print(adjacent[0][0], adjacent[0][1])
print(adjacent[0][0]+adjacent[0][1])
print(adjacent[0][0]+adjacent[1][0]+adjacent[2][0]+adjacent[3][0])
print(adjacent[0][0]+adjacent[1][0]+adjacent[2][0]+adjacent[3][1])
print(adjacent[0][0]+adjacent[1][0]+adjacent[2][1]+adjacent[3][0])
print(adjacent[0][0]+adjacent[1][0]+adjacent[2][1]+adjacent[3][1])
print(adjacent[0][0]+adjacent[1][0]+adjacent[2][1]+adjacent[3][2])
print(adjacent[[0, 1, 2, 3],[0, 0, 0, 0]])
print(adjacent[[0, 1, 2, 3],[0, 0, 0, 1]])
print(adjacent[[0, 1, 2, 3],[0, 0, 1, 0]])
print(adjacent[[0, 1, 2, 3],[0, 0, 1, 1]])
print(adjacent[[0, 1, 2, 3],[0, 0, 1, 2]])
