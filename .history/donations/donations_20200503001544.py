from abc import ABCMeta, abstractstaticmethod
import sys
from flask import render_template
from clothes_donation.clothes_donation import *
from database.dbconn import Database_connection
from dao.dao import *

class IDonation(metaclass=ABCMeta):
    @abstractstaticmethod
    def get_donation():
        pass
        #Donation Interface

class MoneyDonation(IDonation):
    def get_donation(self):
        return render_template('money_donation.html')

class FoodDonation(IDonation):
    def __init__(self):
        self.db = DataBase()

    def get_donation(self):
        dictionary = {}
        dictionary = self.db.getFoodDonationType()
        return render_template('food_donation.html',dictionary = dictionary)

class ClothesDonation(IDonation):
    def get_donation(self):
        dropdown_dictionary = {}
        facade = Facade()
        dropdown_dictionary = facade.getDropdownDetails()
        print("Inside factory",dropdown_dictionary)
        return render_template('clothes_donation.html',dropdown_dictionary = dropdown_dictionary)

class Donations:
    def get_donation_type(self,donationType):
        print("Donation",donationType)
        #donation_dictionary = {"donation_type":donationType}
        return eval(donationType) 
  

