Python 3.12.5 (tags/v3.12.5:ff3bc82, Aug  6 2024, 20:45:27) [MSC v.1940 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def mean(numbers):
...     if not numbers:
...         return 0
...     return sum(numbers) / len(numbers)
... 
>>> def median(numbers):
...     if not numbers:
...         return 0
...     sortedNumbers = sorted(numbers)
...     n = len(sortedNumbers)
...     mid = n // 2
...     if n % 2 == 0:
...         return(sortedNumbers[mid - 1] + sortedNumbers[mid]) / 2
...     else:
...         return sortedNumbers[mid]
... 
...     
>>> def mode(numbers):
...     if not numbers:
...         return 0
...     frequency = {}
...     for number in numbers:
...         frequency[number] = frequency.get(number, 0) + 1
...         maxFreq = max(frequency.values())
...         modes = [number for number, freq in frequency.items() if freq == maxFreq]
...         if len(modes) == 1:
...             return modes[0]
...         else:
...             return modes
... 
...         
>>> def main():
...     testNumbers = [1, 2, 2, 3, 4, 4, 4, 5, 5,]
...     print(f"Mean: {mean(testNumbers)}")
...     print(f"Median: {median(testNumbers)}")
            





    

    
