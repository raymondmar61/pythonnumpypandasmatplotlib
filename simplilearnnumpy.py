#www.Simplilearn.com
#Numpy is the core library for scientific and numerical computing in python.  It provides high-performance multidimensional array objects and tools for working with arrays.
#There are modules built on Numpy.
#Input a list in Numpy.  Multi-dimension numpy array contained in paranthesis ([(array1), (array2), ...])
#Numpy array is fast, convenient, and less memory compared to Python list.
#Dimensions are also called axis.
import numpy as np

#Part One
onedimensionalarray = np.array([1, 2, 3, 4, 5, 6, 7])
twodimensionalarray = np.array([(0, 1, 2, 3), (4, 5, 6, 7)])
print(onedimensionalarray) #print [1 2 3 4 5 6 7]
print(onedimensionalarray.shape) #print (7,) #seven horizontal
print(twodimensionalarray) #print [[0 1 2 3]\n [4 5 6 7]]
print(twodimensionalarray.shape) #print (2, 4) #two veritcal, four horizontal
print(onedimensionalarray[1]) #print 2

import sys
b = range(0,1000)
print("Memory size",sys.getsizeof(5)*len(b)) #print Memory size 28000
c = np.arange(0, 1000)
print("Memory size",c.itemsize*c.size) #print Memory size 8000
import time
size = 100000
list1 = range(0, size)
list2 = range(0, size)
startlist1list2 = time.time()
sumlist1list2 = [(x+y) for x, y in zip(list1, list2)]  #Combines list1 and list2 to one list, add each index, return sum in list comprehension sumlist1list2; e.g. if size = 10, then sumlist1list2 is [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print("Python list sumlist1list2 took", (time.time() - startlist1list2)*100000) #print Python list sumlist1list2 took 3026.3185501098633
array1 = np.arange(0, size)
array2 = np.arange(0, size)
startarray1array2 = time.time()
sumarray1array2 = array1 + array2
print(sumarray1array2)  #print [     0      2      4 ..., 199994 199996 199998]
print("Python array sumarray1array2 took", (time.time() - startarray1array2)*100000) #print Python array sumarray1array2 took 66.61415100097656
array3 = np.array([(1, 2), (3, 4), (5, 6)])
print(array3)
'''
[[1 2]
 [3 4]
 [5 6]]
'''
array3 = np.array([[1, 2], [3, 4], [5, 6]])
print(array3)
'''
[[1 2]
 [3 4]
 [5 6]]
'''
print("Dimensions",array3.ndim) #print Dimensions 2
print("Memory Item size",array3.itemsize) #print Memory Item size 8
print("Data type",array3.dtype) #print Data type int64
print("Shape (up down vertical, left right horizontal)",array3.shape) #print Shape (up down vertical, left right horizontal) (3, 2)
array4 = np.array([[1, 2], [3, 4], [5, 6]], dtype=np.float64) #Changed data type to float
print(array4)
'''
[[ 1.  2.]
 [ 3.  4.]
 [ 5.  6.]]
'''
array5 = np.array([[1, 2], [3, 4], [5, 6]], dtype=np.complex) #Changed data type to complex
print(array5)
'''
[[ 1.+0.j  2.+0.j]
 [ 3.+0.j  4.+0.j]
 [ 5.+0.j  6.+0.j]]
'''
zerosarray = np.zeros((3,4))
print(zerosarray)
'''
[[ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]]
'''
print("Dimensions",zerosarray.ndim) #print Dimensions 2
zerosarray = np.zeros((3,4), dtype=np.int)
print(zerosarray)
'''
[[0 0 0 0]
 [0 0 0 0]
 [0 0 0 0]]
'''
print("Data type",zerosarray.dtype) #print Data type int64
onesarray = np.ones((3,4))
print(onesarray)
'''
[[ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]
 [ 1.  1.  1.  1.]]
'''
print(np.arange(0,5)) #print [0 1 2 3 4]
zerotofive = np.arange(0,5)
print(zerotofive) #print [0 1 2 3 4]
zerotofivelist = list(zerotofive)
print(zerotofivelist) #print [0, 1, 2, 3, 4]
print(type(zerotofivelist)) #print <class 'list'>
zerotofivelist = [x for x in range(0,5)]
print(zerotofivelist) #print [0, 1, 2, 3, 4]
print(type(zerotofivelist)) #print <class 'list'>

concatenatestringadd = np.char.add(["hello","hi"],["abc","xyz"])
print(concatenatestringadd) #print ['helloabc' 'hixyz']
concatenatestringmultiply = np.char.multiply("Hello",3)
print(concatenatestringmultiply) #print HelloHelloHello
concatenatestringcenter = np.char.center("Hello",3,fillchar="-") #print total 3 characters Hello in middle surrounded by hyphens
print(concatenatestringcenter) #print Hel
concatenatestringcenter = np.char.center("Hello",20,fillchar="-") #print total 20 characters Hello in middle surrounded by hyphens
print(concatenatestringcenter) #print -------Hello--------
#more np.char. fill, capatalize, title, lowercase, uppercase, split, split lines, strip, join
print(np.char.lower(["HELLO","WORLD"])) #print ['hello' 'world']
print(np.char.lower("HELLO")) #print hello
love = ["HELLO","WORLD","UNIVERSE"]
lovetitle = [(eachlove).title() for eachlove in love]
print(lovetitle) #print ['Hello', 'World', 'Universe']
print(np.char.title(love)) #print ['Hello' 'World' 'Universe']
print(list(np.char.title(love))) #print ['Hello', 'World', 'Universe']
print(np.char.split("are you coming to the party?")) #print ['are', 'you', 'coming', 'to', 'the', 'party?']
print(("are you coming to the party?").split()) #print ['are', 'you', 'coming', 'to', 'the', 'party?']
print(np.char.splitlines("hello\n how are you?")) #print ['hello', ' how are you?']
print(np.char.strip(["nina","admin","anaita", "anona"],"a")) #print ['nin' 'dmin' 'nait' 'non'] removes the first and last "a"
print(np.char.join([":","-","."],["dmy","ymd","period"])) #print ['d:m:y' 'y-m-d' 'p.e.r.i.o.d']
print(np.char.replace("He is a good dancer","is","was")) #print He was a good dancer

#Part Two
array6 = np.arange(9)
print(array6) #print [0 1 2 3 4 5 6 7 8]
array7 = array6.reshape(3,3)
print(array7)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
 '''
print("array7 dimensions",array7.ndim) #print array7 dimensions 2
#RM:  array7 = array6.reshape(4,2) is ValueError: cannot reshape array of size 9 into shape (4,2)
array7 = array7.flatten()
print(array7) #print [0 1 2 3 4 5 6 7 8]
array8 = array7.reshape(3,3)
print(array8)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
array8 = array8.flatten(order="F")  #C is row major, F is column-major, A is default
print(array8) #print [0 3 6 1 4 7 2 5 8]
array9 = np.arange(12).reshape(4,3)  #Four vertical four down, three horizontal three across
print(array9)
'''
[[ 0  1  2]
 [ 3  4  5]
 [ 6  7  8]
 [ 9 10 11]]
'''
array9 = np.transpose(array9)
print(array9)
'''
[[ 0  3  6  9]
 [ 1  4  7 10]
 [ 2  5  8 11]]
'''
print(list(array9)) #print [array([0, 3, 6, 9]), array([ 1,  4,  7, 10]), array([ 2,  5,  8, 11])]
print(list(array6)) #print [0, 1, 2, 3, 4, 5, 6, 7, 8]
array10 = np.arange(1,9).reshape(2,4)
print(array10)
'''
[[1 2 3 4]
 [5 6 7 8]]
'''
array11 = np.arange(8).reshape(2,2,2)
print(array11)
'''
[[[0 1]
  [2 3]]

 [[4 5]
  [6 7]]]
'''
print("array 11 dimensions",array11.ndim) #print array 11 dimensions 3
print(np.rollaxis(array11,2))
'''
[[[0 2]
  [4 6]]

 [[1 3]
  [5 7]]]
'''
print(np.rollaxis(array11,2,1))
'''
[[[0 2]
  [1 3]]

 [[4 6]
  [5 7]]]
'''
print(np.swapaxes(array11,1,2))
'''
[[[0 2]
  [1 3]]

 [[4 6]
  [5 7]]]
'''
print("\n")

arraymath1 = np.arange(9).reshape(3,3)
print(arraymath1)
'''
[[0 1 2]
 [3 4 5]
 [6 7 8]]
'''
arraymath2 = np.array([10, 11, 12])
print(np.add(arraymath1, arraymath2))  #RM:  the shape horizontal must be the same.  arraymath2 = np.array([10, 11]) error message.
'''
[[10 12 14]
 [13 15 17]
 [16 18 20]]
'''
print(np.subtract(arraymath1, arraymath2))  #RM:  the shape horizontal must be the same.  arraymath2 = np.array([10, 11]) error message.
'''
[[-10 -10 -10]
 [ -7  -7  -7]
 [ -4  -4  -4]]
'''
#RM:  np.multiply() and np.divide() exists
print("\n")

slicearray1 = np.arange(20)
print(slicearray1) #print [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
print(slicearray1[5]) #print 5
print(slicearray1[4:]) #print [ 4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19]
print(slicearray1[:4]) #print [0 1 2 3]
print(slicearray1[slice(2, 9, 2)]) #print [2 4 6 8]
print(slicearray1[slice(3, 15, 2)]) #print [ 3  5  7  9 11 13]
print(slicearray1[slice(4, 16, 3)]) #print [ 4  7 10 13]
#start 18:19


