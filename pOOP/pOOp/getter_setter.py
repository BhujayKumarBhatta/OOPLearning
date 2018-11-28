'''
Created on 28-Nov-2018

@author: Bhujay K Bhatta
'''


class Robot(object):
    '''
    classdocs
    '''

    def __init__(self, name=None):
        self.name = name

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name


# Direct aceess of attributes are allowed here
x = Robot('Calvin')
print('Using direct access to name attribute %s' % x.name)

y = Robot()
print("Using encapsulated setter method to access data")
y.set_name('Mavin')
print("Using encapsulated getter method to access data %s " % y.get_name())
