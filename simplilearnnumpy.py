#www.Simplilearn.com
#Numpy is the core library for scientific and numerical computing in python.  It provides high-performance multidimensional array objects and tools for working with arrays.
#There are modules built on Numpy.
#Input a list in Numpy.  Multi-dimension numpy array contained in paranthesis ([(array1), (array2), ...])
#Numpy array is fast, convenient, and less memory compared to Python list.
#Dimensions are also called axis.
import numpy as np

onedimensionalarray = np.array([1, 2, 3, 4, 5, 6, 7])
twodimensionalarray = np.array([(0, 1, 2, 3), (4, 5, 6, 7)])
print(onedimensionalarray) #print [1 2 3 4 5 6 7]
print(onedimensionalarray.shape) #print (7,)
print(twodimensionalarray) #print [[0 1 2 3]\n [4 5 6 7]]
print(twodimensionalarray.shape) #print (2, 4)
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

