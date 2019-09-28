#YouTube Corey Schafer

#Press Q to exit the plot window
from matplotlib import pyplot as plt

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
