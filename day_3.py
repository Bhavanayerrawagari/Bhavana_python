-->To find out if it is a square or not using if else
n= input("enter the length value")
n1= input("enter the breadth value")
if n == n1:
    print("square")
else:
    print("not square")
-->Multiples of 5 and 7
n=int(input("enter your number"))
if n%5==0 and n%7==0:
    print("multiple")
else:
    print("not multiple")
-->Write a code according to the following
     >100000            15%tax+6%discount
     <100000            5% tax
price=int(input("enter bike price"))
if price>100000:
        discount = price*(6/100)
        value = price-discount
        tax=value*(15/100)
        total=value+tax
else:
    tax =price*(5/100)
    total=price+tax
print("total amount",total)
-->we canot give condition to else,for more than 2 conditions we use elif
-->To find the greatest number among 3
a=2
b=6
c=2
if a>b and a>c:
    print("a is greater")
elif b>a and b>c:
        print("b is greater")
else:
    print("c is greater")/ we can write the else statement by using elif also as,
elif c>a and c>b:
    print("c is greater")
-->based on the given data the grade has to be display grades of school marks
   
marks = int(input("enter your marks"))
if marks<25:
            print("F")
elif marks>=25 and marks<45:
            print("E")
elif marks>=45 and marks<50:
            print("D")
elif marks>=50 and marks<60:
            print("C")
elif marks>=60 and marks<80:
            print("B")
elif marks>=80:
            print("A")
SHORT HAND IF ELSE
**RULES
->statement inside  the if condition have to be present at first
->elif cannot be used in short hand if else
->always it have to end with else
 eg:print("a") if a>b else print("b")
-->to find the input variable is a vowel or consonant
Method 1
char =input("enter alphabet")
if char  == 'a' or char == 'e'or char == 'i' or char == 'o' or char == 'u':
    print("vowel")
else:
    print("consonant")
Method 2
char =input("enter alphabet")
str1 = "aeiouAEIOU"
if char in str1:
    print("VOWEl")
else:
    print("consonant")
Method 3
----> by using shorthand if else
char =input("enter the char")
str1="aeiouAEIOU"
print("VOWELS") if char in str1 else print("consonent")
-->To find greater among 3 using shorthand
a=3
b=4
c=1
print("a is greater") if a>b and a>c else print("b is greater") if  b>a and b>c else print("c is greater")
-->
LOOPING CONCEPTS
looping can be implimented using for and while loops 
->for loop
for loop is used for iteartion ,if we know the number of times the loop have to run
it is used to iterate the iterables. eg(string,list,tuple,etc..)
-->for syntax :
    for syntax in c:
        for(i=0;i<10;i++)
        {
            printf("hello")
        }
    for syntax in python:   
for userdefined_variables in range(start,end,step)-->(n,n-1,how much step we need,by default the step value is 1
    statement
    statement
    statement
Eg :1to print the values from 1 to 10
for i in range(0,11):
    print(i)
Eg:2
for i in range(12, 50,2):
    print(i)
for i in range(1,20):
   print("v")
Eg:3
to decrement the value
for val in range(20,1,-2):
    print(val)
Eg:4 to print the 7 table as 7x1=7---
Method 1
for val in range(1,10+1):
     print('7','X', val,'=' ,val*7)
Method 2 using format function
FORMAT FUNCTION
for val in range(1,10+1):
ans="7 x {} = {}"
 print(ans.format(val,val*7))
    print(f"7x{val}={val*7}")
BREAK STATEMENT:
IT IS USED TO TERMINATE THE LOOP
for i in range(1,10):
    if i==6:
        break
    print(i)
for i in range(1,10):
    if i==6:
      print(i)
      break
for i in range(1,10):
    print(i)
    if i==6:
      break
CONTINUE STATEMENT
Eg:1
for i in range(1,10):
  if i==5:
    continue
  print(i)
--->PRACTICE PROBLEMS
1.EVEN NUMBERS BETWEEN 20 AND 40
for i in range(20,40):
 if i%2==0:for odd i%2!=0
    print(i)
-->WHILE LOOP
**IT IS USED WHEN WE DONT KNOW THENUMBER OF TIMESTHE LOOP HAVE TO RUN
**TO ITERATE THE NON INTERABLE ELEMENTS WHILE LOOP IS USED
SYNTAX:
    INTILIZATION
    WHILE CONDITION:
        STATEMENT
        INCRE OR DECRE






