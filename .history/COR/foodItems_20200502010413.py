from flask import render_template
from clothes_donation.clothes_donation import *
class Fooddon(object):
    def __init__(self, nxt): 
         self._nxt = nxt 
    def handle(self, request): 
        print("Request in handle",request)
        handled = self.processRequest(request) 
        if not handled: 
            return self._nxt.handle(request) 
        else:
            return handled
    def processRequest(self, request):   
        pass

class Grains(Fooddon):
    def processRequest(self, request):
        if request=="Grains":
            db = DataBase()
            dropdown_dictionary = {}
            grainsList = []
            grainsList = db.getGrains(request)
            facade = Facade()
            dropdown_dictionary = facade.getDropdownDetails()
            print("Inside factory",dropdown_dictionary)
            return render_template('grains.html',dropdown_dictionary = dropdown_dictionary,grainsList = grainsList)

class Products(Fooddon):
    def processRequest(self, request):
        if request=="Products":
            request='Product'
            print(f'Enter the type of {request} of product you want to select :')
            products=["Cheese","BreadPack","Pasta","Sphagetti"]
            print(f'Enter the number of {products[1]} packets :')
            return True

class Fruit_Items(Fooddon):
    def processRequest(self, request):
        if request=="Fruits":
            request='Fruit'
            print(f'Enter the type of {request} packet you want to select :')    
            items=["Apple Packets","Banana Packets"]       
            print(f'Enter the number of {items[1]} packets :')
            return True

class User: 
   
    def __init__(self): 
        initial = None  
        self.handler = Grains(Products(Fruit_Items((initial))))
    def agent(self, user_request):   
        for request in user_request: 
            print("Request in agent",request)
            return self.handler.handle(request) 
  




    



