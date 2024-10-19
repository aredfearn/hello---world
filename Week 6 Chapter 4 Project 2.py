Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> f = open("decrypt.py", 'r')
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    f = open("decrypt.py", 'r')
FileNotFoundError: [Errno 2] No such file or directory: 'decrypt.py'
>>> plainText = input("Enter a message: ")
Enter a message: message
>>> distance = int(input("Enter the distance value: "))
Enter the distance value: 10910111511597103101
>>> f.close()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    f.close()
NameError: name 'f' is not defined
