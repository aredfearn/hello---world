Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=========== RESTART: C:\Program Files\Python 3.12\breezypythongui.py ===========
>>> TAX_RATE = 0.20
>>> STANDARD_DEDUCTION = 10000.0
>>> DEPENDENT_DEDUCTION = 3000.0
>>> grossIncome = float(input("Gross income: "))
Gross income: 67000
>>> numDependents = int(input("Dependents: "))
Dependents: 2
>>> class ButtonDemo(EasyFrame):
...     def _init_(self):
...         EasyFrame._init_(self)
...         self.label = self.addLabel(text = "Compute",
...                                    row = 0, comumn = 0,
...                                    columnspan = 2,
...                                    sticky = "NSEW")
... 
...         
>>> taxableIncome = grossIncome - STANDARD_DEDUCTION - \
...                 DEPENDENT_DEDUCTION * numDependents
>>> incomeTax = taxableIncome * TAX_RATE
>>> print("Total tax" + str(incomeTax))
Total tax10200.0
