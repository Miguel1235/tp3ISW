import unittest
from app import Product, CreditCard


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
