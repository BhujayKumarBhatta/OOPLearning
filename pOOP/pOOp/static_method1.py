'''
Created on 28-Nov-2018

@author: Bhujay K Bhatta


'''


class C:
    counter = 0

    def __init__(self):
        type(self).counter += 1

    def __del__(self):
        type(self).counter -= 1


x = C()
print("Number of instances: : " + str(C.counter))
y = C()
print("Number of instances: : " + str(C.counter))
del x
print("Number of instances: : " + str(C.counter))
del y
print("Number of instances: : " + str(C.counter))

'''
Principially, we could have written C.counter instead of type(self).counter,
because type(self) will be evaluated to "C" anyway. But we will see later,
that type(self) makes sense, if we use such a class as a superclass.

If we start the previous program, we will get the following results:
Number of instances: : 1
Number of instances: : 2
Number of instances: : 1
Number of instances: : 0

We used class attributes as public attributes in the previous section.
Of course, we can make public attributes private as well. We can do this
by adding the double underscore again. If we do so, we need a possibility
 to access and change these private class attributes. We could use instance
 methods for this purpose:
'''


class Robot:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    def RobotInstances(self):
        return Robot.__counter


x = Robot()
print(x.RobotInstances())
y = Robot()
print(x.RobotInstances())
'''
This is not a good idea for two reasons: First of all, because the number
of robots has nothing to do with a single robot instance and secondly
because we can't inquire the number of robots before we haven't created an
instance.
If we try to invoke the method with the class name Robot.RobotInstances(),
we get an error message, because it needs an instance as an argument:
>>> Robot.RobotInstances()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: RobotInstances() takes exactly 1 argument (0 given)
'''


class RobotN:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    def RobotInstances():
        return RobotN.__counter


print("access the private class attribute using method RobotInstances()"
      "but without the 'self' parameters , the value returned is % s"
      % RobotN.RobotInstances())
'''
but we can't call it via an instance:

>>> x = Robot()
>>> x.RobotInstances()
Traceback (most recent call last):

  File "<stdin>", line 1, in <module>
TypeError: RobotInstances() takes no arguments (1 given)
>>>

The call "x.RobotInstances()" is treated as an instance
 method call and an instance method needs a reference to
  the instance as the first parameter.

So, what do we want?

We want a method, which we can call
via the class name or via the instance name without the
necessity of passing a reference to an instance to it.

The solution consists in static methods, which don't need a
reference to an instance.
It's easy to turn a method into a static method. All we have
 to do is to add a line with "@staticmethod" directly in front
  of the method header. It's the decorator syntax.

You can see in the following example that we can now use
our method RobotInstances the way we wanted:
'''


class RobotA:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    @staticmethod
    def RobotInstances():
        return RobotA.__counter


print(RobotA.RobotInstances())
x = RobotA()
print(x.RobotInstances())
y = RobotA()
print(x.RobotInstances())
print(RobotA.RobotInstances())

'''
Static methods shouldn't be confused with class methods. Like static methods class methods are not bound to instances, but unlike static methods class methods are bound to a class. The first parameter of a class method is a reference to a class, i.e. a class object. They can be called via an instance or the class name. 

'''


class RobotC:
    __counter = 0

    def __init__(self):
        type(self).__counter += 1

    @classmethod
    def RobotInstances(cls):
        return cls, RobotC.__counter


print(RobotC.RobotInstances())
x = RobotC()
print(x.RobotInstances())
y = RobotC()
print(x.RobotInstances())
print(RobotC.RobotInstances())

'''
$ python3 static_methods4.py
<class '__main__.Robot'>, 0)
<class '__main__.Robot'>, 1)
<class '__main__.Robot'>, 2)
<class '__main__.Robot'>, 2)
The use cases of class methods:

1. the are used in the definition of the so-called factory methods,
 which we will not cover here.

2. They are often used, where we have static methods, which have to
call other static methods. To do this, we would have to hard code
 the class name, if we had to use static methods. This is a problem,
  if we are in a use case, where we have inherited classes.


The following program contains a fraction class, which is still not
 complete. If you work with fractions, you need to be capable of reducing
 fractions, e.g. the fraction 8/24 can be reduced to 1/3. We can reduce a
 fraction to lowest terms by dividing both the numerator and denominator by
 the Greatest Common Divisor (GCD).

We have defined a static gcd function to calculate the greatest common
divisor of two numbers. the greatest common divisor (gcd) of two or more
integers (at least one of which is not zero), is the largest positive integer
that divides the numbers without a remainder. For example, the 'GCD of 8
and 24 is 8.
The static method "gcd" is called by our class method "reduce"
with "cls.gcd(n1, n2)". "CLS" is a reference to "fraction".

'''


class fraction(object):

    def __init__(self, n, d):
        '''
        # calling reduce class method without self parameter
        since class method already has a refernece to class
        '''
        self.numerator, self.denominator = fraction.reduce(n, d)

    @staticmethod
    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    @classmethod
    def reduce(cls, n1, n2):
        '''
        calling static method gcd with self parameter
        '''
        g = cls.gcd(n1, n2)
        return (n1 // g, n2 // g)

    def __str__(self):
        return str(self.numerator)+'/'+str(self.denominator)


x = fraction(8, 24)
print(x)


'''
We will demonstrate in our last example the usefulness of class methods in inheritance. We define a class "Pets" with a method "about". This class will be inherited in a subclass "Dogs" and "Cats". The method "about" will be inherited as well. We will define the method "about" as a "staticmethod" in our first implementation to show the disadvantage of this approach: 
'''
class Pets:
    name = "pet animals"

    @staticmethod
    def about():
        print("This class is about {}!".format(Pets.name))   
    

class Dogs(Pets):
    name = "'man's best friends' (Frederick II)"

class Cats(Pets):
    name = "cats"

p = Pets()
p.about()
d = Dogs()
d.about()
c = Cats()
c.about()

'''
We get the following output: 

This class is about pet animals!
This class is about pet animals!
This class is about pet animals!
Especially, in the case of c.about() and d.about(), we would have preferred a more specific phrase! The "problem" is that the method "about" doesn't know that it has been called by an instance of the Dogs or Cats class. 
We decorate it now with a classmethod decorator instead of a staticmethod decorator: 

'''
class Pets:
    name = "pet animals"

    @classmethod
    def about(cls):
        print("This class is about {}!".format(cls.name))
    
class Dogs(Pets):
    name = "'man's best friends' (Frederick II)"

class Cats(Pets):
    name = "cats"

p = Pets()
p.about()

d = Dogs()
d.about()

c = Cats()
c.about()

''''
This class is about pet animals!
This class is about 'man's best friends' (Frederick II)!
This class is about cats!
'''

