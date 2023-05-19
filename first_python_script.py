#get working directory
import os
os.getcwd()

x = 2
print(x)

# test basic operations
x % 2    #calculate remainder when divided by 2
x / 1.2  #standard division
x // 1.2 #floor division (round the answer down to the nearest integer)
x ** 2   #power

# printing
print("fist line \n second line")   #use \n for skipping lines
print(r"fist line \n second line")  #use r preface to print 'raw strings'

# strings
mystring = "hello"
string2  = " and me"
mystring*2 + string2  #can use arithmetric operations on strings to concatenate them
mystring[0]      #strings can be indexed; NB indexes start with 0, not 1
mystring[-1]     #negative indexes count from end of the string, NB these start with -1 (since -0 = 0)
mystring[0:2]    #slicing can be used to obtain substrings (note that the last number is excluded, so this captures indices 0 and 1)
mystring[:4]     #omitting the first index defaults to 0
mystring[0:]     #omitting the last index defaults to the size of the string
mystring[-2:]    #e.g. 2nd to last to the last 
mystring[100]    #gives out of range error
mystring[0] = 1  #strings are immutable (items can't be redefined)

# useful basic functions
x = 1,2

#length
len(x)        #length of object
len(mystring) #no. characters in a string

# lists
x1 = [1, 2, 3, 4]    #define with square brackets; can include items of same or...
x2 = [1, 2, "a", 4]  #...mixed type
x3 = x1 + x2         #concatenation can be done with '+' operator
x3[0] = "hello"      #lists ARE mutable (i.e., their contents can be changed)
x3.append(1)         #items can be added to the end of lists using append()
x3             
x = []               #[] can be used to assign an empty list
x[0:5] = [1,2,3,4]   #and later assign values
x[:] = []            #lists can be emptied by assigning all elements, [:], to []

# nesting lists 
x = [1,2,3,4,5]
y = [1,2,3]
z = [x, y]
z

# mulitple assignment
a,b = 1,2  #a gets assigned 1, b gets assigned 2
a
b

##--------------##
## CONTROL FLOW ##
##--------------##

## WHILE STATEMENTS
# Fibonacci series example
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:  #note conditional statements end with a ':'
    print(a)
    a, b = b, a+b  #here, a=b, and b=a+b

a,b = 5, 5*2
a,b

# note that print can be used like print(paste()) in R
i = 256*256
print('The value of i is', i, end="\n")  #defaults to ending with a new line (\n) but can be changed with the end argument

## IF STATEMENTS
x = int(input("Please enter an integer: ")) # int() specifies type as integer; input() can be used to request an input from the user

if x < 0:  #note lack of brackets around conditional statement & no curly braces after
    x = 0   
    print('Negative changed to zero')
elif x == 0:   #NB elif is the equivalent of else if from R
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# another if statement (testing my own)
toggle1, toggle2 = 1,0

if toggle1 & toggle2:  #NB no need to define as toggle1 == 1 (if implicitly asks if variable is TRUE [where non-zero integers are all TRUE])
    print("Do some action here")
else:
    print("Do some other action here")

# another example
toggle1 = 2

if toggle1 == 3:
    print(3)
else:
    print("Another number:", toggle1)

## FOR STATEMENTS

# loop over a string
some_things = ["hello", "goodbye", "good night"]

for i in some_things:  #equivalent to R's: for(i in 1:length(some_things)){}
    print(i, len(i))   #note that index variable i iterates over the items of any sequence (you do not need to specify some_things[i])

# for loops using range()
for i in range(5):   #by default range starts at 0 and ends at max(range) -1
    print(i)

range(5)            #doesn't make the list until called to; saves space
list(range(5))      #to see the elements of range
list(range(0,5,2))  #can be used like R's seq(); arguments define the start, end & incremenet respectively

# can iterate over the indices of a sequence
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):  #like in R: for(i in 1:length(a)); range is an 'iterable' object
    print(i, a[i])

sum(range(4))  #0+1+2+3

# break statements
for i in range(1,5):
    if i == 3:
        break  #break when condition met & exit for loop
    print(i)   #hence all values BEFORE condition met are printed

# continue statements
for i in range(2,10):
    if i % 2 == 0:
        print("Found an even number:", i)
        continue #continues with the next iteration of the loop
    print("Found an odd number:", i)

# FUNCTIONS
def fnx(x):   #def is used to define a function, followed by function name then input parameters
    print(x**2)  #x squared

fnx(2)  #call the function

def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n.
    
    You usualy document functions like this (note the triple quotes) to begin & close the multi-line comment.
    """
    a, b = 0, 1 
    while a < n:
        print(a, end=' ')
        a, b = b, a+b  #python assigns right to left, so b=a+b performed, then a=b
    print()

# Now call the function we just defined:
fib(2)


def fib2(n):  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []  #create empty list
    a, b = 0, 1  # define initial values for a and b
    while a < n: #while loop
        result.append(a)    #'append' is a 'method'; equivalent of (but more memory efficient than): result = result + [a]
        a, b = b, a+b       #python assigns right to left, so b=a+b performed, then a=b
    return(result)  #returns value from the function

f100 = fib2(100)    # call it
f100                # write the result

del f100   # can remove variables from environment using del

# you can also define default arguments for functions, like in R
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

ask_ok("Do you really want to quit?")

# playing with keyword 'in'
answer = "y"
if answer in ("yes", "y", "yeah"):  #the 'keyword' in checks whether a sequence contains a certain value
    print("Yay!")
else:
    print("Neigh!")

## continuing learning: 09/05/2023
list(range(5, 10)) # can use range(x, n) where x=starting number and n=ending number+1 

x = ["Sup", "Hello", "Yo", "Weird"]
for i in range(len(x)):  #can also use range(len()) to iterate over the indices of a (non-numeric) sequence
    print(x[i])

x = range(0,10,2)  #can use range() like R's seq() function; with arguments range(start, stop, step)
list(x) #show the output using list()

sum(range(4))

## match statement: takes an expression and compares its values to successive patterns given as >=1 'case' blocks
def matching_function(status):
    match status:
        case 100:
            return "Naaah"
        case 200:
            return "Neither"
        case 300: 
            return "Bingo!"
        case _:
            return "Something's wrong"


x = "Iron"
x1 = x.lower(), x.upper() #can use .lower() and .upper() to make strings all in lower or upper case
x1[0][0].upper() + x1[0][1:].lower() #playing with this function


## functions continued: using keyword arguments (kwargs)
# *arguments here defines non-keyworded/positional arguments
# **keywords here defines keyworded arguments
# use case: we don't know the number of arguments needed in advance
def cheeseshop(kind, *arguments, **keywords):  # * signifies elements of a tuple; ** signifies elements of a dictionary
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

# it can be called like this:
cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           "I can add another one here to show that these are all assigned to the *arguments input",
           # the below are keyword arguments (note that changing their position changes the order they're printed in):
           shopkeeper="Michael Palin",  #keyword parameters also known as "named parameters"
           client="John Cleese",
           sketch="Cheese Shop Sketch")

## Functions continued: Special parameters

# By default, arguments may be passed to a Python function either by position or explicitly by keyword

# the "standard" argument, which can be called either with a positional parameter or a keyword
def standard_arg(arg):
    print(arg)
# parameters can be marked as positional-only by defining parameters followed by ", /" as below
def pos_only_arg(arg, /):
    print(arg)
# parameters can also be marked as keyword only with "*, arg" as below
def kwd_only_arg(*, arg):
    print(arg)
# in the combined example, this function takes positional-only, 'standard' or keyword-only arguments
def combined_example(pos_only, /, standard, *, kwd_only):
    print(pos_only, standard, kwd_only)

# both work with no restriction on how function is called (positional or keyword arguments)
standard_arg(arg=2) #places no restrictions on the calling conventions
standard_arg(2)     #places no restrictions on the calling conventions
# only positional works
pos_only_arg(2)
pos_only_arg(arg=2)  #this fails with an error
# only keyword works
kwd_only_arg(2)  #this fails with an error (gave positional argument even though the function takes none)
kwd_only_arg(arg=2)
# combined example:
combined_example(3, standard=2, kwd_only=1) #this works
combined_example(3, 2, kwd_only=1) #this works
combined_example(pos_only=3, 2, kwd_only=1) #this fails with error (keyword given to positional argument)
combined_example(3, 2, 1) #this fails with error (missing correct keyword argument call)

### The above can be summarised by:
# def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
#       -----------    ----------     ----------
#         |             |                  |
#         |        Positional or keyword   |
#         |                                - Keyword only
#          -- Positional only

# my own example function:
def some_test_func(arg1, /, arg2, *, arg3, arg4):  #everything past the * must be called with the parameter keyword
    print(arg1, arg2, arg3, arg4)

some_test_func(1, arg2=2, arg3=3, arg4=100)

## Unpacking argument lists
# When arguments are already in a list or tuple but need to be "unpacked" for a function call requiring separate positional arguments:
args = [3,6]  #start & stop arguments for range(), in a tuple 
list(range(*args)) #unpack these arguments using the * syntax!

# similarly, dictionaries can deliver keyword arguments using the ** syntax: 
def parrot(voltage, state='a stiff', action='voom'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.", end=' ')
    print("E's", state, "!")

#Note use of dictionary definition, with curly braces {} & key:value pairs
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"} 
parrot(**d)  #** delivers keyword arguments

# got up to 4.8.5 (https://docs.python.org/3/tutorial/controlflow.html)

## make change for test commit