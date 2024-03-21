'''
-->while loop
break using while loop
-->iterate from 20 to 30 and break the loop in 27

i=20
while i<31:
    if i==27:
        break
    print(i)
    i+=1-->20-26
    
i=20
while i<31:
    print(i)
    if i==27:
        break
    i+=1-->20-27
    
i=20
while i<31:
    print(i)
    i+=1
    if i==27:
        break-->20-26
    
i=20
while i<31:
    if i==27:
       print(i)
       break
    i+=1-->only 27
    
#CONTINUE USING WHILE LOOP:
i=20
while i<31:
    i=i+1
    if i==27:
       continue 
    print(i)
-->to find the sum of numbers from 12 to 22

-->
i=12
sum=0
while i<23:
    sum=sum+i
    i+=1
print(sum)

--> to find the average from20 to 25    
i=20
sum=0
while i<26:
    sum=sum+i
    avg=sum/6
    i+=1
print(avg)

#to find avg for n no.of variables
i=20
sum = 0
count = 0
while i<=30:
    sum=sum+i
    count+=1
    i+=1
print(sum/count)

#--->Nested for loop
for i in range(1,4):
    for j in range(1,5):
        print(i,j)
      
-->to get o/p as
* * * *
* * * *
* * * *
* * * *
for row in range(1,5):
    for col in range(1,5):
        print("*",end=" ")
    print()
-->    
To execute n.no of rows
--->

rows=int(input("enter the rows:"))
cols=int(input("enter the cols:"))
for row in range(rows):
    for col in range(cols):
        print("*",end=" ")
    print()
-->
for row in range(5):
    for col in range(5):
        print(row,end=" ")
    print()
-->
sum=0
for row in range(5):
    for col in range(5):
        sum=sum+1
        print(sum,end=" ")
    print()
-->to print starts in right angle traingle

for row in range(0,6):
    for col in range(0,row+1):
        print("*",end=" ")
    print()

for row in range(0,6):
    for col in range(row,6):
        print("*",end=" ")
    print()
-->top print square
for row in range(6):
    for col in range(6):
        if col==0 or col==5 or row==0 or row==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
-->to print a triangle:

for row in range(0,5):
    for col in range(0,6):
        if ((row==0 and col==3) or (row==1 and (col>=2 and col<=4) or (row==2 and (col>=1 and col<=5)))):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

-->for triangle
for row in range(0,4):
    for col in range(0,4):
        if (col==0 or row==3):
            print("*",end=" ")
        elif((row==1 and col==1) or (row==2 and col==2)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
DATA TYPES:
    mainly two type:
        primary and collection
-->primary:numbers(int,float,complex),string,boolean,none
-->collection:list,tuple,set,dicitonary
LIST:if the collection of elements are sorrounded by[]square brackets.
Eg:l1=[1,2,3,9.67"hello",[4,5]]
-->characteristics of list:
    1. list have to be sorrounded by []
    2.it is mutable(the elements in the list are changable)
    3.every element inside list is indexed
    4.the elements inside list will be ordered format
    5.it can hold duplicate values
    6.its heterogenous
-->To access the elements in list
l1=[1,4,89.8,"p"]
-->INDEXING:
 In the collection datatypes like list,tuple,string, the elements will be alloted with pre-defined unique value called index value
 ->we have two types of indexing
 --> Positive indexing=starts with 0 from left hand side
 ->Negative indexing=starts with -1 from right hand side
 
#positve index
m1=[1,2,3,9.67,"hello",[4,5]]
print(m1[0])
print(m1[10])-->Error cause index ouof range
#Negative indexing:
m1=[1,2,3,9.67,"hello",[4,5]]
print(m1[-1])-->[4,5]

-->SLICING:
lst[start_index:end_index:step]
using positive indexing
lst=[1,4,1,7,89.7,7.5,"p","i"]
print(lst[0:4])
print(lst[6:8])
print(lst[:3])
print(lst[3:])
print(lst[:])
print(lst[0:4:1])-->last one shows the step value

using negative indexing
lst=[1,4,1,7,89.7,7.5,"p","i"]
print(lst[-4:-1])
print(lst[-1])
print(lst[-7:-1:2])-->4,7,7.5 step of 2
-->To insert/add element inside list we use append function and it will add it at last
    
l1=[1,2,3]
l1.append("car")
print(l1)
'''
a=[10,50,89]
b='123'
for i in a:
    b=b+" " +i
    print(b)








        
        
         













    



      

    
   
       
   
















    
    
