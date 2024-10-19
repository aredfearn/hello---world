Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def navigte_file_lines():
...     filename = input("Enter the filename: ")
...     try:
...         with open(filename, 'r') as file:
...             lines = file.readlines()
...             while True:
...                 print(f"The file has {len(lines)} lines.")
...                 line_number = int(input("Enter a line number (0 to quit): "))
...                 if line_number == 0:
...                     Print("Exiting the program.")
...                     break
