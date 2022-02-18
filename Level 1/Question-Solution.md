### Question 1
Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: Consider use range(#begin, #end) method<br><br>
 Solution:
```python
list1 = [x for x in range(2000,3201)] # List which has numbers in range 2000-3200
list2 = [str(x) for x in list1 if (x%7==0 and x%5!=0)] # List which has numbers which are divisible by 7 and are not the multiple of 5
print(', '.join(list2))
```

### Question 2
Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.<br><br>
Solution:
```python
list = []
user = int(input("How many numbers of factorials you want to calculate? "))

for i in range(0,user):
    n = int(input("Enter the number to calculate its factorial : "))
    if(n == 1 or n == 0):
        list.append('1')
    else:
        fact = 1
        for i in range(1,n+1):
            fact *= i
        list.append(str(fact))

print(', '.join(list))
```


### Question 3 
Question: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary. Suppose the following input is supplied to the program: 8 Then, the output should be: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints: In case of input data being supplied to the question, it should be assumed to be a console input. Consider use dict()<br><br>
Solution:
```python
user = int(input("Enter number of values to be squared from 1 : "))
dict = { x: x**2 for x in range(1,user+1)}
print(dict)
```

### Question 4
Question: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be: ['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

Hints: In case of input data being supplied to the question, it should be assumed to be a console input. tuple() method can convert list to tuple<br><br>
Solution:
```python
user = input("Enter comma seperated values : ")
list = user.split(',')
print(list)
print(tuple(list))
```

### Question 5
Question: Define a class which has at least two methods: getString: to get a string from console input printString: to print the string in upper case. Also please include simple test function to test the class methods.

Hints: Use init method to construct some parameters<br><br>
Solution:
```python
class Methods:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = input("Enter a string")

    def printString(self):
        print(self.s.upper())

obj = Methods()
obj.getString()
obj.printString()
```

