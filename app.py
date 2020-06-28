from datetime import date


class Product:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def setStock(self, stock):
        self.stock = stock

    def getStock(self):
        return self.stock

    def setPrice(self, price):
        if price < 0:
            raise ValueError('The price must be greater than 0')
        self.price = price

    def getPrice(self):
        return self.price

    def validateNameAndDescription(self):
        if(len(self.name) and len(self.description)):
            return True
        else:
            return False


class CreditCard:
    def __init__(self, number):
        self.number = number
        self.expiryDate = date.today()

    def getExpiryDate(self):
        return self.expiryDate

    def getNumber(self):
        return self.number

    def validateCreditCardGreaterThan0(self):
        return self.number > 0
