# 1 - Conventions
#num = int(input('Enter another number: '))
#print(f'{num} is positive and {num} square is {num*num}') if num > 0 else print('Bye')
'''my_string = 'Hello word!'
print(my_string[::-1])
print(my_string[:5])
title = 'The Good, The Bad, and the Ugly'
print(f'Source code: {title}')
print('Split using a space: ', title.split(' '))
print('Split using a comma: ', title.split(','))
print('String count: ', title.count(' '))
welcome_massage = 'Hello World!'
print(welcome_massage.replace("Hello", "GoodBye"))
print("Edward Alun Rawlings".find('John'))
format_string = "{artist} sang {song} in {year}"
print(format_string.format(artist='Paloma Faith', song='Guilty', year=2023))
import string
template = string.Template('$artist sang $song in $year')
print(template.substitute(artist='Freddle Mercury', song='The Great Pretender', year=1987))'''
'''import random
# Dice Roll Game
MIN = 1
MAX = 2
roll_again = 'y'
while roll_again == 'y':
    print('Roolling the dices...')
    print('The values are...')
    dice1 = random.randint(MIN, MAX)
    print(dice1)
    dice2 = random.randint(MIN, MAX)
    print(dice2)
    roll_again = input('Roll teh dices again: (y / n): ')

# Calculate the factorial of a number.
import os
def factorial(n)->int:
    if n in (0,1): return 1
    return factorial(n-1) * n

#n = 5
#print(factorial(n))
def show_result()->str:
    inputs = int(input("Enter a number to calculate factorial: "))
    if inputs < 0 : 
        print("The number can not be less tan zero!")
        inputs = int(input("Enter a number to calculate factorial: "))
        os.system('clear')
    print(f"The fatorial of {inputs} is {factorial(inputs)}")

show_result()

# Number Guessing Game
import random as rd

COMPUTER = 0
PLAYER = 0
MIN, MAX = 1, 10

def inputs()->int:
    return int(input('Enter a guess number: '))

def guess_number()->str:
    COMPUTER = rd.randint(MIN,MAX)
    PLAYER = inputs()
    print(f"COMPUTER = {COMPUTER}")
    print(f"PLAYER = {PLAYER}")

    if COMPUTER > PLAYER:
        return f"{COMPUTER} is Higher Than {PLAYER}"
    elif COMPUTER < PLAYER:
        return f"{COMPUTER} is Less Than {PLAYER}"
    else:
        return f"{COMPUTER} is Equal {PLAYER}"

print("Welcome to Guess Number Game!")
print(guess_number())'''

# Class
#print(type({'Name':'Kel', 'age':22}))
#print(type(2.3))
#print(type(float))
class Person:
    instance_count = 0
    def __init__(self, name, age) -> None:
        Person.increment_instance_count()
        self.__name, self.__age = name, age

    def __str__(self) -> str:
        return f"{self.__name} is {str(self.__age)}"

    def getName(self)->str:
        return self.__name
    
    def getAge(self)->int:
        return self.__age
    
    def setName(self, name)->None:
        self.__name = name

    def setAge(self, age)->None:
        self.__age = age

    def birthday(self)->None:
        print(f'Happy birthday you were {self.getAge()}')
        self.setAge(self.getAge() + 1)
        print(f'You are now {self.getAge()}')
    
    def is_teenager(self)->bool:
        return self.getAge() < 20

    def calculate_pay(self, hours_worked)->float:
        rate_of_pay = 7.50
        if self.getAge() >= 21:
            rate_of_pay += 2.50
        return hours_worked * rate_of_pay
    
    # Decorators, classa methods
    #Instance methods define the behaviour of the instance or object.
    #Class methods define the behaviour of the class.
    @classmethod
    def increment_instance_count(cls):
        cls.instance_count += 1
    
    # Static method
    @staticmethod
    def static_function():
        print('Steatic method!')

#p = Person('Kel',22)
'''print(p.getName())
p.setName('Cesar')
print(p.getName())'''
#print(type(p))
#print(id(p))
#px = p
#print(px.getAge())
#print(id(p))
#print(id(px))
'''print(p)
#print(px)
p.birthday()
print(p)
pay = p.calculate_pay(40)
print(f'Pay {p.getName()} {pay}')
print(p.is_teenager())
#del px
#print(px)
print(p.__dict__)
print(p)
print(p.instance_count)
px = Person('Duda',21)
print(p.instance_count)

p.static_function()

class Employee (Person):
    def __init__(self, name, age, id):
        super().__init__(name, age)
        self.id = id
    
    def __str__(self):
        return super().__str__() + ' -id (' + str(self.id) + ')'

    def calculate_pay(self, hours_worked) -> float:
        #return super().calculate_pay(hours_worked)
        rate_of_pay =  7.50
        if self.getAge() >= 21:
            rate_of_pay += 2.50
        return hours_worked * rate_of_pay
    
class SalesPerson(Employee):
    def __init__(self, name, age, id, region, sales):
        super().__init__(name, age, id)
        self.region, self.sales = region, sales
    
    def bonus(self):
        return self.sales * 0.5
    


print('Person')
p = Person('John', 54)
print(p)
print('-'*25)

print('Employee')
e = Employee('Denise', 51, 7468)
print(e)
e.birthday()
print(f'e.calculate_pay(40): {e.calculate_pay(40)}')
print('-'*25)

print('SalesPerson')
s = SalesPerson('Phoebe', 21, 4712, 'UK', 30000.0)
s.birthday()
print(f's.calculate.pay(40): {s.calculate_pay(40)}')
print(f's.bonus(): {s.bonus()}')'''

# Python Proprety
# @property, @<method_name>.setter, @<method_name>.deleter

# Exceptions
# Type of exceptions: ZeroDivisionError, Exception, IndexError, FileNotFoundError
runcalc = lambda x: x / 2
'''try:
    runcalc(6)
except ZeroDivisionError:
    print('oops')

finally:
    print('Always runs')

# Raising an Exception
def function_bang(n):
    if n > 0:
        print('function_bang in ')
    else:
        raise Exception('Bang!')
    #print('function_bang')

function_bang(8)
class DivideByYWhenZeroException(Exception):
    """ Sample Exception class """

def divide(x, y):
    try:
        result = x / y
    except Exception as e:
        raise DivideByYWhenZeroException from e

def main():
    divide(6,0)

main()'''

'''from utils import Shape
s = Shape('rectangle')
print(s)'''
'''# Trabalhar com o sistema
import sys
print(f'sys.version: {sys.version}')
print(f'sys.maxsize: {sys.maxsize}')
print(f'sys.path: {sys.path}')
print(f'sys.plataform: {sys.platform}')

from abc import ABCMeta
class Shape(metaclass = ABCMeta):
    def __init__(self, id) -> None:
        self.id = id

s = Shape(9)
print(s.id)'''

# Decoractor (@)-> decorector's operator 
'''def logger(func):
    def inner(x,y):
        #Without parameters
        #print(f'calling {func.__name__}')
        #func()
        #print(f'called {func.__name__}')
        # With parameters
        print(f'calling {func.__name__} with {x} and {y}')
        func(x,y)
        print(f'called {func.__name__}')
    return inner

@logger
def target():
    print('In target function')
@logger
def my_func(x,y):
    print(x,y)

#t1 = logger(target)
#t1()
my_func(4,5)
#target()'''

'''# Define the decorator functions
def  make_bold(fn):
    def makebold_wrapped():
        return "<b>" + fn() + "</b>"
    return makebold_wrapped

def make_italic(fn):
    def makeitalic_wrapped():
        return "<i>" + fn() + "</i>"
    return makeitalic_wrapped

# Apply decorators to functions hello
@make_bold
@make_italic
def hello():
    return 'hello world'

# Call function hello
print(hello())'''
'''# Class Decorators
def singleton(cls):
    print('In singleton for: ', cls)
    instance = None
    def get_instance():
        nonlocal instance
        if instance is None:
            instance = cls()
        return instance
    return get_instance

@singleton
class Service(object):
    def print_it(self):
        print(self)

@singleton
class Foo(object):
    pass 

print('Starting')
s1 = Service()
print(s1)
s2 = Service()
print(s2)
f1 = Foo()
print(f1)
f2 = Foo()
print(f2)
print('Done')

# filter
data = [1,3,5,2,7,4,10]
print(f'data {data}')
# filter for even numbers using a lambda function
d1 = list(filter(lambda i: i % 2 == 0, data))
print(f'd1: {d1}')

def is_even(i):
    return i % 2 == 0
#filter for even numbers using a named function
d2 = list(filter(is_even, data))
print(f'd2: {d2}')'''
'''
# Using map
l1, l2 = [2,3,5,7], [1,4,6,8]
l3 = list(map(lambda i, j: i*j, l1,l2))
print(l3)
'''
'''
# Using lambda, list and map together to acess atributes of a class
data = [Person('John', 54), Person('Phoebe', 21), Person('Adam', 19)]
ages = list(map(lambda p: p.getAge(), data)) 
print(ages[0])'''

from functools import reduce
data = [1,3,5,2,7,4,10]
result = reduce(lambda total, value: total + value, data)
#print(result)

data1 = [Person('John', 54), Person('Phoebe', 21), Person('Adam', 19)]
total_age = reduce(lambda running_total, person: running_total + person.getAge(), data1, 0)
average_age = total_age // len(data1)
print(f'Average ages: {average_age}')


# Find duplicate number
def findDuplicate(nums):
    tortoise = nums[0]
    here = nums[0]
    while True:
        tortoise = nums[tortoise]
        here = nums[nums[here]]
        if tortoise == here:
            break
    ptr1 = nums[0]
    ptr2 = tortoise
    while ptr1 != ptr2:
        ptr1 = nums[ptr1]
        ptr2 = nums[ptr2]
    
    return ptr1

print(findDuplicate([3,1,3,4,2]))