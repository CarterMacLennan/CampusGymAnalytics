# import modules
import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LinearRegression
from sklearn import metrics
%matplotlib inline

# Read Dataset
db = pd.read_csv("data.csv") 
db = db[db.number_people != 0]


# Split data into Testing & Training Sets
x = db['temperature'].values.reshape(-1,1)   # input variables
y = db['number_people'].values.reshape(-1,1) # output variables
trainX, testX, trainY, testY = train_test_split(x, y, test_size=0.1, random_state=0)

# Train our data & predict slope
regressor = LinearRegression()
regressor.fit(trainX, trainY)
predY = regressor.predict(testX)
print(regressor.coef_)

# Plot the predicted Data
plt.grid(which='major',linewidth=0.25)
plt.plot(testX, predY, color='lime', linewidth=2)
plt.scatter(testX, testY, color='gray')
plt.xlabel("Temperature (°F)")
plt.ylabel("Number of People")
plt.title("Predict the crowdedness at a given temperature")
plt.gcf().set_size_inches(11,8)
plt.savefig('RainPredictionPlot.png', bbox_inches='tight')
plt.show() 