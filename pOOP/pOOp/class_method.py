

class Pizza(object):
    radius = 42

    @classmethod
    def get_radius(cls):
        return cls.radius


'''
Class methods are methods that are
not bound to an object, but to a class

>>> Pizza.get_radius
<bound method type.get_radius of <class '__main__.Pizza'>>
>>> Pizza().get_radius
<bound method type.get_radius of <class '__main__.Pizza'>>
>>> Pizza.get_radius == Pizza().get_radius
True
>>> Pizza.get_radius()
42
'''


class Date(object):

    # instance method
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    # mandatory argument cls, to the class itself
    '''
    cls is an object that holds the class itself, not an instance of
    the class. It's pretty cool because if we inherit our Date class,
    all children will have from_string defined also.

    from_string is used as a Factory to create Date objects from otherwise
    unacceptable parameters.
    '''
    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    # no obligatory argument, just a function
    '''
    We have a date string that we want to validate somehow.
    This task is also logically bound to the Date class we've
    used so far, but doesn't require instantiation of it.
    '''
    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999


'''
date2 = Date.from_string('11-09-2012')
is_date = Date.is_date_valid('11-09-2012')


Though classmethod and staticmethod are quite similar, there's a
slight difference  in usage for both entities: classmethod
musthave a reference to a class object as the first parameter,
whereas staticmethod can have no parameters at all.
Example
class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

date2 = Date.from_string('11-09-2012')
is_date = Date.is_date_valid('11-09-2012')
Explanation
Let's assume an example of a class, dealing with date
information (this will be our boilerplate):
class Date(object):

    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year
This class obviously could be used to store information about
 certain dates (without timezone information; let's assume all
  dates are presented in UTC).
Here we have __init__, a typical initializer of Python class
 instances, which receives arguments as a typical instancemethod,
  having the first non-optional argument (self) that holds a
  reference to a newly created instance.
Class Method
We have some tasks that can be nicely done using classmethods.
Let's assume that we want to create a lot of Date class instances
 having date information coming from an outer source encoded as
  a string with format 'dd-mm-yyyy'. Suppose we have to do this
   in different places in the source code of our project.
So what we must do here is:

Parse a string to receive day, month and year as three integer
 variables or a 3-item tuple consisting of that variable.
Instantiate Date by passing those values to the initialization call.
This will look like:
day, month, year = map(int, string_date.split('-'))
date1 = Date(day, month, year)
For this purpose, C++ can implement such a feature with overloading,
 but Python lacks this overloading. Instead, we can use classmethod.
  Let's create another "constructor".
    @classmethod
    def from_string(cls, date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        date1 = cls(day, month, year)
        return date1

date2 = Date.from_string('11-09-2012')
Let's look more carefully at the above implementation, and
 review what advantages we have here:
We've implemented date string parsing in one place and it's reusable now.
Encapsulation works fine here (if you think that you could implement
 string parsing as a single function elsewhere, this solution fits
  the OOP paradigm far better).
cls is an object that holds the class itself, not an instance of the class.
 It's pretty cool because if we inherit our Date class, all children will
  have from_string defined also.

Static method
What about staticmethod? It's pretty similar to classmethod but doesn't take
 any obligatory parameters (like a class method or instance method does).
Let's look at the next use case.
We have a date string that we want to validate somehow. This task is also
 logically bound to the Date class we've used so far, but doesn't require
  instantiation of it.
Here is where staticmethod can be useful. Let's look at the next piece of code:
    @staticmethod
    def is_date_valid(date_as_string):
        day, month, year = map(int, date_as_string.split('-'))
        return day <= 31 and month <= 12 and year <= 3999

    # usage:
    is_date = Date.is_date_valid('11-09-2012')
So, as we can see from usage of staticmethod, we don't have any access to
 what the class is---it's basically just a function, called syntactically
  like a method, but without access to the object and its internals (fields
   and another methods), while classmethod does.
'''


class Hero:


    @staticmethod
    def say_hello():
        print("Helllo...")

  @classmethod
  def say_class_hello(cls):
     if(cls.__name__=="HeroSon"):
        print("Hi Kido")
     elif(cls.__name__=="HeroDaughter"):
        print("Hi Princess")

class HeroSon(Hero):
  def say_son_hello(self):
     print("test  hello")



class HeroDaughter(Hero):
  def say_daughter_hello(self):
     print("test  hello daughter")


testson = HeroSon()

testson.say_class_hello() #Output: "Hi Kido"

testson.say_hello() #Outputs: "Helllo..."

testdaughter = HeroDaughter()

testdaughter.say_class_hello() #Outputs: "Hi Princess"

testdaughter.say_hello() #Outputs: "Helllo..."




Let's explore it with an example:
class PythonBook:
    def __init__(self, name, author):
        self.name = name
        self.author = author
    def __repr__(self):
        return f'Book: {self.name}, Author: {self.author}'
Without a @classmethod,you should labor to creat instances one by one and they are scartted.
book1 = PythonBook('Learning Python', 'Mark Lutz')
In [20]: book1
Out[20]: Book: Learning Python, Author: Mark Lutz
book2 = PythonBook('Python Think', 'Allen B Dowey')
In [22]: book2
Out[22]: Book: Python Think, Author: Allen B Dowey
As for example with @classmethod
class PythonBook:
    def __init__(self, name, author):
        self.name = name
        self.author = author
    def __repr__(self):
        return f'Book: {self.name}, Author: {self.author}'
    @classmethod
    def book1(cls):
        return cls('Learning Python', 'Mark Lutz')
    @classmethod
    def book2(cls):
        return cls('Python Think', 'Allen B Dowey')
Test it:
In [31]: PythonBook.book1()
Out[31]: Book: Learning Python, Author: Mark Lutz
In [32]: PythonBook.book2()
Out[32]: Book: Python Think, Author: Allen B Dowey
See? Instances are successfully created inside a class definition and they are collected together.
In conclusion, @classmethod decorator convert a conventional method to a factory method

