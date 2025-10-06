"""
Daniel Oluwasina
"""
import unittest
from bankaccount import BankAccount


class bankTest(unittest.TestCase):
    def setUp(self):
        self.default = BankAccount("John", 500)
    
    def testBalance(self):
        self.assertEqual(self.default.get_balance(), 500)

    def testDeposit(self):
       self.default.deposit(50)
       self.assertEqual(self.default.get_balance(), 550)

    def testWithdraw(self):
        self.default.withdraw(60)
        self.assertEqual(self.default.get_balance(), 440)
    
    def testWithException(self):
        with self.assertRaises(Exception):
            self.default.withdraw(1000)
            self.default.withdraw(-300)
            
    def testSequence(self):
        self.default.deposit(100)   
        self.default.withdraw(50)   
        self.default.deposit(200)   
        self.default.withdraw(150) 
        self.assertEqual(self.default.get_balance(), 600)

if __name__ == "__main__":
    unittest.main()