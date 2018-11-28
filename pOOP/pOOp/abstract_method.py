'''
Created on 02-Oct-2018

@author: Bhujay K Bhatta
'''


'''
Abstract methods
An abstract method is a method defined in a base class,
but that may not provide any implementation. In Java,
it would describe the methods of an interface.
So the simplest way to write an abstract method in Python is:
'''


class Pizza(object):

    def get_radius(self):
        raise NotImplementedError


'''
Any class inheriting from Pizza should implement and override
the get_radius method, otherwise an exception would be raised.
This particular way of implementing abstract method has a drawback.
If you write a class that inherits from Pizza and forget to
implement get_radius, the error will only be raised when you'll
try to use that method.
>>> Pizza()
<__main__.Pizza object at 0x7fb747353d90>
>>> Pizza().get_radius()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in get_radius
NotImplementedError
There's a way to trigger this way earlier, when the object is
being instantiated, using the abc module that's provided with Python.
'''
import abc


class BasePizza(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_radius(self):
        """Method that should do something."""


'''
Using abc and its special class, as soon as you'll try to instantiate
 BasePizza or any class inheriting from it, you'll get a TypeError.
>>> BasePizza()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class BasePizza with abstract
 methods get_radius

Keep in mind that declaring a method as being abstract,
 doesn't freeze the prototype of that method. That means that
  it must be implemented, but it can be implemented with any
  argument list.
'''

import abc

class BasePizza(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_ingredients(self):
        """Returns the ingredient list."""

class Calzone(BasePizza):
    def get_ingredients(self, with_egg=False):
        egg = Egg() if with_egg else None
        return self.ingredients + egg


'''
This is valid, since Calzone fulfills the interface requirement
 we defined for BasePizza objects. That means that we could also
 implement it as being a class or a static method, for example:


Therefore, you can't force an implementation of your abstract
 method to be a regular, class or static method, and arguably
 you shouldn't. Starting with Python 3 (this won't work as you
 would expect in Python 2, see issue5867), it's now possible to
  use the @staticmethod and @classmethod decorators on top
   of @abstractmethod:

'''
import abc


class BasePizza(object):
    __metaclass__ = abc.ABCMeta

    ingredient = ['cheese']

    @classmethod
    @abc.abstractmethod
    def get_ingredients(cls):
        """Returns the ingredient list."""
        return cls.ingredients


'''
Don't misread this: if you think this is going to force your
subclasses to implement get_ingredients as a class method
 you are wrong. This simply implies that your implementation
  of get_ingredients in the BasePizza class is a class method.
An implementation in an abstract method? Yes! In Python, contrary
 to methods in Java interfaces, you can have code in your abstract
  methods and call it via super():
'''

import abc

class BasePizza(object):
    __metaclass__  = abc.ABCMeta

    default_ingredients = ['cheese']

    @classmethod
    @abc.abstractmethod
    def get_ingredients(cls):
         """Returns the ingredient list."""
         return cls.default_ingredients

class DietPizza(BasePizza):
    def get_ingredients(self):
        return ['egg'] + super(DietPizza, self).get_ingredients()
In such a case, every pizza you will build by inheriting from BasePizza will have to override the get_ingredients method, but will be able to use the default mechanism to get the ingredient list by using super().


