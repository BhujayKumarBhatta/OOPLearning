'''
Created on 28-Nov-2018

@author: Bhujay K Bhatta

Data Encapsulation is seen as the bundling of data with the
methods that operate on that data. Information hiding on the
other hand is the principle that some internal information or
data is "hidden", so that it can't be accidentally changed

Abstraction = Data Encapsulation + Data Hiding

Encapsulation is often accomplished by providing two kinds of
methods for attributes: The methods for retrieving or accessing the
values of attributes are called getter methods. Getter methods do not
change the values of attributes, they just return the values.
The methods used for changing the values of attributes are called setter
methods.
'''


class Robot(object):
    '''
    classdocs
    '''

    def __init__(self, name=None, color=None):
        # Private attributes __name can only be accessed from within the class
        self.__name = name
        # restricted attributes for internal usage
        self._life = "my life is eternal"
        # public attributes for usage outside the class
        self.color = color

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name


y = Robot()
print("Using encapsulated setter method to access"
      " data of private attribute __name")
y.set_name('Mavin')
print("Using encapsulated getter method to access data"
      " data of private attribute __name = %s " % y.get_name())

print("Using restricted attributes _life %s" % y._life)
x = Robot('Calvin')
# Direct aceess of private attributes are not allowed here
print("Using direct access to  private name attribute __name is"
      " not allowed  and will fail")
print (x.__name)
