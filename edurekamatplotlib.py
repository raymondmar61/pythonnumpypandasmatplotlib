#YouTube edureka
#Data Visualization is a process to communicate information easier in pictures or graphs.  Data Visualization allows people to quickly interprete the data and adjust different variables to see their effect.  Find insights in data.
from matplotlib import pyplot as plt
from matplotlib import style
plt.plot([1, 2, 3], [4, 5, 1])  #line chart([x-axis points], [y-axis points]) (1, 4), (2, 3), (3, 1)
plt.title("Title")
plt.xlabel("x-axis label")
plt.ylabel("y-axis label")
#plt.show()
xaxislist = [5, 8, 10]
yaxislist = [12, 16, 6]
plt.plot(xaxislist, yaxislist)  #line chart([x-axis points], [y-axis points])
plt.title("Title line chart")
plt.xlabel("x-axis label")
plt.ylabel("y-axis label")
#plt.show()

style.use("ggplot")
xaxislist = [5, 8, 10]
yaxislist = [12, 16, 6]
xaxislist2 = [6, 9, 11]
yaxislist2 = [6, 15, 7]
plt.plot(xaxislist, yaxislist,"green",label="line one", linewidth=5) #green is the line color
plt.plot(xaxislist2, yaxislist2,"cyan",label="line two", linewidth=2) #cyan is the line color
plt.title("Title line chart")
plt.xlabel("x-axis label")
plt.ylabel("y-axis label")
plt.legend()
plt.grid(True, color="black")  #grid lines
#plt.show()

xbarlist1 = [1, 3, 5, 7, 9]
ybarlist1 = [5, 2, 7, 8, 2]
xbarlist2 = [2, 4, 6, 8, 10]
ybarlist2 = [8, 6, 2, 5, 6]
plt.bar(xbarlist1, ybarlist1, label="bar one")
plt.bar(xbarlist2, ybarlist2, label="bar two", color="green")
plt.legend()
plt.xlabel("x-axis label")
plt.ylabel("y-axis label")
plt.title("Title bar chart")
#plt.show()

from random import randint
yrandomnumbers = [randint(1,100) for y in range(1,25)]
print(yrandomnumbers)
xbins = [x for x in range(0,110, 5)]
print(xbins)
plt.hist(yrandomnumbers, xbins, histtype="bar", rwidth = 1.0)
plt.xlabel("x-axis label bins 0-4, 5-9, 10-14 . . . 95-99, 100- lower end inclusive")
plt.ylabel("y-axis label")
plt.title("Title histogram")
plt.legend()
#plt.show()

xscatter = [1, 2, 3, 4, 5, 6, 7, 8]
yscatter = [5, 2, 4, 2, 1, 4, 5, 2]
plt.scatter(xscatter, yscatter, label="skitscat", color="black")
plt.xlabel("x-axis label")
plt.ylabel("y-axis label")
plt.title("Title scatter plot")
plt.legend()
#plt.show()

days = [1, 2, 3, 4, 5]
sleeping = [7, 8, 6, 11, 7]
eating = [2, 3, 4, 3, 2]
working = [7, 8, 7, 2, 2]
playing = [8, 5, 7, 8, 13]
#the plt.plot([], [], . . .) must be included to display a legend
plt.plot([], [], color="maroon", label="sleeping", linewidth=5)
plt.plot([], [], color="cyan", label="eating", linewidth=5)
plt.plot([], [], color="red", label="working", linewidth=5)
plt.plot([], [], color="black", label="playing", linewidth=5)
plt.stackplot(days, sleeping, eating, working, playing, colors=["maroon","cyan","red","black"])
plt.xlabel("x-axis label")
plt.ylabel("y-axis label")
plt.title("Title stack plot")
plt.legend()
#plt.show()

numbers = [8, 3, 9, 4]
activities = ["sleeping","eating","working","playing"]
colorslist = ["cyan","brown","red","blue"]
plt.pie(numbers, labels=activities, colors = colorslist, startangle=90, shadow=True, explode=(0, 0.1, 0, 0), autopct="%1.1f%%") #startangle means the first division is a vertical line
plt.title("Title pie chart")
#plt.show()

import numpy as np
def f(t):
	return np.exp(-t)*np.cos(2*np.pi*t)
t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)
plt.subplot(211)  #plot 2 charts, first chart first column, first row. multiple charts
plt.plot(t1, f(t1), "bo", t2, f(t2))
plt.subplot(212) #plot 2 charts, second chart first column, second row. multiple charts
plt.plot(t2, np.cos(2*np.pi*t2))
#plt.show()
#left is number of charts to show, align horizontal number 2 or align vertical 1, numbered chart.

plt.plot((1, 2, 3), (4, 5, 6), "bo", (10, 11, 12), (20, 21, 22))
#plt.show() #plot two sets of lines.  first set of lines is dots.  second set of lines is line.  Both sets of lines are not connected.
plt.plot((1, 2, 3), (4, 5, 6), "bo", (1, 2, 3), (4, 5, 6))
#plt.show() #plot two sets of lines.  first set of lines is dots.  second set of lines is line.  Both sets are connected with dots and lines together.

plt.subplot(221)
plt.plot((1, 2, 3), (4, 5, 6), "bo", (1, 2, 3), (4, 5, 6))
plt.subplot(222)
plt.plot((1, 2, 3), (4, 5, 6), (5, 4, 1), (2, 5, 3))
#plt.show()
#left is number of charts to show, align horizontal number 2 or align vertical 1, numbered chart.