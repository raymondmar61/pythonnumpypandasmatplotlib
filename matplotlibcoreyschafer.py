#YouTube Corey Schafer

#Press Q to exit the plot window
#from matplotlib import pyplot as plt

"""
#Matplotlib Tutorial (Part 1)_ Creating and Customizing Our First Plots [720p]
#A format string consists of marker, line, and color.  fmt = "[color][marker][line]".  Each is optional.  If not provided, then default used; however, if line is given and no marker, then it's a line without markers.  formatstringexample = "k--" is black color dash line.
print(plt.style.available) #print ['seaborn-ticks', 'seaborn-poster', 'seaborn-pastel', 'seaborn-colorblind', 'seaborn-darkgrid', 'seaborn-paper', 'fivethirtyeight', 'ggplot', 'seaborn-notebook', 'seaborn-white', 'seaborn-whitegrid', 'seaborn-deep', 'seaborn-talk', 'grayscale', 'seaborn-dark', 'seaborn-dark-palette', 'seaborn-muted', 'bmh', '_classic_test', 'fast', 'Solarize_Light2', 'dark_background', 'seaborn-bright', 'seaborn', 'classic']
plt.style.use("fivethirtyeight")  #RM:  run the matplotlib style without the attributes.  I kept the attributes as reference.
#plt.xkcd()  #It's a method to run a matplotlib style which mimics webcomics
#Ages values for the median salaries
agesx = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
# Median Developer Salaries by Age
devy = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
#Median Python Developer Salaries by Age
pydevy = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
#Median JavaScript Developer Salaries by Age
jsdevy = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
plt.plot(agesx, devy, color="#444444", linestyle="--", marker=".", label="All Devs devy legend label")
plt.plot(agesx, pydevy, color="b", marker="o", linewidth=3, label="Python pydevy legend label")
plt.plot(agesx, jsdevy, color="yellow", linewidth=3, label="JavaScript jsdevy legend label")
plt.xlabel("Ages plt.xlabel()")
plt.ylabel("Median Salary plt.ylabel()")
plt.title("Median Salary (USD) by Age plt.title()")
plt.legend()
plt.grid(True)
plt.tight_layout()  #improves padding
#plt.legend(["All Devs devy","Python pydevy"])  #RM:  another way to display legend for which y-labels in list are in order of plt.plot()
plt.savefig("savechartplot.png")
plt.show()
"""

"""
#Matplotlib Tutorial (Part 2)_ Bar Charts and Analyzing Data from CSVs [720p]
#Bar and line in one chart use both plt.bar and plt.plot
agesx = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]
devy = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752]
pydevy = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640]
jsdevy = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583]
plt.style.use("fivethirtyeight")
# plt.bar(agesx, devy, color="#444444", label="All Devs devy legend label")
# plt.plot(agesx, pydevy, color="b", marker="o", linewidth=3, label="Python pydevy legend label")
# plt.plot(agesx, jsdevy, color="yellow", linewidth=3, label="JavaScript jsdevy legend label")
# plt.xlabel("Ages plt.xlabel()")
# plt.ylabel("Median Salary plt.ylabel()")
# plt.title("Median Salary (USD) by Age plt.title()")
# plt.legend()
# plt.tight_layout() #improves padding
# plt.show()
#Multiple bars in one chart
import numpy as np
# xindexes = np.arange(len(agesx))
# barwidth = 0.25
# plt.bar(xindexes - barwidth, devy, width=barwidth, color="#444444", label="All Devs devy legend label")
# plt.bar(xindexes, pydevy, width=barwidth, color="b", label="Python pydevy legend label")
# plt.bar(xindexes + barwidth, jsdevy, width=barwidth, color="yellow", label="JavaScript jsdevy legend label")
# plt.xticks(ticks=xindexes, labels=agesx)  #RM:  error message specifically assigning tick marks and labels plt.xticks(ticks=xindexes, labels=agesx).  It now works because I updated matplotlib.
# plt.xlabel("Ages plt.xlabel()")
# plt.ylabel("Median Salary plt.ylabel()")
# plt.title("Median Salary (USD) by Age plt.title()")
# plt.legend()
# plt.tight_layout() #improves padding
# plt.show()
#Import CSV file csv
import csv
from collections import Counter
# with open("data.csv") as csvfile:
# 	csvreader = csv.DictReader(csvfile) #reads csv file as a dictionary
# 	row = next(csvreader)
# 	print(row) #print OrderedDict([('Responder_id', '1'), ('LanguagesWorkedWith', 'HTML/CSS;Java;JavaScript;Python')])
# 	print(row["LanguagesWorkedWith"]) #print HTML/CSS;Java;JavaScript;Python
# 	print(row["LanguagesWorkedWith"].split(";")) #print ['HTML/CSS', 'Java', 'JavaScript', 'Python']	
# 	languagescounter = Counter()
# 	#for loop reads each row in csvreader, splits the language, adds to languagescounter to count
# 	for eachrow in csvreader:
# 		languagescounter.update(eachrow["LanguagesWorkedWith"].split(";"))
# print(languagescounter) #print Counter({'JavaScript': 59218, 'HTML/CSS': 55465, 'SQL': 47544, 'Python': 36442, 'Java': 35916, 'Bash/Shell/PowerShell': 31991, 'C#': 27097, 'PHP': 23030, 'C++': 20524, 'TypeScript': 18523, 'C': 18017, 'Other(s):': 7920, 'Ruby': 7331, 'Go': 7201, 'Assembly': 5833, 'Swift': 5744, 'Kotlin': 5620, 'R': 5048, 'VBA': 4781, 'Objective-C': 4191, 'Scala': 3309, 'Rust': 2794, 'Dart': 1683, 'Elixir': 1260, 'Clojure': 1254, 'WebAssembly': 1015, 'F#': 973, 'Erlang': 777})
# print(languagescounter.most_common(15)) #print [('JavaScript', 59218), ('HTML/CSS', 55465), ('SQL', 47544), ('Python', 36442), ('Java', 35916), ('Bash/Shell/PowerShell', 31991), ('C#', 27097), ('PHP', 23030), ('C++', 20524), ('TypeScript', 18523), ('C', 18017), ('Other(s):', 7920), ('Ruby', 7331), ('Go', 7201), ('Assembly', 5833)]
# languagesx = []
# popularityy = []
# for item in languagescounter.most_common(15):
# 	languagesx.append(item[0])
# 	popularityy.append(item[1])
# print(languagesx) #print ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']
# print(popularityy) #print [59218, 55465, 47544, 36442, 35916, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
# #Instructor says faster using zip function and unpacking values.
# languagesx.reverse() #RM:  doesn't work sorting.  It works now because I updated matplotlib.
# popularityy.reverse() #RM:  doesn't work sorting.  It works now because I updated matplotlib.
# plt.barh(languagesx, popularityy) #horizontal bar chart
# plt.xlabel("Number Of People Who Use plt.xlabel()")
# plt.ylabel("Programming Languaes plt.ylabel()")
# plt.title("Most Popular Languages plt.title()")
# plt.tight_layout()
# plt.show()
#Import CSV file Pandas
import pandas as pd
from matplotlib import pyplot as plt  #RM:  Python pandas must be uploaded first, matplotlib afterwards.
data = pd.read_csv("data.csv")
ids = data["Responder_id"]
languageresponses = data["LanguagesWorkedWith"]
languagescounter = Counter()
for response in languageresponses:
	languagescounter.update(response.split(";"))
print(languagescounter) #print Counter({'JavaScript': 59218, 'HTML/CSS': 55465, 'SQL': 47544, 'Python': 36442, 'Java': 35916, 'Bash/Shell/PowerShell': 31991, 'C#': 27097, 'PHP': 23030, 'C++': 20524, 'TypeScript': 18523, 'C': 18017, 'Other(s):': 7920, 'Ruby': 7331, 'Go': 7201, 'Assembly': 5833, 'Swift': 5744, 'Kotlin': 5620, 'R': 5048, 'VBA': 4781, 'Objective-C': 4191, 'Scala': 3309, 'Rust': 2794, 'Dart': 1683, 'Elixir': 1260, 'Clojure': 1254, 'WebAssembly': 1015, 'F#': 973, 'Erlang': 777})
print(languagescounter.most_common(15)) #print [('JavaScript', 59218), ('HTML/CSS', 55465), ('SQL', 47544), ('Python', 36442), ('Java', 35916), ('Bash/Shell/PowerShell', 31991), ('C#', 27097), ('PHP', 23030), ('C++', 20524), ('TypeScript', 18523), ('C', 18017), ('Other(s):', 7920), ('Ruby', 7331), ('Go', 7201), ('Assembly', 5833)]
languagesx = []
popularityy = []
for item in languagescounter.most_common(15):
	languagesx.append(item[0])
	popularityy.append(item[1])
print(languagesx) #print ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java', 'Bash/Shell/PowerShell', 'C#', 'PHP', 'C++', 'TypeScript', 'C', 'Other(s):', 'Ruby', 'Go', 'Assembly']
print(popularityy) #print [59218, 55465, 47544, 36442, 35916, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
#Instructor says faster using zip function and unpacking values.
languagesx.reverse()
popularityy.reverse()
plt.barh(languagesx, popularityy) #horizontal bar chart
plt.xlabel("Number Of People Who Use plt.xlabel()")
plt.ylabel("Programming Languaes plt.ylabel()")
plt.title("Most Popular Languages plt.title()")
plt.tight_layout()
plt.show()
"""

"""
#Matplotlib Tutorial (Part 3)_ Pie Charts [720p]
plt.style.use("fivethirtyeight")
# slices = [120, 80, 30, 20]
# labels = ["Sixty","Forty", "Extra1","Extra2"]
# colorslices = ["#008fd5","r","yellow","green"]
# slices = [59219, 55466, 47544, 36443, 35917, 31991, 27097, 23030, 20524, 18523, 18017, 7920, 7331, 7201, 5833]
# labels = ["JavaScript", "HTML/CSS", "SQL", "Python", "Java", "Bash/Shell/PowerShell", "C#", "PHP", "C++", "TypeScript", "C", "Other(s):", "Ruby", "Go", "Assembly"]
slicestopfive = [59219, 55466, 47544, 36443, 35917]
labelstopfive = ["JavaScript", "HTML/CSS", "SQL", "Python", "Java"]
colorslices = ["#008fd5","r","yellow","green","b"]
explodemovesliceout = [0, 0, 0, 0.1, 0]
plt.pie(slicestopfive, labels=labelstopfive, colors=colorslices, explode=explodemovesliceout, shadow=True, startangle=90, autopct="%1.1f%%", wedgeprops={"edgecolor":"black"})  #start angle rotates counterclockwise.  autopct includes percentages of the total pie chart.
plt.title("Top Five Programming Languages Count Of People plt.title()")
plt.tight_layout()
plt.show()
"""

"""
#Matplotlib Tutorial (Part 4)_ Stack Plots [720p]
#RM:  Area plot or area chart
plt.style.use("fivethirtyeight")
time = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#player1points = [1, 2, 3, 3, 4, 4, 4, 4, 5]
#player2points = [1, 1, 1, 1, 2, 2, 2, 3, 4]
#player3points = [1, 1, 1, 2, 2, 2, 3, 3, 3]
developer1hours = [8, 6, 5, 5, 4, 2, 1, 1, 0]
developer2hours = [0, 1, 2, 2, 2, 4, 4, 4, 4]
developer3hours = [0, 1, 1, 1, 2, 2, 3, 3, 4]
#labelslist = ["player1points", "player2points", "player3points"]
labelslist = ["developer1hours", "developer2hours", "developer3hours"]
colorslist = ["#6d904f","#fc4f30","008fd5"]
#plt.stackplot(time, player1points, player2points, player3points, colors=colorslist, labels=labelslist)
plt.stackplot(time, developer1hours, developer2hours, developer3hours, colors=colorslist, labels=labelslist)
#plt.legend(loc="lower left")
plt.legend(loc=(0.07, 0.05))  #these are percentages away from left and away from bottom.
#plt.title("My Awesome Stack Plot Points Scored Per Time")
plt.title("My Awesome Stack Plot Hours Worked Per Time")
plt.tight_layout()
plt.show()
"""

"""
#Matplotlib Tutorial (Part 5)_ Filling Area on Line Plots [720p]
import pandas as pd
from matplotlib import pyplot as plt  #RM:  Python pandas must be uploaded first, matplotlib afterwards.
data = pd.read_csv("data05fillbetweens.csv")
ages = data["Age"]
developersalary = data["All_Devs"]
pythonsalary = data["Python"]
javascriptsalary = data["JavaScript"]
plt.plot(ages, developersalary, color="#444444", linestyle="--", label="All Developers Salary")
plt.plot(ages, pythonsalary, label="Python Salary")
overallmedian = 78508  #RM:  Excel calculated overall median 78508.  Instructor edited numbers during tutorial.
#plt.fill_between(ages, pythonsalary, overallmedian, where=(pythonsalary > overallmedian), interpolate=True, alpha=0.25)  #alpha is transparency.  1 is solid or no transparency.  where denotes which qualifying areas to display transparency. interpolate fill more accurately.
#plt.fill_between(ages, pythonsalary, overallmedian, where=(pythonsalary <= overallmedian), interpolate=True, color="red", alpha=0.25)  #alpha is transparency.  1 is solid or no transparency.  where denotes which qualifying areas to display transparency. interpolate fill more accurately.
plt.fill_between(ages, pythonsalary, developersalary, where=(pythonsalary > developersalary), interpolate=True, alpha=0.25, label="Above Average")  #alpha is transparency.  1 is solid or no transparency.  where denotes which qualifying areas to display transparency. interpolate fill more accurately.  These are filling between pythonsalary line and developersalary line
plt.fill_between(ages, pythonsalary, developersalary, where=(pythonsalary <= developersalary), interpolate=True, color="red", alpha=0.25, label="Below Average")  #alpha is transparency.  1 is solid or no transparency.  where denotes which qualifying areas to display transparency. interpolate fill more accurately.  These are filling between pythonsalary line and developersalary line
plt.legend()
plt.title("Median Salary (USD) by Age")
plt.xlabel("Ages")
plt.ylabel("Median Salary (USD)")
plt.tight_layout()
plt.show()
"""

"""
#Matplotlib Tutorial (Part 6)_ Histograms [720p]
#https://stackoverflow.com/questions/26454649/python-round-up-to-the-nearest-ten
#https://stackoverflow.com/questions/3348825/how-to-round-integers-in-python
#Historgrams is lower end inclusive to upper end exclusive
import pandas as pd
from matplotlib import pyplot as plt  #RM:  Python pandas must be uploaded first, matplotlib afterwards.
from math import *
plt.style.use("fivethirtyeight")
ages = [18, 19, 21, 25, 26, 26, 30, 32, 38, 45, 55]
#binslist = [10, 20, 30, 40, 50, 60]
print(floor(min(ages)/10.0)*10) #print 10
print(ceil(max(ages)/10.0)*10) #print 60
lowestbin = floor(min(ages)/10.0)*10
highestbin = ceil(max(ages)/10.0)*10
binslist = [x for x in range(lowestbin, highestbin+1,10)]
print(binslist) #print [10, 20, 30, 40, 50, 60]
plt.hist(ages, bins=binslist, edgecolor="black")
plt.title("Ages Of Respondents")
plt.xlabel("Ages")
plt.ylabel("Total Respondents")
plt.tight_layout()
plt.show()
binslistexcludelowerages = [20, 30, 40, 50, 60]
plt.title("Ages Of Respondents 20 and greater")
plt.hist(ages, bins=binslistexcludelowerages, edgecolor="black")
plt.show()
data = pd.read_csv("data06histograms.csv")
ids = data["Responder_id"]
ages = data["Age"]
bins = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
plt.hist(ages, bins=bins, edgecolor="black", log=True) #print on logarithmeic scale log=True
medianage = 29
plt.axvline(medianage, color="#fc4f30", label="Median Age", linewidth=2)  #axis vertical line
plt.legend()
plt.title("Ages Of Respondents From data06histograms.csv")
plt.xlabel("Ages")
plt.ylabel("Total Respondents")
plt.tight_layout()
plt.show()
"""

"""
#Matplotlib Tutorial (Part 7)_ Scatter Plots [720p]
import pandas as pd
from matplotlib import pyplot as plt  #RM:  Python pandas must be uploaded first, matplotlib afterwards.
plt.style.use("seaborn")
x = [5, 7, 8, 5, 6, 7, 9, 2, 3, 4, 4, 4, 2, 6, 3, 6, 8, 6, 4, 1]
y = [7, 4, 3, 9, 1, 3, 2, 5, 2, 4, 8, 7, 1, 6, 4, 9, 7, 7, 5, 1]
plt.scatter(x, y, s=100, c="green", marker="X", edgecolor="black", linewidth=1, alpha=0.75)  #s is size of dot plots, c is color, edgecolor is the marker's border color, linewidth is the size of the border, alpha is transparency 0 is transparent to 1 is solid
plt.tight_layout()
plt.show()
differentgraycolorforeachplot = [7, 5, 9, 7, 5, 7, 2, 5, 3, 7, 1, 2, 8, 1, 9, 2, 5, 6, 7, 5]
plt.scatter(x, y, s=100, c=differentgraycolorforeachplot, marker="*", edgecolor = "black", linewidth=1, alpha=1)
plt.tight_layout()
plt.show()
dotplotsizes = [209, 486, 381, 255, 191, 351, 185, 228, 174, 538, 239, 394, 399, 153, 273, 293, 436, 501, 397, 539]
plt.scatter(x, y, s=dotplotsizes, c=differentgraycolorforeachplot, cmap="Greens", marker="*", edgecolor = "black", linewidth=1, alpha=1) #cmap or color map plots different green color for each x value plot.  Also, different sizes for each dot plots s = dotplotsizes.
colorbar = plt.colorbar() #colorbar to assist reading how reading the 
colorbar.set_label("Colorbar Title For plt.colorbar()")
plt.tight_layout()
plt.show()
youtubedata = pd.read_csv("2019-05-31-data.csv")
viewcount = youtubedata["view_count"]
likes = youtubedata["likes"]
ratio = youtubedata["ratio"]
plt.scatter(viewcount, likes, c=ratio, cmap="summer")
colorbar = plt.colorbar() #colorbar to assist reading how reading the 
colorbar.set_label("Colorbar Title For plt.colorbar() Like/Dislike Ratio")
plt.xscale("log") #set the x axis and y axis scale to log between 10^6 to 10^9 in this data set
plt.yscale("log") #set the x axis and y axis scale to log between 10^6 to 10^9 in this data set
plt.title("Trending YouTube Videos")
plt.xlabel("View Count")
plt.ylabel("Total Likes")
plt.tight_layout()
plt.show()
"""

"""
#Matplotlib Tutorial (Part 8)_ Plotting Time Series Data [720p]
import pandas as pd
from datetime import datetime, timedelta
from matplotlib import pyplot as plt  #RM:  Python pandas must be uploaded first, matplotlib afterwards.
from matplotlib import dates as mpldates
plt.style.use("seaborn")
#Instructor showed how to format dates
dates = [datetime(2019, 5, 24), datetime(2019, 5, 25), datetime(2019, 5, 26), datetime(2019, 5, 27), datetime(2019, 5, 28), datetime(2019, 5, 29), datetime(2019, 5, 30)]
y = [0, 1, 3, 4, 6, 5, 7]
#plt.plot_date(dates, y) #plot a scatterplot dates is x-axis and y is y-axis
#plt.plot_date(dates, y, linestyle="solid") #plot a line chart dates is x-axis and y is y-axis
#plt.gcf().autofmt_xdate()  #gcf get current figure.  autofmt automatically format to make x-axis look better.
#dateformat = mpldates.DateFormatter("%b %d, %Y") #format date to display month day, year May 24, 2019
#plt.gca().xaxis.set_major_formatter(dateformat) #gca get current axis set the formatting for the X-axis
#plt.show()

bitcointdata = pd.read_csv("data08timeseries.csv")
bitcointdata["Date"] = pd.to_datetime(bitcointdata["Date"]) #RM:  Currently the dates in the file is read as a string.  Convert to date.
bitcointdata.sort_values("Date", inplace=True)
pricedate = bitcointdata["Date"] #case sensitive
priceclose = bitcointdata["Close"] #case sensitive
plt.plot_date(pricedate, priceclose, linestyle="solid") #plot a line chart dates is x-axis and y is y-axis
plt.gcf().autofmt_xdate()  #gcf get current figure.  autofmt automatically format to make x-axis look better.
plt.title("Bitcoin Prices")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.tight_layout()
plt.show()
"""


#Matplotlib Tutorial (Part 9)_ Plotting Live Data in Real-Time [720p]
#RM:  The instructor is simulating a live chart updating every one second.
import random
from itertools import count
import pandas as pd
from matplotlib import pyplot as plt  #RM:  Python pandas must be uploaded first, matplotlib afterwards.
from matplotlib.animation import FuncAnimation
# plt.style.use("fivethirtyeight")
# xvalues = []
# yvalues = []
# index = count()
# print(index) #print count(0)
# next(index)
# print(index) #print count(1)
# next(index)
# def animate(i):
# 	xvalues.append(next(index))  #RM:  I wrote two print(index) and two next(index).  Chart starts at x=2.
# 	yvalues.append(random.randint(0, 5))
# 	plt.cla() #cla instructor thinks clear axis.  It eliminates the different color variation.
# 	plt.plot(xvalues, yvalues)
# variableanimate = FuncAnimation(plt.gcf(), animate, interval=1000) #gcf get current figure.  interval=1000 is one second.
# plt.tight_layout()
# plt.show()
plt.style.use("fivethirtyeight")
#Run data_get.py to generate a simulation of live data saved to data09livedata.csv.  Run the Python code as data_get.py generates data.
index = count()
def animate(i):
	livedata = pd.read_csv("data09livedata.csv")
	x = livedata["x_value"]
	y1 = livedata["total_1"]
	y2 = livedata["total_2"]
	plt.cla() #cla instructor thinks clear axis.  It eliminates the different color variation.
	plt.plot(x, y1, label="Channel 1")
	plt.plot(x, y2, label="Channel 2")
	plt.legend(loc="upper left")
	plt.tight_layout()
variableanimate = FuncAnimation(plt.gcf(), animate, interval=1000) #gcf get current figure.  interval=1000 is one second.
plt.tight_layout()
plt.show()
