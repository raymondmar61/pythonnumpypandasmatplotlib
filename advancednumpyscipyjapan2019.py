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
print(np.argmin(dist75, axis=1)) #print [0 0 1 1 2 2 2 0 0 0].  Prints row index number for number closest to 0.75 looking at numpy array10x3, not numpy dist75.  dist75 helps find the row index number closest to zero.

#start 43:20 exercise  Find the variance in the expr.npy file.  Sort the values in value to retrieve the 1,500 highest numbers.  Produce a shape of (1500, 375) matrix.
#expr.npy is the file name
#RM:  I don't know argmin and abs.  I don't know np.var and np.argsort.
print(expr.shape) #print (20500, 375)
rowvariance = np.var(expr, axis=1)  #I'm guessing get the variance for each row.  Row is denoted by axis=1.
print(rowvariance) #print [  1.15134606e+02   2.69122020e+02   1.20892527e+09 ...,   2.16789079e+06   4.30965782e+05   1.07554677e+05]
print(rowvariance.shape) #print (20500,)
rowvarianceorder = np.argsort(rowvariance)  #sorts the values from smallest to biggest
print(rowvarianceorder) #print [14473  1800 17851 ..., 14683 10080  7424]
mostvariablerows = rowvarianceorder[-1500:]  #get the biggest 1,500 values using indexing.  Get the 1,500th value from the end to the 1st highest value.  I think it's the 1,500 rows with most variance.
print(mostvariablerows) #print [ 5856 11853 16599 ..., 14683 10080  7424]
mostvariabledata = expr[mostvariablerows]  #RM:  I don't know what the code does.  Retrieve the rows with the top 1,500 variances is my guess.
print(mostvariabledata)
'''
[[  2945  12905   1182 ...,   4518  10620   5880]
 [ 10611   4997  15721 ...,   5554   6963   7443]
 [  1277   1248    112 ...,   1863    377   2835]
 ..., 
 [119691  70684 377874 ..., 127389 225083 183294]
 [  2365  61551 195854 ...,    205 529840 414008]
 [713016  49774 575361 ..., 287205   1051 207329]]
'''
print(mostvariabledata.shape) #print (1500, 375)

#Broadcasting.  Two arrays must have the same dimension size or one of the arrays must be size 1 to normalize every column by its corresponding library size.
a = c
print(a)
'''
[[100 200  50 400]
 [ 50   0   0 100]
 [350 100  50 200]]
'''
a = a+5
print(a)
'''
[[105 205  55 405]
 [ 55   5   5 105]
 [355 105  55 205]]
'''
a = c
b = np.array([1, 2, 3, 4])
print(a.shape) #print (3, 4)
print(b.shape) #print (4, ) which is actually (1, 4)
a = a+b
print(a)
'''
[[101 202  53 404]
 [ 51   2   3 104]
 [351 102  53 204]]
'''
# a = c
# b = np.array([1, 2, 3])
# a = a+b
# print(a)  #print ValueError: operands could not be broadcast together with shapes (3,4) (3,)
a = c
b = np.array([[1], [2], [3]])
print(a.shape) #print (3, 4)
print(b.shape) #print (3, 1)
a = a+b
print(a)
'''
[[101 201  51 401]
 [ 52   2   2 102]
 [353 103  53 203]]
'''
librarysize = np.sum(expr, axis=0)
print(expr.shape) #print (20500, 375)
print(librarysize.shape) #print (375,)
print(librarysize[np.newaxis, :].shape) #print (1, 375)
print(np.all([True, True, False])) #print False
print(np.all(expr/librarysize == expr/librarysize[np.newaxis, :])) #print True
exprlibrary = expr / librarysize
exprlibrary *= 1e6 #multiple by 10^6 to keep the numbers on a readable scale which reads per million reads.
print(exprlibrary)
'''
[[  0.00000000e+00   0.00000000e+00   0.00000000e+00 ...,   0.00000000e+00
    3.01507487e-01   0.00000000e+00]
 [  2.88883496e-01   1.96755990e-02   0.00000000e+00 ...,   4.40579806e-02
    5.02512479e-02   7.38250294e-02]
 [  1.54393784e+03   1.02940766e+03   1.34319315e+03 ...,   1.78298242e+03
    1.76865967e+03   1.69812333e+03]
 ..., 
 [  9.65352349e+00   4.95431582e+01   4.22685116e+01 ...,   4.97855180e+01
    5.98659866e+01   7.26438290e+01]
 [  1.10257201e+01   4.25779961e+01   1.51058877e+01 ...,   2.15223235e+01
    2.18090416e+01   1.25687113e+01]
 [  0.00000000e+00   0.00000000e+00   0.00000000e+00 ...,   2.20289903e-01
    0.00000000e+00   0.00000000e+00]]
'''
genelength = np.load("gene-lens.npy")
print(genelength.shape) #print (20500,)

#Broadcast exprlibrary and genelength together to produce RPKM
rpkm = exprlibrary / genelength[:, np.newaxis]*1e3
print(rpkm)
'''
[[  0.00000000e+00   0.00000000e+00   0.00000000e+00 ...,   0.00000000e+00
    1.74888334e-01   0.00000000e+00]
 [  7.97359911e-02   5.43074771e-03   0.00000000e+00 ...,   1.21606350e-02
    1.38700657e-02   2.03767677e-02]
 [  5.74595401e+02   3.83106685e+02   4.99885803e+02 ...,   6.63558770e+02
    6.58228385e+02   6.31977420e+02]
 ..., 
 [  2.72621392e+00   1.39912901e+01   1.19368855e+01 ...,   1.40597340e+01
    1.69065198e+01   2.05150604e+01]
 [  2.64596115e+00   1.02179016e+01   3.62512303e+00 ...,   5.16494445e+00
    5.23375128e+00   3.01624940e+00]
 [  0.00000000e+00   0.00000000e+00   0.00000000e+00 ...,   1.30118076e-01
    0.00000000e+00   0.00000000e+00]]
'''
#RM:  Stopped at 3D broadcasting 01:13:01 too advanced at the moment and the rest of the video is exercises.