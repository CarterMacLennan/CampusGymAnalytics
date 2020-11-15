# imports
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Read & sort dataset
db = pd.read_csv("data.csv")
db  = db.sort_values(by=["month"],ascending=True)
db = db[db.number_people != 0]

# temp variables
maxNumW = [0] * 5
maxNumF = [0] * 5

# get max number of ppl per month
for month,ppl in zip(db.month,db.number_people):
    if 0 < month < 6 and maxNumW[month-1] < ppl:
        maxNumW[month-1] = ppl
    elif 7 < month < 13 and maxNumF[month-8] < ppl:
        maxNumF[month-8] = ppl
        
# Plot dataset
months = ["Jan","Feb","March","April","May"]
plt.bar(months,maxNumW,label = "Winter")

months = ["Aug","Sep","Oct","Nov","Dec"]
plt.bar(months,maxNumF,label = "Fall")

plt.xlabel("Month")
plt.ylabel("Number of People")
plt.title("Max number for Winter and Fall Semester")
plt.tight_layout()
plt.legend(loc ="upper right")
plt.gcf().set_size_inches(11,8)
plt.savefig('MaxSemester.jpg', bbox_inches='tight')
plt.show() 