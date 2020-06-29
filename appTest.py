import unittest
from app import Product, CreditCard, User, Chart


class testProducts(unittest.TestCase):

    # TU 1: Todo producto que se encuentre en la base de datos tendrá que tener un nombre y una descripción, es decir que si por ejemplo tenemos en la base de datos un celular de tal marca, este deberá tener una descripción acorde.
    def testNameAndDescription(self):
        result = Product(
            'El principito', 'Libro para niños').validateNameAndDescription()
        self.assertTrue(result)


class testPayment(unittest.TestCase):

    # TU 2: A la hora de ingresar el número de tarjeta, el usuario no puede ingresar valores numéricos negativos en ese campo, si lo hace el sistema no permite realizar la compra.
    def testCreditCardNumberGreaterThan0(self):
        result = CreditCard(10).validateCreditCardGreaterThan0()
        self.assertTrue(result)


class testCreditCardNumber(unittest.TestCase):

    # TU 3: A la hora de ingresar el número de tarjeta, el usuario no puede ingresar letras en ese campo, si lo hace el sistema no permite realizar la compra.
    def testCreditCardNumber(self):
        result = CreditCard(10).validateCreditCardOnlyNumber()
        self.assertTrue(result)


class testUser(unittest.TestCase):

    # TU 4: La longitud mínima de caracteres de una contraseña debe ser mayor o igual a 8
    def testPasswordLength(self):
        result = User('Ignacio', '12345678').validateLengthPasswordUser()
        self.assertTrue(result)

    # TU 5: Si el usuario ingresa algo distinto de números y letras su contraseña no será válida
    def testPasswordCharacters(self):
        result = User('Fulanito', 'superSecret123A').validatePasswordUser()
        self.assertTrue(result)

    # TU 6: La longitud del campo "Usuario" no puede ser nula
    def testUserLength(self):
        result = User('Fulanito', 'superPassword').validateUserLength()
        self.assertTrue(result)


class testProdcuts(unittest.TestCase):

    # TU 7: El descuento debe ser menor que el precio del producto
    def testdiscount(self):
        chart = Chart('12', 'This is the chart of Fulanito')
        chart.setTotal(100)
        chart.setDesc(50)
        result = chart.validateTotalGreaterThanDiscount()
        self.assertTrue(result)

    # TU 8: El stock de un producto no puede ser negativo
    def testUserNoNegativeProductQuantity(self):
        product = Product('Teclado', 'Teclado razer BlackWidow')
        product.setStock(10)
        result = product.validateNoNegativeProductQuantity()
        self.assertTrue(result)
