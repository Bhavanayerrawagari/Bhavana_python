#DAY-1
'''
  print("hello world")
COMMENTING-
1.It is used for making documentation in python file.
2.When a line is commentend that  line will be not be considered as a part of the code
3.when the program is executed,commented line will not be in the part of execution.
NOTE:
  -->  single line commenting can be done using # at the beginning of the line
    eg:#print("hello")
  -->  Multiple line commenting can be done using  '''code''',the lines between the quotes will be commented.
    eg:print("hello ")
        '''
         print("hello world")
         print("hello world")
         '''
        print("hello frnds")
IMPORT:
    Import is a keyword which is used to communicate between the python files
    eg:import(file_1)
       print(file_name)
            or
       from file_1 import(a,b)
       print(a)
       print(b)
BARGAINED CHARACTERISTICS:
    Controls & data structures-->ABC language
    String & its format-->from C
    Regular Expressions-->fortorn
    Exceptional handling-->Module 3
    Magic methods from-->Fortron
WHAT KIND OF LANGUAGE IS PYTHON?
1.Object orientend programming language-OOPS is a programming  which uses "classes and objects",and it is used to implement real time world applications (which is a userfriendly language)
2.Dynamically typed language-This consists of a interpreter(which is nothing but a compiler), so that there will be no need of declaring the variable type before using it.
3.Interpretted programming language-As in c the compiler complies block wise,here it compiles line-by-line(up to the correct line it will show the result in console).
4.Compiled language
FLAVOURS OF PYTHON:
    Cpython-written in c,most common implementation of python
    Jython-Java implementation of python
    Ironpython-which is tightly integrated with .NET
    Brython-Browser python,runs in browsers
    Rubypython-Bridge between python and ruby interpreter
    Micropython-runs in microcontrollers
print()---->which is used to print the result in console
      It has 5 parameters:object,sep,end,file,flush
      OBJECT:The value to be printend is object
      Eg:print(a)---where a is called object
      SEPERATOR-which is used to seperate variables
      eg:a=3
         b=2
         print(a,b,sep='$')
      END:which is used to add the string at the end of the value.It will not keep the command to stay in same line.
      eg:
          a=2
          b=3
          c=4
          print(str(a),b,end='%%')
          print(str(c))
VARIABLE:It is a name which is used to identify the value of variables which is stored in a specific memory loaction.
RULES TO DEFINE VARIABLES:
    1.variable have to start with only alphabets,underscores.
    2.The cahr follwing the 1st char can be alphabets,numbers,underscores.
    3.No spaces are allowed.
    4.No specific characters like !@#$%^&*
    5.Case sensitive
    6.Keywords are not allowed as variables.
WAYS TO DEFINE VARIABLES:
    we cannot define variables in the same line
      eg:a=3,b=4
         print(a,b)
    we cannot assign single value to multiple variables
      eg:a,b=78
         print(a,b)
     if no.of variables=no.of values(then there will be no error)
      eg:a,b=7,9
         print(a)
         print(b)
TUPLE:collection of data types
  eg: a=8,9.87,"hello"
      print(a)
      print(type(a))
'''
      
#CODE:
#print("hello ")
'''
print("hello world")
print("hello world")
print("hello frnds")
#import this
print(this)
#import antigravity
#a=3
b=2
print(a,b,sep='$')
#a=2
b=3
c=4
print(str(a),b,end='%%')
print(str(c))
#a=3,b=4
print(a,b)
#a,b=78
print(a,b)
#a,b=7,9
print(a)
print(b)
#a=8,9.87,"hello"
print(a)
print(type(a))
'''         




