from database.dbconn import Database_connection
from dao.dao import *
class Main:
    def __init__(self):
        self.db = DataBase()
    class place:
        def getplace(self):
            locations = []
            locations = self.db.getLocations()
            return locations

    class category:
        def getcategory(self):
            categories = []
            categories = self.db.getCategories()
            return categories

    class mode:
        def getmode(self): 
            mode = []
            mode = self.db.getModes()
            return mode

    # Facade
    class Facade:
        def __init__(self):
            self.place = Main().place()
            self.category = Main().category()
            self.mode = Main().mode()

        def start_clothes(self):
            clothes_dictionary = {}
            location = []
            category = []
            mode = []

            location = self.place.getplace()
            category = self.category.getcategory()
            mode = self.mode.getmode()
            clothes_dictionary = {'location':location,'category':category,'mode':mode}
            print("Clothes Dictionary",clothes_dictionary)
            return clothes_dictionary

        
