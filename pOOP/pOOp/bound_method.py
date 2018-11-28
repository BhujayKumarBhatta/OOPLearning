'''
Created on 02-Oct-2018

@author: Bhujay K Bhatta
'''


class Pizza(object):
    def __init__(self, size):
        self.size = size

    def get_size(self):
        return self.size


'''
if __name__ == "__main":
    Pizza.get_size
    Pizza.get_size(Pizza(42))
'''

#################################
'''
>>> import clsmethods
>>> from clsmethods import Pizza
>>> Pizza.get_size
<unbound method Pizza.get_size>
>>> Pizza.get_size()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unbound method get_size() must be called
with Pizza instance as first argument (got nothing instead)
>>> Pizza.get_size(Pizza(42))
42

what Python does for us, is that it binds all the methods
 from the class Pizza to any instance of this class.
 This means that the attribute get_size of an instance of
  Pizza is a bound method: a method for which the first
  argument will be the instance itself.
>>> Pizza(42).get_size
<bound method Pizza.get_size of <clsmethods.Pizza object
at 0x0000000002BCAE80>>
>>> Pizza(42).get_size()
42
>>>
As expected, we don't have to provide any argument to get_size,
since it's bound, its self argument is automatically
 set to our Pizza instance
>>> m = Pizza(42).get_size
>>> m()
>>> m.__self__
<clsmethods.Pizza object at 0x0000000002BCAE80>

In Python 3, the functions attached to a class are not
 considered as unbound method anymore, but as simple functions,
 that are bound to an object if required. So the principle
  stays the same, the model is just simplified.

'''
