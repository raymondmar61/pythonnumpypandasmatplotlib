#YouTube Corey Schafer

#Press Q to exit the plot window
from matplotlib import pyplot as plt

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
plt.plot(agesx, devy, color="#444444", linestyle="--", marker=".", label="All Devs devy")
plt.plot(agesx, pydevy, color="b", marker="o", linewidth=3, label="Python pydevy")
plt.plot(agesx, jsdevy, color="yellow", linewidth=3, label="JavaScript jsdevy")
plt.xlabel("Ages plt.xlabel()")
plt.ylabel("Median Salary plt.ylabel()")
plt.title("Median Salary (USD) by Age plt.title()")
plt.legend()
plt.grid(True)
plt.tight_layout()  #improves padding
#plt.legend(["All Devs devy","Python pydevy"])  #RM:  another way to display legend for which y-labels in list are in order of plt.plot()
plt.savefig("savechartplot.png")
plt.show()