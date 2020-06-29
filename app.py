from datetime import date
import re


class User:
    def __init__(self, nameUser, passwordUser):
        self.nameUser = nameUser
        self.passwordUser = passwordUser

    def __len__(self):
        return len(self.passwordUser)

    def setNameUser(self, nameUser):
        self.nameUser = nameUser

    def getNameUser(self):
        return self.nameUser

    def setPasswordUser(self, passwordUser):
        self.passwordUser = passwordUser

    def getPasswordUser(self):
        return self.passwordUser

    def validateLengthPasswordUser(self):
        if (len(self.passwordUser) >= 8):
            return True
        else:
            return False

    def validatePasswordUser(self):
        if re.match("^[A-Za-z0-9]*$", self.passwordUser):
            return True
        else:
            return False

    def validateUserLength(self):
        if (len(self.nameUser) == 0):
            return False
        else:
            return True
    
    def validateNameUserLength(self):
        if (len(self.nameUser) > 20):
            return False
        else:
            return True

class Chart:
    def __init__(self, chartId, description):
        self.chartId = chartId
        self.description = description
        self.discount = 0

    def setTotal(self, total):
        if total < 0:
            raise ValueError('The total must be greater than 0')
        self.total = total

    def getTotal(self):
        return self.total

    def getDesc(self):
        return self.discount

    def setDesc(self, discount):
        if discount < 0:
            raise ValueError('The discount must be greater than 0')
        self.discount = discount

    def validateDescription(self):
        if(len(self.description)):
            return True
        else:
            return False

    def validateTotalGreaterThanDiscount(self):
        return self.total > self.discount


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

    def validateNoNegativeProductQuantity(self):
        if(self.stock < 0):
            return False
        else:
            return True
    
    def validateNoNegativePrice(self):
        if(self.price < 0):
            return False
        else:
            return True


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

    def validateCreditCardOnlyNumber(self):
        return isinstance(self.number, int)
