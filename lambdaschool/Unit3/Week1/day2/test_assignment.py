import unittest
from assignment import Employee

class TestEmployee(unittest.TestCase):
    def test_email(self):
        emp1 = Employee('Josh', 'Fowlkes', 100000)
        emp2 = Employee('Escanor', 'Meliodas', 123456789)

        self.assertEqual(emp1.email, 'Josh.Fowlkes@yahooooooooligans.com')
        self.assertEqual(emp2.email, 'Escanor.Meliodas@yahooooooooligans.com')

if __name__ == '__main__':
    unittest.main()
