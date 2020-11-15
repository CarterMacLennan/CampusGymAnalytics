# imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read & sort dataset
db = pd.read_csv("data.csv")
db  = db.sort_values(by=["month"],ascending=True)
db = db[db.number_people != 0]

# temp variables
indexW=0
countW=0
avgW = [0] * 5
indexF=0
countF=0
avgF = [0] * 5

# get avg of ppl per month
for month,ppl,durSem,isHoliday in zip(db.month,db.number_people,db.is_during_semester,db.is_holiday):
    if (1 <= month <= 5 and durSem==1 and isHoliday !=1): # Winter Semester
        if month == indexW+1:
            avgW[indexW] += ppl
            countW+=1
        else:
            avgW[indexW] = avgW[indexW]/countW
            indexW+=1
            countW=0
    elif(8 <= month <= 12 and durSem==1 and isHoliday !=1): # Fall Semester
        if month == indexF+8:
            avgF[indexF] += ppl
            countF+=1
        elif(countF!=0):
            avgF[indexF] = avgF[indexF]/countF
            indexF+=1
            countF=0
            
# Calculate last month of semester
avgW[indexW] = avgW[indexW]/countW
avgF[indexF] = avgF[indexF]/countF

# Plot Graphs
monthsW = ["Jan","Feb","Mar","Apr","May"] # Winter Semester
plt.bar(monthsW,avgW,label = "Winter")

monthsF = ["Aug","Sep","Oct","Nov","Dec"] # Fall Semester
plt.bar(monthsF,avgF,label = "Fall")

plt.xlabel("Month") 
plt.ylabel("Average Number of People")
plt.title("Average for the Winter and Fall Semester")
plt.tight_layout()
plt.legend(loc ="upper right")
plt.gcf().set_size_inches(11,8)
plt.savefig('AvgSemester.png', bbox_inches='tight')
plt.show()