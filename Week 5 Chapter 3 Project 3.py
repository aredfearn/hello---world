Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
>>> import math
>>> 
>>> smaller = int(input("Enter the smaller number: "))
Enter the smaller number: 1
>>> larger = int(input("Enter the larger number: "))
Enter the larger number: 25
>>> myNumber = math.log(smaller, larger)
>>> count = 0
>>> count += 1
>>> myNumber = int((smaller + larger)/2)
>>> print(smaller, larger)
1 25
>>> print("Your number is: ",myNumber)
Your number is:  13
>>> hlp = input("Enter =,, <, or >: ")
Enter =,, <, or >: 
>>> if hlp == '>':
...     smaller = myNumber+1
... elif hlp == '<':
...     larger = myNumber-1
... elif hlp == '=':
...     print("Yippee, I got it in", count, "tries!")
... else:
...     print("I'm out of guesses, I give up!")
...     break
SyntaxError: 'break' outside loop
>>> 
