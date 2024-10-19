Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> startingSalary = int(input("Enter the starting salary: "))
Enter the starting salary: 30000
>>> percentageIncrease = int(input("Enter the yearly percentage increase: "))
Enter the yearly percentage increase: 2
>>> percentageIncrease = percentageIncrease / 100
>>> years = int(input("Enter the number of years: "))
Enter the number of years: 10
>>> for years in range (1, years + 1):
...     annualPay = startingSalary * percentageIncrease
...     print("%16s%20s%11s%5s" %
...           ("Starting Salary", "Percentage Increase", "Annual Pay", "Years"))
... 
...     
 Starting Salary Percentage Increase Annual PayYears
 Starting Salary Percentage Increase Annual PayYears
 Starting Salary Percentage Increase Annual PayYears
 Starting Salary Percentage Increase Annual PayYears
 Starting Salary Percentage Increase Annual PayYears
 Starting Salary Percentage Increase Annual PayYears
 Starting Salary Percentage Increase Annual PayYears
 Starting Salary Percentage Increase Annual PayYears
 Starting Salary Percentage Increase Annual PayYears
 Starting Salary Percentage Increase Annual PayYears
