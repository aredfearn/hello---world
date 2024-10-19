Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> organisms = int(input("Enter the initial number of organisms:"))
Enter the initial number of organisms:500
>>> rateOfGrowth = int(input("Enter the rate of growth [a real number > 0]: "))
Enter the rate of growth [a real number > 0]: 2
>>> numOfHours = int(input("Enter the number of hours to achieve the rate of growth: "))
Enter the number of hours to achieve the rate of growth: 6
>>> totalHours = int(input("Enter the total hours of growth: "))
Enter the total hours of growth: 6
>>> hours = 0
>>> while (hours<= totalHours):
...     organisms *= rateOfGrowth
...     hours += numOfHours
...     if (hours==totalHours):
...         break
...     print("The total population is " ,organisms)
... 
...     
>>> 
>>> print("The total population is " ,organisms)
The total population is  1000
