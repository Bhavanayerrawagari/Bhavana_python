--> SWAPPING OF NUMBERS-it is done by using the "temp"
Eg:
    1.a=5
      b=6
      temp=a--->temp=5
      a=b--->a=6
      print(a,b)-->6,5
    2.a,b=b,a
      print(a,b)->without using a another memory loaction
    3.a=2
     b=3
     a=a+b--->a=2+3=5
     b=a-b--->b=5-3=2
     a=a-b--->a=5-2=3
     print(a-b)--->3,2
    4.a=a*b-->2*3=6
      b=a/b-->6/3=2
      a=a/b-->6/2=3
      print(a,b)=3.0,2.0--->in this eg when we write print(a,b) the output will be in the form of float if we need to change it to the integer then
      print(int(a),int(b)-->3,2
-->To find out the "memory address" of the particular variable we use the key woed "id"
           eg:1 a=7
                b=8
                print(a)
                print(id(a))-->2642151866800-->it will change for every run
                print(id(b))-->2642151866832
              2. a=3
                 b=3
                 print(id(a))--->265438698
                 print(id(b))---->265438698--both will have the same memory location because in python if the values are same even though variables are different they will
                 point out to the same memory location.
----->KEYWORDS
            keywords are reserved words which provides special meaning to compiler or interpretor.
To check no.of keywords in python,
            import keyword
            print(keyword.kwlist)--->[False,True-----and so on]
To find out the length(no.of keywords)
           print(len(keyword.kwlist))--->35
To find out the type
           print(type(keyword.kwlist))-->class 'list'                              
To check if the given string is keyword or not
        print(keyword.iskeyword("sid"))-False-->if the given string is a keyword it will show true if not then false
#-- we cannot use keywords as variable names
        if=5
        print(if)-->error because if is a keyword
-->LITERALS:
    It is a constant value assigned to a variable .A variable is consider to be constant when it is define in caps
    eg:A=7
    a=4-->a is variable
    A=4-->A is literal/constant
-->CONSTANT:
    It creates a hash value for constant data types and provides error for non constant datatypes
    The hash value can be generated for all constant values like int(any number),float(6+8j),strinh("hi"),tuple(3,4)
eg: 1.n=89+7j
      print(hash(n))-->700110
    2.f=[7,4]
      print(hash(f))-->error cause list is not a constant
-->OPERATORS:
    operators are symbols which is used to perform various operations between two or more operands
1.Arithmetic operator:-->+,-,*,/,%,//,**
eg:1.a=3
     b=2
     c=2
     print(a+b+c)-->same for -.*
    2.a=4
      b=2
      print(a/b)-->used for quotient value
      print(a%b)-->used for remainder value
    3.floor division
      a=23456
      b=345
      print(a/b)-->output will be in the float value (like 3456.087)
      print(a//b)-->here it wonnot generate the value after the point(.)
    4.**--used for power number
      print(2**4)--->output=16

-->if we need to input the value after compiling we use keyword "input",
   n1=input("enter the value:")
   print(n1)-->output:enter the value:4  4
   print(type(n1)-->ouput will be string because when ever we use input()only without specifing any type at front it will show str
eval()-->used to get the runtime values of datatypes
         n1=eval(input("enter the value:"))
         print(type(n1))-->if the enter value is 78(num)it will show int,if it is 8+j it will show (float),if it is "hii" it will show str

2.Assignment operators:-->+-=,>,<,!=,<=,>=
    eg:
         a=8
         a+=2
         print(a)-->output=10
Comparision-->==,<,>,!=,<=,>=
         eg:a=8
            b=7
            print(a>b)-->if the statement is correct it will show true otherwise false
3.Bitwise operators:--->&,|,^,~,<<,>>
which are used for bit manupulation
         &=and,|=or,^=xor,~=tilda,<<=lift shift,>>=right shift
&--->a=7
    b=4
    print(a&b)-->output=6,by performing the and gate operation truthtable like wise same or and xor
~--->a=9         
    print(~a)-->output=-10 the tilda operator works as it gives the output as the negative nextvalue of the input
    tilda which converts 0 to 1 and 1 to 0
<<-->print(5<<3)
    output=40-->here first we have to write the binary code for the input value here it is 5 so,
                            128 64  32 16  8  4  2  1
                            0   0   0   0  0  1  0  1--->5,and it has to shift left for 3
                            0   0   1   0  1  0  0  0-->40
>>-->print(5>>3)
    output=0-->8  4  2  1
               0  1  0  1-->5,shift right for 3
               0  0  0  0  1  0  1-->since there is no value here it is 0
    print(20>>3)-->ouput=2--->16  8  4  2  1
                               1  0  1  0  0-->20,>>for 3
                               0  0  0  1  0  1-->2
4.LOGICAL OPERATORS:and,or,not
         which are used to compare the expressions
         Eg: a=6
             print(a>3 and a<10)-->True,if the print condition is satisfies it will show true otherwise false
             print(a>3 or a<30)-->True,                 "
             print(not(a>8 and a<10))-->true,it will show opposite to the condition
5.IDENTITY OPERATOR:is,is not
         It is used to compare the memory location that the values are stored
         Eg:a=8
            b=8
            print(a is b)-->True,because both will have the same memory location
            print(a is not b)-->False
         2.a=[1,2,3]
           b=[1,2,3]
           print(a is b)-->False,list has a different memory location even though the values in it are same cause it is a variable
        3. a=(1,2)
           b=(1,2)-->True,because tuple has same memory location since it is a constant
6.MEMBERSHIP OPERATOR:in,not in
         used to check if the required value is present in the collection or not
        Eg:1.n=[2,3,4,5]
             num=55
             print(num in n)-->False,becuase 55 not in the list
         2.m=67
           num=7
           print(num in m)-->Error,because these operators only perform for list of collection values
--> for tuple also it will work
--->CONDITIONAL STSTEMENTS: if,elif,else
if--> 1.a=6
        if a:
            print("hello")-->hello
       2.a=0
         if a:
             print("hello")--->the output will not come/display
--> for a=0,a=none,a=false,a=" "--> the if condition doesnot work for these else will work
if else-->a=0
          if a:
              print("yes")
          else:
              print("no")-->no,as stated above
2. if the given number is even or odd
n=int(input("enter the value:")
if n%2==0:
      print(n,"even")
else
      print(n,"odd")
-->the user has to input the name,age,nationality if his/her age is above 18 and nationality is indian it has to display eligible for vote
name=input("enter the name:")
age=input("enetr the age:")
nat=input("enter the nationality:")
if n>=18 and n==indian:
    print("eligible for vote:")
else:
    print("not eligible for vote:")
    
         

         
 
         














