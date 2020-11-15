import os
import tornado.ioloop
import tornado.web
from  tornado import web
import pickle
import matplotlib.pyplot as plt
import numpy as np


def surveyPlot(survey):
    numTemp = [0]*2
    for i in survey.answersTemp:   
        if i=='cold':
            numTemp[0]+=1
        elif i=='hot':
            numTemp[1]+=1
        
    # plot tempPref
    plt.bar(['Cold','Hot'],numTemp)
    plt.xlabel("Temperature") 
    plt.ylabel("Number of times selected")
    plt.title("Preferred temperature for going to the gym")
    plt.gcf().set_size_inches(11,8)
    plt.savefig('TempSurvey.jpg', bbox_inches='tight')        
    plt.close() 
        
    numTime = [0]*24

    for ans in survey.answersHour:
        numTime[int(ans)]+=1
        
    # plot timePref
    timePref = [i for i in range(24)]
    plt.bar(timePref,numTime)
    plt.xlabel("Time of Day") 
    plt.ylabel("Number of times selected")
    plt.title("Preferred time of going to the gym")
    plt.gcf().set_size_inches(11,8)
    plt.savefig('TimeSurvey.jpg', bbox_inches='tight')
    plt.close() 

class Survey:
    def __init__(self):
        self.answersTemp = []
        self.answersHour = []
    def new_entry(self):
        num = len(self.answersTemp)
        self.answersTemp.append({})
        self.answersHour.append({})
        return num
    def save_answer(self,id,tempPref,hour):
        self.answersTemp[id]= tempPref
        self.answersHour[id]= hour

class Answer(tornado.web.RequestHandler):
    def post(self):
        # Load the Survey File
        file = open('mySurvey.bin','rb')
        survey = pickle.load(file)
        num = survey.new_entry()
        
        # Get User input
        tempPref = self.get_body_argument('tempPref')
        hour = self.get_body_argument('hour')
        
        # Save input to Survey File
        survey.save_answer(num,tempPref,hour)
        file = open('mySurvey.bin','wb')
        pickle.dump(survey,file)
        file.close()
        
        surveyPlot(survey)
        
        self.render('answer.html')

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("home.html")

application = tornado.web.Application([
    (r"/3585688/", MainHandler),(r"/3585688/answer",Answer),
    (r"/3585688/(.*)", web.StaticFileHandler,{"path":"/home/cs2704/test/"}),
])

if __name__== '__main__':
    application.listen(5229)
    tornado.ioloop.IOLoop.instance().start()