# Write a Pandas program to add, subtract, multiple and divide two Pandas Series.

import pandas as pd
sample_series = [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]

ds1 = pd.Series(sample_series[0])
ds2 = pd.Series(sample_series[1])

class Calculation():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def addition(self):
        addition = self.a + self.b
        return addition

    def substraction(self):
        substraction = self.a - self.b
        return substraction

    def multiplication(self):
        multiplication = self.a * self.b
        return multiplication

    def division(self):
        division = self.a / self.b
        return division

calculator = Calculation(ds1, ds2)

print(calculator.addition())
print(calculator.substraction())
print(calculator.multiplication())
print(calculator.division())