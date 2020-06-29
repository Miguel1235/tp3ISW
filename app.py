from datetime import date

class User:
    def __init__(self,nameUser,passwordUser):
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
    
    def validateLenghtPasswordUser(password):
        if (len(password) >= 8):
            return True
        else:
            return False
        
    def validateCharacterPasswordUser(passwordUser):
        for character in passwordUser:
            if character.isdigit():
                return True
            else:
                return False
            
    def  validateUserLength (nameUser):
        if (len(nameUser)==0):
            return False
        else:
            return True
        
class Carro:
    def __init__(self, carroid, description):
        self.carroid = carroid
        self.description = description

    def setTotal(self, total):
        if total < 0:
            raise ValueError('The total must be greater than 0')
        self.total = total
        self.total = total

    def getTotal(self):
        return self.Total
    def getDesc(self):
        return self.desc

    def setDesc(self, Desc):
        if desc < 0:
            raise ValueError('The desc must be greater than 0')
        self.desc = Desc

    def getPrice(self):
        return self.price

    def validateDescription(self):
        if(len(self.description)):
            return True
        else:
            return False

    def validateTotalGreaterThanDesc(self):
        return self.total > self.desc
    
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
        
    def validateNoNegatyProductQuantity(number):
        if(number < 0):
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

