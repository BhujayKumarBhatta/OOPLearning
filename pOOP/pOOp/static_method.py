'''
Created on 02-Oct-2018

@author: Bhujay K Bhatta
'''

'''
Static methods are a special case of methods.
 Sometimes, you'll write code that belongs to
  a class, but that doesn't use the object itself at all.
   For example:
'''


class Pizza(object):
    @staticmethod
    def mix_ingradients(x, y):
        return x + y
    # Static method without self means not dependent
    # the state of the object

    def cook(self):
        return self.mix_ingradients(self.cheese, self.vegetables)


'''
In such a case, writing mix_ingredients as a non-static method would work too,
 but it would provide it with a self argument that would not be used. Here,
  the decorator @staticmethod buys us several things:
Python doesn't have to instantiate a bound-method for each Pizza
 object we instantiate. Bound methods are objects too,
  and creating them has a cost. Having a static method avoids that:
>>> Pizza().cook is Pizza().cook
False
>>> Pizza().mix_ingredients is Pizza.mix_ingredients
True
>>> Pizza().mix_ingredients is Pizza().mix_ingredients
True
It eases the readability of the code: seeing @staticmethod
, we know that the method does not depend on the state of the object itself;

It allows us to override the mix_ingredients method in a subclass.
 If we used a function mix_ingredients defined at the top-level of our module,
  a class inheriting from Pizza wouldn't be able to change the way we mix
  ingredients
  for our pizza without overriding cook itself.
'''
