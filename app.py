from datetime import date

class User:
    def __init__(self,nameUser,passwordUser):
        self.nameUser = nameUser
        self.passwordUser = passwordUser
    
    def setNameUser(self, nameUser):
        self.nameUser = nameUser
    
    def getNameUser(self):
        return self.nameUser

    def setPasswordUser(self, passwordUser):
        self.passwordUser = passwordUser
    
    def getPasswordUser(self):
        return self.passwordUser
    
    def validateLenghtPasswordUser(self.passwordUser):
        if (len(self.passwordUser) >= 8):
            return True
        else:
            return False

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

    def validateCreditCardOnlyNumber(self.number):
        if type(self.number) == int:
            return True
        else:
            return False
