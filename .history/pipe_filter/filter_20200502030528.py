#!/usr/bin/env python
from dao.dao import *
class Filter(object):
    """
        Base filter class which can take a message and alter the message appropriately.
        You define what happens with the message.
    """

    def __init__(self):
        pass

    def process(self, message):
        pass

class getLocation(Filter):
    def __init__(self):
        self.testList = []
    def process(self,message):
        self.testList.append(message.loc)
        print("in loc",location.testList)

class getCategory(Filter):
    def process(self,message):
        location = getLocation()
        location.testList.append(message.category)
        print("in cat",location.testList)
        

class getMode(Filter):

    def process(self,message):
        location = getLocation()
        location.testList.append(message.mode)
        print("Finalllll",location.testList)
        db = DataBase()
        db.leftoverDetailsToDb(location.testList)
        pass
