<details>
    <summary>Question 1</summary>
    <p>
        Question: Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H] Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to your program in a comma-separated sequence. Example Let us assume the following comma separated input sequence is given to the program: 100,150,180 The output of the program should be: 18,22,24

Hints: If the output received is in decimal form, it should be rounded off to its nearest value (for example, if the output received is 26.0, it should be printed as 26) In case of input data being supplied to the question, it should be assumed to be a console input.<br><br>
    </p>
</details>
Solution:
```python
print("C = 50\nH = 30")
c = 50
h = 30
d = input("Enter comma seperated values of variable D : ")
list = [int(x) for x in d.split(',')]

list2 = [str(((2*c*x)/h)**(1/2)) for x in list]
print(', '.join(list2))
```

### Question 2
Question: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1. Example Suppose the following inputs are given to the program: 3,5 Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

Hints: Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.<br><br>
Solution:
```python
r = int(input("Enter the number of rows : "))
c = int(input("Enter the number of columns : "))

list = [[x*y for x in range(c)] for y in range(r)]
print(list)
```

### Question 3 
Question: Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically. Suppose the following input is supplied to the program: without,hello,bag,world Then, the output should be: bag,hello,without,world

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.<br><br>
Solution:
```python
w = input("Enter comma seperated words : ")
list = [x for x in w.split(',')]
print(','.join(sorted(list)))
```

### Question 4


Question: 
Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized.
Suppose the following input is supplied to the program:
Hello world
Practice makes perfect
Then, the output should be:
HELLO WORLD
PRACTICE MAKES PERFECT

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
```python
user = input("Enter a string : ")
print(user.upper())
```

### Question 5


Question:
Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
Suppose the following input is supplied to the program:
hello world and practice makes perfect and hello world again
Then, the output should be:
again and hello makes perfect practice world

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
We use set container to remove duplicated data automatically and then use sorted() to sort the data.

Solution:
```python
user = input("Enter a string : ")
a = user.split(' ')
b = set(a)
a = list(b)
a.sort()
print(' '.join(a))
```

### Question 6


Question:
Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
```python
user = input("Enter comma seperated binary digits : ")
list1 = user.split(",")
list2 = []
i = 0
while(i<len(list1)):
    if(list1[i] == "1010" or list1[i] == "0101" or list1[i] == "1111"):
        list2.append(list1[i])

    i += 1
print(' '.join(list2))
```


### Question 7

Level 2

Question: Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number. The numbers obtained should be printed in a comma-separated sequence on a single line.
Hints: In case of input data being supplied to the question, it should be assumed to be a console input.

Solution:
```python
def is_even(a):
    check = True
    while(a>0):
        if((a%10)%2 == 0):
            a = a//10

        else:
            check = False
            break
    return check


list1  = [x for x in range(1000,3001)]
even = list(filter(is_even, list1))
print((even))
```

