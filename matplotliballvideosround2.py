#Sentdex Matplotlib Tutorial Round Two
#matplotlib.org website information
#Home returns chart to original view
#Back to view past view
#Forward to view forward view
#The crosshair drag the graph holding left mouse button.  Zoom holding right mouse button depending on zoom direction with mouse.
#The magnifying glass draw a rectangle left mouse button to zoom in and right mouse button to zoom out.
#Configure Subplot button adjust chart parameters.
#Save pic

import matplotlib.pyplot as plt
#plot.plot([x-values], [y-values])
#plt.plot([1, 2, 3], [5, 7, 4])

"""
#Two Line Chart
x = [1,2,3]
y = [5,7,4]
x2 = [1,2,3]
y2 = [10,14,12]
plt.plot(x,y, label="First Line")  #label="" is required for plt.legend()
plt.plot(x2,y2, label="Second Line")  #label="" is required for plt.legend()
plt.xlabel("x-axis label plt.xlabel()")
plt.ylabel("y-axis label plt.ylabel()")
plt.title("Chart Title plt.title()\nSubtitle")
plt.legend()
plt.show()
"""

"""
#Bar Chart
x = [2,4,6,8,10]
y = [6,7,8,2,4]
x2 = [1,3,5,7,9]
y2 = [7,8,2,4,2]
plt.bar(x,y, label="Bar Chart 1", color="blue")
plt.bar(x2,y2, label="Bar Chart 2", color="k")  #k is black, c is cyan, b is blue
plt.xlabel("x-axis label plt.xlabel()")
plt.ylabel("y-axis label plt.ylabel()")
plt.title("Bar Chart")
plt.legend()
plt.show()
"""

"""
#Histogram
populationageyaxis = [22,55,62,45,21,22,34,42,42,4,99,102,110,120,121,122,130,111,115,112,80,75,65,54,44,43,42,48]
binsxaxis = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130]  #bins are inclusive-exclusive 0-9, 10-19, 20-29, . . . , 120-129, 130-
plt.hist(populationageyaxis, binsxaxis, histtype="bar", rwidth=0.8)
plt.xlabel("x-axis label plt.xlabel()")
plt.ylabel("y-axis label plt.ylabel()")
plt.title("Histogram Chart")
plt.legend()
plt.show()
"""

"""
#Scatter Plot
x = [1,2,3,4,5,6,7,8]
y = [5,2,4,2,1,4,5,2]
plt.scatter(x,y, label="Label For plt.legend()", color="#FF0000", marker="*", s=100) #marker is the scatter plot icon and s is size
plt.xlabel("x-axis label plt.xlabel()")
plt.ylabel("y-axis label plt.ylabel()")
plt.title("Scatter Plot")
plt.legend()
plt.show()
"""

"""
#Stack Plot
daysxaxis = [1,2,3,4,5]
sleeping = [7,8,6,11,7]
eating = [2,3,4,3,2]
working = [7,8,7,2,2]
playing = [8,5,7,8,13]
plt.plot([],[],color="magenta", label="Sleeping", linewidth=5) #label plt.legend() plot a blank line for sleeping
plt.plot([],[],color="c", label="Eating", linewidth=5) #label plt.legend() plot a blank line for eating
plt.plot([],[],color="#FF0000", label="Working", linewidth=5) #label plt.legend() plot a blank line for working
plt.plot([],[],color="#000000", label="Playing", linewidth=5) #label plt.legend() plot a blank line for playing
plt.stackplot(daysxaxis, sleeping, eating, working, playing, colors=["magenta","c","#FF0000","#000000"])
plt.xlabel("x-axis label plt.xlabel()")
plt.ylabel("y-axis label plt.ylabel()")
plt.title("Stack Plot")
plt.legend()
plt.show()
"""

"""
#Pie Chart
slicesnumbers = [7, 2, 2, 13]
activitieslabels = ["sleeping","eating","working","playing"]
colorslist = ["magenta","c","#FF0000","#000000"]
plt.pie(slicesnumbers, labels=activitieslabels, colors=colorslist, startangle=180, shadow=True, explode=(0,0.1,0,0.5), autopct="%1.1f%%") #startangle is the starting angle moving counterclockwise; 0 is flat line direction is right.  explode is which slice is pulled out number is distance pulled out from center starting from sleeping or explode=(sleeping, eating, working, playing) pulling out eating and playing.  autopct is the autopercent and its percentage display formatting.
plt.xlabel("x-axis label plt.xlabel()")
plt.ylabel("y-axis label plt.ylabel()")
plt.title("Pie Chart")
plt.legend()
plt.show()
"""

"""
#Load data from a file with open and import csv
import csv
x = []
y = []
with open("example.txt","r") as csvfile:  #instructor says .csv is okay
	plots = csv.reader(csvfile, delimiter=",")
	for row in plots:
		print(row) #print ['1', '5'] . . . ['13', '7']
		x.append(int(row[0]))
		y.append(int(row[1]))
print(x) #print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(y) #print [5, 3, 4, 7, 4, 3, 5, 7, 4, 4, 5, 11, 7]
plt.plot(x,y, label="Loaded from example.txt")
plt.xlabel("x-axis label plt.xlabel()")
plt.ylabel("y-axis label plt.ylabel()")
plt.title("")
plt.legend()
plt.show()
"""
"""
#Load data from a file numpy
import numpy as np
x, y = np.loadtxt("example.txt", delimiter=",", unpack=True, dtype=np.int64)  #instructor says .csv is okay
print(x) #print [ 1  2  3  4  5  6  7  8  9 10 11 12 13]
print(y) #print [ 5  3  4  7  4  3  5  7  4  4  5 11  7]
plt.plot(x, y, label="Numpy easier to upload file")
plt.xlabel("x-axis label plt.xlabel()")
plt.ylabel("y-axis label plt.ylabel()")
plt.title("")
plt.legend()
plt.show()
"""

"""
#Download data from the internet
import numpy as np
import urllib
import matplotlib.dates as mdates
def bytespdate2num(formatdate,encoding="utf-8"):
	strconverter=mdates.strpdate2num(formatdate)
	def bytesconverter(bbytes):
		sstring = bbytes.decode(encoding)
		return strconverter(sstring)
	return bytesconverter
def graph_data(stock):
	stockpriceurl="https://www.quandl.com/api/v1/datasets/WIKI/"+stock+".csv?column=4&sort_order=asc&collapse=quarterly&trim_start=2017-01-01&trim_end=2018-01-01"
	sourcecode=urllib.request.urlopen(stockpriceurl).read().decode()
	print(sourcecode)
	splitsource=sourcecode.split("\n")
	del(splitsource[0]) #delete Date,Close the first list item
	del(splitsource[-1]) #delete null the last list item
	print(splitsource)
	dateclose, closeprice = np.loadtxt(splitsource,delimiter=",",unpack=True,converters={0: bytespdate2num("%Y-%m-%d")})
	print(dateclose)
	print(closeprice)
	plt.plot_date(dateclose,closeprice, label="default dots")
	plt.xlabel("xlabel")
	plt.ylabel("ylabel")
	plt.title("title\ntitlenewline")
	plt.legend()
	plt.show() #show graph default dots
	plt.plot_date(dateclose,closeprice, "-", label="line chart denoated by hyphen")
	plt.xlabel("xlabel")
	plt.ylabel("ylabel")
	plt.title("title\ntitlenewline")
	plt.legend()
	plt.show() #show graph line chart denoated by hyphen"	
graph_data("AAPL")
"""