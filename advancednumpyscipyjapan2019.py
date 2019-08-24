#Advanced NumPy SciPy Japan 2019 Tutorial Juan Nunuz-Iglesias
#github.com/jni/scipy-japan-2019 Numpy tutorial given at SciPy Japan 2019
#author wrote a book open source http://elegant-scipy.org

import numpy as np
'''
Gene	Cell type A	Cell type B	Cell type C	Cell type D
Gene 0	100	200	50	400
Gene 1	50	0	0	100
Gene 2	350	100	50	200
'''
gene0 = [100, 200, 50, 400]
gene1 = [50, 0, 0, 100]
gene2 = [350, 100, 50, 200]
expressiondata = [gene0, gene1, gene2]
print(expressiondata) #print [[100, 200, 50, 400], [50, 0, 0, 100], [350, 100, 50, 200]]
#The list is not a list of integers.  The list points to integers.
a = np.array(expressiondata)
print(a)
'''
[[100 200  50 400]
 [ 50   0   0 100]
 [350 100  50 200]]
'''
def numpyinfo(a):
	print("Number of elements numpyname.size", a.size)
	print("Number of dimensions numpyname.ndim", a.ndim)
	print("Shape numpyname.shape", a.shape)
	print("Data type numpyname.shape", a.dtype)
	print("Strides numpyname.strides", a.strides)
	print("Flags numpyname.flags:", a.flags)
	print("data memory reference numpyname.data", a.data)
numpyinfo(a)
'''
Number of elements numpyname.size 12
Number of dimensions numpyname.ndim 2
Shape numpyname.shape (3, 4)
Data type numpyname.shape int64
Strides numpyname.strides (32, 8)  #(number of steps to get to next axis in bytes, number of steps to get to the next element in bytes); in 2d array, its (number of steps to get to next row below in bytes, number of steps to get to next element or next element on next column in bytes)
Flags numpyname.flags:   C_CONTIGUOUS : True
  F_CONTIGUOUS : False
  OWNDATA : True
  WRITEABLE : True
  ALIGNED : True
  UPDATEIFCOPY : False
data <memory at 0x7f178dbf7dc8>
'''
#numpyname.ravel() convert numpy array to a singular linear array
print(a.ravel()) #print [100 200  50 400  50   0   0 100 350 100  50 200]
print(a.ravel().shape) #print (12,)
lineara = a.ravel().view(dtype = np.uint8) #8-bit integers
print(lineara)
'''
[100   0   0   0   0   0   0   0 200   0   0   0   0   0   0   0  50   0
   0   0   0   0   0   0 144   1   0   0   0   0   0   0  50   0   0   0
   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
   0   0 100   0   0   0   0   0   0   0  94   1   0   0   0   0   0   0
 100   0   0   0   0   0   0   0  50   0   0   0   0   0   0   0 200   0
   0   0   0   0   0   0]
'''
numpyinfo(lineara)
'''
Number of elements numpyname.size 96  #12 elements * 8 bit integer= 96
Number of dimensions numpyname.ndim 1
Shape numpyname.shape (96,)  #12 elements * 8 bit integer= 96
Data type numpyname.shape uint8
Strides numpyname.strides (1,)  #1 byte to get to next element
Flags numpyname.flags:   C_CONTIGUOUS : True
  F_CONTIGUOUS : True
  OWNDATA : False
  WRITEABLE : True
  ALIGNED : True
  UPDATEIFCOPY : False
data memory reference numpyname.data <memory at 0x7f7fd279cac8>
'''
print(a.T)  #.T is transpose
'''
[[100  50 350]
 [200   0 100]
 [ 50   0  50]
 [400 100 200]]
'''
numpyinfo(a.T)  #.T is transpose
'''
Number of elements numpyname.size 12
Number of dimensions numpyname.ndim 2
Shape numpyname.shape (4, 3)
Data type numpyname.shape int64
Strides numpyname.strides (8, 32)
Flags numpyname.flags:   C_CONTIGUOUS : False
  F_CONTIGUOUS : True
  OWNDATA : False
  WRITEABLE : True
  ALIGNED : True
  UPDATEIFCOPY : False
data memory reference numpyname.data <memory at 0x7f57c241adc8>
'''
#copy a numpy array.  Dependent copy connected.
b = a
print(b)
'''
[[100 200  50 400]
 [ 50   0   0 100]
 [350 100  50 200]]
'''
a[0,0] = 5
print(b)
'''
[[  5 200  50 400]
 [ 50   0   0 100]
 [350 100  50 200]]
'''
print(a[0,0]) #print 5
print(b[0,0]) #print 5
#copy a numpy array.  Independent copy not connected.
a[0,0] = 100
c = a.copy()
print(c)
'''
[[100 200  50 400]
 [ 50   0   0 100]
 [350 100  50 200]]
'''
a[0,0] = 5
print(c)
'''
[[100 200  50 400]
 [ 50   0   0 100]
 [350 100  50 200]]
'''
print(a[0,0]) #print 5
print(c[0,0]) #print 100

expr = np.load("expr.npy")
numpyinfo(expr)
'''
Number of elements numpyname.size 7687500
Number of dimensions numpyname.ndim 2
Shape numpyname.shape (20500, 375)
Data type numpyname.shape uint32
Strides numpyname.strides (4, 82000)
Flags numpyname.flags:   C_CONTIGUOUS : False
  F_CONTIGUOUS : True
  OWNDATA : False
  WRITEABLE : True
  ALIGNED : True
  UPDATEIFCOPY : False
data memory reference numpyname.data <memory at 0x7f6392c83ea0>
'''
print(expr)
'''
[[     0      0      0 ...,      0     18      0]
 [    12      1      0 ...,      2      3      4]
 [ 64134  52319  48016 ...,  80938 105589  92008]
 ..., 
 [   401   2518   1511 ...,   2260   3574   3936]
 [   458   2164    540 ...,    977   1302    681]
 [     0      0      0 ...,     10      0      0]]
'''
total = np.sum(expr)
print(total) #print 19873220752
librarysize = np.sum(expr, axis=0)  #axis=0 add by column
#print(librarysize)
print(librarysize.shape) #print (375,)

#find the number in each row closest to 0.75
#37:32 exercise  #RM:  I don't know argmin and abs.
array10x3 = np.random.random((10,3))
print(array10x3)
'''
[[ 0.93976121  0.00602402  0.2807998 ]
 [ 0.809319    0.3027444   0.67768268]
 [ 0.41455128  0.9904926   0.31548314]
 [ 0.07117051  0.77742754  0.9439281 ]
 [ 0.18795124  0.06579758  0.62259755]
 [ 0.36160333  0.103226    0.8239357 ]
 [ 0.46188334  0.54978602  0.55685275]
 [ 0.5695015   0.26418011  0.49620877]
 [ 0.70216192  0.22176301  0.18156319]
 [ 0.8522842   0.25536452  0.28000926]]
'''
dist75 = np.abs(array10x3 - 0.75)
print(dist75)
'''
[[ 0.18976121  0.74397598  0.4692002 ]
 [ 0.059319    0.4472556   0.07231732]
 [ 0.33544872  0.2404926   0.43451686]
 [ 0.67882949  0.02742754  0.1939281 ]
 [ 0.56204876  0.68420242  0.12740245]
 [ 0.38839667  0.646774    0.0739357 ]
 [ 0.28811666  0.20021398  0.19314725]
 [ 0.1804985   0.48581989  0.25379123]
 [ 0.04783808  0.52823699  0.56843681]
 [ 0.1022842   0.49463548  0.46999074]]
'''
print(np.argmin(dist75, axis=1)) #print [0 0 1 1 2 2 2 0 0 0]

#start 43:20 exercise  #RM:  I don't know argmin and abs.