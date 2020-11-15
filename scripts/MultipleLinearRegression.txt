# Imports
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
%matplotlib inline

# Read dataset
db = pd.read_csv("data.csv") 
db = db[db.number_people != 0]
columns = db[['temperature','month','hour','day_of_week','is_start_of_semester','is_holiday','is_during_semester','is_weekend']]

# Split data into Testing & Training Sets
x = columns.values # input variables
y = db['number_people'].values # output variables
trainX, testX, trainY, testY = train_test_split(x, y, test_size=0.2, random_state=0) 

# Train our data & predict slope
regressor = LinearRegression()
regressor.fit(trainX, trainY)
predY = regressor.predict(testX)

#Ouput Coefficients
for a,b in zip(columns,regressor.coef_):
    print(str(a)+':',b)

# Compare the Predicted vs the Actual Data 
df = pd.DataFrame({'Actual': testY.flatten(), 'Predicted': predY.flatten()})
df[6:18].plot(kind='bar')
plt.title("Actual VS. Predicted Number of People")
plt.ylabel("Number of People")
plt.grid(which='major', linewidth=0.25)
plt.xticks
plt.gcf().set_size_inches(11,8)
plt.savefig('PredictionAlgPlot.png', bbox_inches='tight')
plt.show()