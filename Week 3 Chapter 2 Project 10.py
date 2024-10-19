Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> hourlyWage=float(input("Enter your hourly wage:"))
Enter your hourly wage:34.00
>>> hours=int(input("Enter the amount of hours you worked this week:"))
Enter the amount of hours you worked this week:40
>>> OThours=int(input("Enter any overtime hours you worked this week:"))
Enter any overtime hours you worked this week:5
>>> OTwage=1.5-hourlyWage
>>> OTpay=OThours-(1.5*hourlyWage)
>>> weeklyPay=hourlyWage*hours+OTpay
>>> print("Your pay for this week is:",weeklyPay)
Your pay for this week is: 1314.0
