from app import Login
from database.dbconn import Database_connection
from dao.dao import *
from flask import render_template, redirect, url_for,session
from interceptorPattern.Interceptor_contextObject import *
class EventProcessor(object):
    def __init__(self):
        self.db = DataBase()
    def login(self,username_form,password_form):
        donationsDictionary = {}  
        user_dictionary = {} 
        donationsDictionary = DataBase.retrieveDonations()       #gets list of donations options from the database
        user_dictionary = self.db.getPasswordForLogin(username_form) #gets user details from the db  
        if user_dictionary['password']  == password_form:
            session['username'] = user_dictionary['user_name']
            session['email'] = user_dictionary['user_email']
            session['phonenumber'] = user_dictionary['user_phnumber']
            session['address'] = user_dictionary['user_address']
            print("Session : ",session)
            ci = ConcreteInterceptor()
            dispatcher = Dispatcher()   
            dispatcher.register(ci)
            ConcreteFramework.event(self,user_dictionary['user_name'])
            return render_template("index.html",donationsDictionary = donationsDictionary)     
        else:
            return render_template("login.html")  

    def register(self,userdetails_dictionary):
        self.db.insertUserDataInDB(userdetails_dictionary)
        return render_template("login.html")
        

class UserChoice:   #Acts as a event channel
    def __init__(self): 
        self.eventProcessor = EventProcessor() #Initiated our processor for processing data for the event.
    def optForLogin(self,username_form,password_form):
        return self.eventProcessor.login(username_form,password_form)
    
    def optForRegister(self,userdetails_dictionary):
        return self.eventProcessor.register(userdetails_dictionary)