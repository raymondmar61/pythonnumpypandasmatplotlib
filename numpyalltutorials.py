#YouTube Joeyajames
#NumPy data types:  int8 bit -128 to 127, int16 bit -32768 to 32,767, int32, int64, uint8 unsigned integer 0 to 255, uint16 0 to 65535, uint32, uint64, float16 half precision signed float, float32 single precision signed lfoat, float64 double precision signed float, compex64, complex 128.  Also boolean bool_, string, datetime, and python object.  Default is float64.
import numpy as np

numpyarray = np.array([2,3,4])
print(numpyarray) #print [2 3 4]
numpyrange = np.arange(1,13,2)
print(numpyrange) #print [ 1  3  5  7  9 11].  Print numbers starting at 1 exclusive at 13 increment by 2
numpyrandom = np.random.random(3)  #Random numbers between 0 and 1
print(numpyrandom) #print [0.31309967 0.7921456  0.78090792].  
numpyrandominteger = np.random.randint(0,10,5) #Random integers between 0 and 10 inclusive five elements
print(numpyrandominteger) #print [3 0 4 7 9]
numpylinspace = np.linspace(1,12,6)
print(numpylinspace) #print [ 1.   3.2  5.4  7.6  9.8 12. ].  Print six numbers starting a 1 equal separation at 12 inclusive
numpylinspace = np.linspace(1,12,6, dtype=np.int8)
print(numpylinspace) #print [ 1  3  5  7  9 12].  Print six numbers starting a 1 almost equal separation at 12 inclusive
numpyreshape = numpylinspace.reshape(3,2)
print(numpyreshape) #print [[ 1  3]\n  [ 5  7]\n  [ 9 12]].  Reshape to three dimension two elements each or three rows two elements each.  Three rows, two columns.
numpyarray = np.array([6, 4, -5, 8, 99, 1000000, -53])
print(numpyarray.size) #print 7.  Number of elements
print(numpyarray.shape) #print (7,).  If there's no rows, then first number is columns or number of elements.
print(numpyarray.dtype) #print int64
numpyarray = np.array([(-1, -3), (0, 5), (8, 44)])
print(numpyarray.size) #print 6.  Number of elements
print(numpyarray.shape) #print (3,2).  If there's no rows, then first number is columns or number of elements.  Three rows, two columns.
print(numpyarray.dtype) #print int64
print(numpyarray.itemsize) #print 8 prints memory size in bytes
numpyarray = np.array([6, 4, -5, 8, 99, 1000000, -53])
print(numpyarray > 0) #print [ True  True False  True  True  True False]
numpyarray = numpyarray + 70
print(numpyarray) #print [     76      74      65      78     169 1000070      17].  Add 70 to all numbers.
numpyzeroes = np.zeros((5))
print(numpyzeroes) #print [0. 0. 0. 0. 0.]
numpyzeroes = np.zeros((5), dtype=np.int64)
print(numpyzeroes) #print [0 0 0 0 0]
numpyzeroes = np.zeros((2,3), dtype=np.int64)
print(numpyzeroes) #print [[0 0 0]\n [0 0 0]]
numpyones = np.ones((10))
print(numpyones) #print [1. 1. 1. 1. 1. 1. 1. 1. 1. 1.]
numpyones = np.ones((4,2), dtype=np.int16)
print(numpyones) #print [[1 1]\n  [1 1]\n  [1 1]\n  [1 1]]
numpyk = np.random.random((2,3))
print(numpyk) #print [[0.73414294 0.31502813 0.24473664]\n [0.97007539 0.79083236 0.45979176]]
np.set_printoptions(precision = 2, suppress=True) #print future NumPy two decimal places and no scientific notation.
print(numpyk) #print [[0.73 0.32 0.24]\n [0.97 0.79 0.46]]
np.set_printoptions(edgeitems=3,infstr='inf', linewidth=75, nanstr="nan", precision=8, suppress=False, threshold=1000, formatter=None) #Default options, reset printoptions https://docs.scipy.org/doc/numpy/reference/generated/numpy.set_printoptions.html
print(numpyk) #print [[0.73414294 0.31502813 0.24473664]\n [0.97007539 0.79083236 0.45979176]]
numpyl = np.array([7,1,4,4,1])
print(type(numpyl)) #print <class 'numpy.ndarray'>
print(numpyl.sum()) #print 17
print(numpyl.min()) #print 1
print(numpyl.max()) #print 7
print(numpyl.mean()) #print 3.4.  There is no .average()
print(numpyl.var()) #print 5.039999999999999.  Variance is population.
print(numpyl.std()) #print 2.24499443206.  Standard deviation is population.
numpym = np.array([[3,8],[4,5],[3,8]])
print(numpym) #print [[3 8]\n [4 5]\n [3 8]]
print(numpym.sum(axis=0)) #print [10 21].  Adds each vertical column.
print(numpym.sum(axis=1)) #print [11  9 11].  Adds each horizontal rows.
numpyn = np.arange(1,11,1)
print(numpyn) #print [ 1  2  3  4  5  6  7  8  9 10]
numpyshuffle = np.random.shuffle(numpyn)
print(numpyshuffle) #print None
numpychoice = np.random.choice(numpyn)  #Randomly chooses one item.
print(numpychoice) #print 2
numpyl = np.array([7,1,4,4,1])
listnumpyl = list(numpyl) #convert numpy to list
print(listnumpyl) #print [7, 1, 4, 4, 1]
#upload file, import text file, import csv file
data = np.loadtxt("data.txt", dtype=np.uint8, delimiter=",", skiprows=1)  #skip the first row because the first row is the header.  Assigned data type dtype=np.uint8 to reduce file size.
print(data) #print [[9 3 8 7 6 1 0 4 2 5]\n [1 7 4 9 2 6 8 3 5 0]\n [4 8 3 9 5 7 2 6 0 1]\n [1 7 4 2 5 9 6 8 0 3]\n [0 7 5 2 8 6 3 4 1 9]\n [5 9 1 4 7 0 3 6 8 2]]







