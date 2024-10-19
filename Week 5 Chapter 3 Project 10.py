Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> purchasePrice = float(input("Enter the purchase price: "))
Enter the purchase price: 3500
>>> years = int(input("Enter the number of years: "))
Enter the number of years: 3
>>> rate = int(input("Enter the interest rate as %: "))
Enter the interest rate as %: 12
>>> rate = rate / 100
>>> totalInterest = 0.0
>>> print("%28s%29s%23s%18s" % \
...       ("Current total balanced owed", "Interest owed for that month", "Payment for that month", "Balance remaining"))
 Current total balanced owed Interest owed for that month Payment for that month Balance remaining
>>> for year in range(1, years + 1):
...     interest = purchasePrice = rate
...     remainingBalance = purchasePrice + interest
...     print("%28s%29s%23s%18s" % \
...           (currentTotalBalancedOwed, interestOwedForThatMonth, paymentForThatMonth, balanceRemaining))
...     purchasePrice = remainingBalance
...     totalInteres += rate
...     print("Ending balance: $%0.2f" % endBalance)
...     print("Total interest earned: $%0.2f" % totalInterest)
... 
...     
Traceback (most recent call last):
  File "<pyshell#16>", line 5, in <module>
    (currentTotalBalancedOwed, interestOwedForThatMonth, paymentForThatMonth, balanceRemaining))
NameError: name 'currentTotalBalancedOwed' is not defined
