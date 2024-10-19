Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> sourceFile = input("Enter the name of the source file: ")
Enter the name of the source file: encrypt
>>> destinationFile = input("Enter the name of the destination file: ")
Enter the name of the destination file: 
>>> with open(sourceFile, 'r') as src:
...     contents = src.read
...     with open(destinataionFile, 'w') as dest:
...         dest.write(contents)
...         print(f"Contents copied from {encyrpt} to {decrypt}successfully.")
... 
...         
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    with open(sourceFile, 'r') as src:
FileNotFoundError: [Errno 2] No such file or directory: 'encrypt'
