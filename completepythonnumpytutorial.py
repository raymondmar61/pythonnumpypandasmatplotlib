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
#start 20:00