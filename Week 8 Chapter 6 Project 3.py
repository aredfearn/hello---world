Python 3.12.7 (tags/v3.12.7:0b05ead, Oct  1 2024, 03:06:41) [MSC v.1941 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def isSorted(lst):
...     if len(lst) < 2:
...         return True
...     for i in range(len(lst) - 1):
...         if lst[i] > lst[i + 1]:
...             return False
...         return True
...     if _name_ == "main_":
...         testCases = [
...             ([], True),
...             ([1], True),
...             ([1, 2, 3, 4, 5], True),
...             ([5, 4, 3, 2, 1], False),
...             ([1, 3, 2, 4, 5], False),
...             ([1, 2, 2, 3, 4], True)
...             ]
...         for i, (lst, expected) in enumerate(testCases):
...             result = isSorted(lst)
...             print(f"Test case {i + 1}: {'Passed' if result == expected else 'Failed'}")
... 
...             
