import pandas as pd
import plotly.figure_factory as ff
import csv
import statistics

df=pd.read_csv("StudentsPerformance.csv")
data=df["reading score"].tolist()
mean=sum(data)/len(data)
print(mean)
std=statistics.stdev(data)
print(std)
median=statistics.median(data)
print(median)
mode=statistics.mode(data)
print(mode)
fig=ff.create_distplot([data],["Result"],show_hist=False)
fig.show()

firststdstart,firsststdend=mean-std,mean+std
secondstdstart,secondstdend=mean-(2*std),mean+(2*std)
thirdstdstart,thirdstdend=mean-(3*std),mean+(3*std)
list1std=[result for result in data if result>firststdstart and result<firsststdend]
list2std=[result for result in data if result>secondstdstart and result<secondstdend]
list3std=[result for result in data if result>thirdstdstart and result<thirdstdend]
print("{}% of data lies with in firststd".format(len(list1std)*100.0/len(data)))
print("{}% of data lies with in secondstd".format(len(list2std)*100.0/len(data)))
print("{}% of data lies with in thirdstd".format(len(list3std)*100.0/len(data)))