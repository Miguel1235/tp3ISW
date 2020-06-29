import unittest
from app import Product, CreditCard, User


# TU 1: Todo producto que se encuentre en la base de datos tendrá que tener un nombre y una descripción, es decir que si por ejemplo tenemos en la base de datos un celular de tal marca, este deberá tener una descripción acorde.


class testProducts(unittest.TestCase):
    def testNameAndDescription(self):
        result = Product(
            'El principito', 'Libro para niños').validateNameAndDescription()
        self.assertTrue(result)

# TU 2: A la hora de ingresar el número de tarjeta, el usuario no puede ingresar valores numéricos negativos en ese campo, si lo hace el sistema no permite realizar la compra.


class testPayment(unittest.TestCase):
    def testCreditCardNumberGreaterThan0(self):
        result = CreditCard(10).validateCreditCardGreaterThan0()
        self.assertTrue(result)

# TU 3: A la hora de ingresar el número de tarjeta, el usuario no puede ingresar letras en ese campo, si lo hace el sistema no permite realizar la compra.

class testCreditCardNumber(unittest.TestCase):
    def testCreditCardNumber(self):
        result = CreditCard(10).validateCreditCardOnlyNumber()
        self.assertTrue(result)

# TU 4: La longitud mínima de caracteres de una contraseña debe ser mayor o igual a 8, caso contrario el sistema no permite crear el usuario en el sistema.

class testPasswordLenght(unittest.TestCase):
    def testPasswordLenght(self):
        result = User("Ignacio","12345678").validateLenghtPasswordUser()
        self.assertTrue(result)

#  #TU 5: Si el usuario no ingresa números y letras en su contraseña no será una contraseña válida
class testPasswordUser(unittest.TestCase):
     def testPasswordUser(self):
         result = User('12345678').validatePasswordUser()
         self.assertTrue(result)
        


        
# # TU 6: La longitud del campo "Usuario" no puede ser nula, si es asi, el sistema deniega el acceso
# class testPasswordCharacters(unittest.TestCase):
#     def testUserLenght(self):
#         result = User("user1test").validateUserLength()
#         self.assertTrue(result)
    
    
# # TU 7: La cantidad de producto que se desee comprar no puede ser inferior a cero
# class testNoNegativeProductQuantity(unittest.TestCase):
#     def testUserLenght(self):
#         result = Product("4").validateNoNegatyProductQuantity()
#         self.assertTrue(result)
    
#TU 8 :Al aplicar un descuento al carrito, el precio del mismo no resultará nunca en negativo.
 class testdiscount(unittest.TestCase):
     def testdiscount(self):
         result = Carro('12','')
         Carro.setTotal(100)
         Carro.setDesc(50)
         Carro.validateTotalGreaterThanDesc()
         self.assertTrue(result)
