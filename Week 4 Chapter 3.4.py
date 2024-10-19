Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> height = float(input("Enter the height the ball is dropped in feet: "))
Enter the height the ball is dropped in feet: 10
>>> bounced = float(input("Enter the height in feet the ball bounced: "))
Enter the height in feet the ball bounced: 6
>>> numberOfBounces = int(input("Enter the number of times the ball bounced: "))
Enter the number of times the ball bounced: 2
>>> index = float(input("Enter the bounce Index: "))
Enter the bounce Index: 0.6
>>> calculatedHeight = float(height*index)
>>> heightDifference = height-calculatedHeight
>>> bounceSum = (calculatedHeight/1-index)
>>> totalDistance = ((((2*bounceSum) + height)))
>>> print("The total distance is: ", totalDistance)
The total distance is:  20.8
