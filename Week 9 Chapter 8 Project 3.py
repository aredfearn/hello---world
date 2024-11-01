Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> def kochSnowflake(order, size):
...     if order == 0:
...         turtle.forward(size)
...     else:
...         for angle in [60, -120, 60, 0]:
...             kochSnowflake(order-1, sie/3)
...             turtle.left(angle)
...             turtle.speed(0)
...             turtle.penup()
...             turtle.goto(-150, 100)
...             turtle.pendown()
...         for _ in range(3):
...             kochSnowflake(4, 300)
...             turtle.right(120)
...             turtle.hideturtle()
...             turtle.done()
... 
...             
