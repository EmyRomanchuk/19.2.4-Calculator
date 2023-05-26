import pytest
from app.calculator import Calculator

class TestCalc:
   def setup(self):
       self.calc = Calculator

   def test_adding_success(self):
       assert self.calc.adding(self, 11, 3) == 14         #сложение

   def test_subtraction_success(self):
       assert self.calc.subtraction(self, 10, 8) == 2     #вычитание

   def test_division_success(self):                       #деление
        assert self.calc.division(self, 15, 3) == 5.0

   def test_multiply_success(self):                       #умножение
        assert self.calc.multiply(self, 13, 2) == 26

   def teardown(self):
       print ('Задание выполнено.')
