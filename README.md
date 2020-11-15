# CAMPUS GYM ANALYTICS 
A web application developed with python and HTML that allows the user to view how crowded a campus gym will be based on the following variables:
- Temperature
- Month
- Day
- Hour
- Is start of semester 
- Is during semester   
- Is weekend

The outcome is predicted using multiple linear regression derived from a [source on Kaggle](https://www.kaggle.com/nsrose7224/crowdedness-at-the-campus-gym).

The application also allows the user to enter data into a survey and view the results. As well as view aggregated data concerning the crowdedness of that gym derived from the source on Kaggle.

## Table of Contents

  - [Technology Stack](#technology-stack)
  - [Data](#data)
  - [Report](#report)

# Technology Stack

### Environment
* Juniper

### Modules
* os 
* tornado
* pickle
* pandas
* numpy
* matplotlib
* seaborn
* sklearn

# Data

## Number of people for each month of a semester
<div class="row">
  <div class="column">
    <img src="/client/images/AvgSemester.jpg" width="400" height="300"/>
  </div>
  <div class="column">
    <img src="/client/images/MaxSemester.jpg" width="400" height="300"/>
  </div>
</div>  

## Predicting Crowdedness based on Temperature using Linear Regression 

<div class="row">  
  <div class="column">
    <img src="/client/images/RainPrediction.jpg" width="400" height="300"/>
  </div>
  <div class="column">
    <img src="/client/images/Prediction.jpg" width="400" height="300"/>
  </div>
</div>  

## Predicting Crowdedness using Multiple Linear Regression 
The coefficient for each independant variable is used in predict.html to allow the user to view the expected number of people at the gym based off of the inputted variables.
| Variable             | Coefficient |
|----------------------|-------------|
| Temperature          | 0\.79       |
| Month                | \-0\.67     |
| Day                  | 1\.53       |
| Hour                 | \-0\.87     |
| Is start of semester | 7\.3        |
| Is during semester   | 13\.52      |
| Is weekend           | \-5\.3      |

<img src="/client/images/PredictionUI.png"  width="600" height="400"/>

## Survey Results 
A survey was added to the site, allowing the user to enter their preferred temperature and time for going to the gym. After submitting the form, they would be redirected to answer.html to view the results of the survey so far.

<img src="/client/images/SurveyUI.png" width="750" height="300"/> 
 
<div class="row"> 
  <div class="column">
    <img src="/client/images/TempSurvey.jpg" width="400" height="300"/>
  </div>
  <div class="column">
    <img src="/client/images/TimeSurvey.jpg" width="400" height="300"/>
  </div>
</div> 
 
# Report 
 
### Introduction and Background

Out of curiosity, I wanted to be able to predict how the crowded a campus gym would be based on the date, time, and temperature. On the website Kaggle, there is an interesting dataset concerning [the crowdedness of a university gym](https://www.kaggle.com/nsrose7224/crowdedness-at-the-campus-gym). This dataset includes the number of individuals at a campus gym recorded every ten minutes for over a year, along with the associated time stamps. Additionally, the data source includes other aggregated data that proved to have a significant impact on the number of individuals at the gym. Using this dataset and data analytics with Python, I was able to gather meaningful information that may be used at our own university.

### Hypothesis

Before analyzing the data set, I hypothesized that the number of individuals at the gym would spike significantly at the beginning of each semester and would be followed by a steady decline throughout the rest of the semester. I made this hypothesis based on my own experiences as a powerlifter, as well as analytics provided by GoodLife fitness. I’ve found the gym to be substantially busier at the beginning of the semester, as classes have not yet begun providing a lot of assignments. Additionally, [CBC News](https://www.cbc.ca/news/canada/nova-scotia/new-years-resolutions-fitness-industry-1.5406575) reinforced his hypothesis, as their article stated that Goodlife gym memberships are sold the most in January which is also the first month of the winter semester.

I also hypothesized that very cold weather would be an indication that there would be a substantial increase in the number of people. This hypothesis was based on a [research study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3867318/) on weather’s impact on individuals’ everyday activities. It was determined that people are far more likely to spend more time inside indoor facilities on very cold days. Therefore, I concluded that if this is the case, there should be a greater number of people at the gym at the same time on very cold days.

### Analysis and Implication

In order to determine the crowdedness of the gym throughout both semesters, the average number of people at the gym throughout each month were plotted as shown in Figure 1.1. This plot showcases that my hypothesis was correct that the number of people at the gym peak at the beginning of each semester and decays as the semester carries on. Please note that the month of August and September appear very similar because the fall semester starts very late in the month of august. To reinforce these results, the max number of people at the gym at the same time for every month was plotted as shown in Figure 1.2. As expected, the maximum number of people at the gym at the same time, peaks at the beginning of each semester, and decays as the semester carries on.

#### Figure 1.1 & 1.2

<div class="row">
  <div class="column">
    <img src="/client/images/AvgSemester.jpg" width="400" height="300"/>
  </div>
  <div class="column">
    <img src="/client/images/MaxSemester.jpg" width="400" height="300"/>
  </div>
</div> 

In order to determine the relationship temperature has with the crowdedness of a campus gym, the sklearn library was used to perform a linear regression. By using linear regression, the sign and coefficient of temperature in relation to the number of people at the gym was determined to be a positive slope of 1.06. This slope proves that the number of individuals should peak on very hot days which is the exact opposite of my original hypothesis.

In order to view the relationship that all other variables included in the dataset have, I utilized the sklearn library to perform a multiple linear regression. The resulting sign and coefficients shown in Table 1.1 reinforces the positive impact that temperature and the start of the semester have. Additionally, as the week drags on there is an increase in the number of individuals at the gym, however, on weekends there’s a drop in approximately 5 people.

#### Table 1.1

| Variable             | Coefficient |
|----------------------|-------------|
| Temperature          | 0\.79       |
| Month                | \-0\.67     |
| Day                  | 1\.53       |
| Hour                 | \-0\.87     |
| Is start of semester | 7\.3        |
| Is during semester   | 13\.52      |
| Is weekend           | \-5\.3      |

### Conclusion

Using the dataset and data analytics with Python, I was able to successfully gather meaningful information on the crowdedness of a campus gym. As anticipated, the number of individuals at the gym peak at the beginning of the semester, and gradually decay as the semester carries on. This can be seen in both Figure 1.1 and 1.2 as well as in the positive sign of the variable “Is start of semester” in Table 1.1. Furthermore, in contrast to my hypothesis, temperature has a positive relationship with the number of people at a campus gym. This was concluded by the positive slope with a coefficient of 1.06 derived from a linear regression using the sklearn library. Additionally, this positive relationship reappeared in the multiple linear regression, but with a slope of 0.79. Finally, the relationship other factors have on the crowdedness of a campus gym were able to be determined using the multiple linear regression, which proved to be very significant. On the website I developed, I was able to utilize the signs and coefficients derived from the multiple linear regression to predict the crowdedness of a campus gym.

### References
* [the crowdedness of a university gym](https://www.kaggle.com/nsrose7224/crowdedness-at-the-campus-gym)
* [CBC News](https://www.cbc.ca/news/canada/nova-scotia/new-years-resolutions-fitness-industry-1.5406575)
* [research study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3867318/)
