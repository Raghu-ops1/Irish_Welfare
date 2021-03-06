from flask import render_template

class Fooddonation(object):
    def accept(self,visitor):
        #Interface to accept a visitor
        return visitor.visit(self)

    def gets_buy_food():
        return render_template("buyFood.html")
    def gets_donate_food():
        return render_template("donateFood.html")
    def gets_party_leftovers():
        return render_template("partyLeftovers.html")



class Visitor(object):
    pass

class BuyFood(Visitor):
    def visit(self):
        return Fooddonation.buy_food()

class Donate_Food(Visitor):
    def visit(self):
        return Fooddonation.donate_food()

class Party_leftovers(Visitor):
    def visit(self):
        return Fooddonation.party_leftovers()   





