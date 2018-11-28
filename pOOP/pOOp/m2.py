'''
Created on 23-Feb-2018

@author: Bhujay K Bhatta
'''
class X(object):
    pass
X.__class__
X.__dict__


dir(X)

ins1 = X()
ins2 = X()
ins1.someNumber = 2*3
print ins1.someNumber


class Behave(object):
    def __init__(self, name):
      self.name = name
    
    def once(self):
        print "Hello,", self.name
        
    def rename(self, newName):
        self.name = newName
        
    def repeat(self, N):
      for i in range(N): self.once( )

beehive = Behave("Queen Bee")
beehive.repeat(3)
beehive.rename("Stinger")
beehive.once( )
print beehive.name
beehive.name = 'See, you can rebind it "from the outside" too, if you want'
beehive.repeat(2)

#signature-based-polymorphism
# repeat method with same name and argument ( same signature ) but 
#differenet implementaion in Repeater , aMIx is a mix if them  
# repeat method applies to all the mix 

class Repeater(object):
    def repeat(self,N):
        print N*"**"

aMix = beehive, Behave("john"), Repeater(), Behave('world')
for w in aMix: w.repeat(3)

#inheritance and ovverride , template Method  Design pattern  
class Subclass(Behave):
  def once(self): print '(%s)' % self.name
# only once  method behavior has changed but others remained same  
subInstance = Subclass("Queen Bee")
subInstance.repeat(3)  
subInstance.once()
subInstance.rename("Best Bee")
print subInstance.name

"""
Delegation involves implementing
some functionality by letting another existing piece of code do most of the work,
often with some slight variation
"""
class OneMore(Behave):
    def repeat(self, N): 
        Behave.repeat(self, N+1)
# delegating some work of the method to super class Classname.method(self,..)
  
zealant = OneMore("Worker Bee")
zealant.repeat(3)

# instead of  Classname.method use super facilitate multiple inhertance
class OneMore1(Behave):
    def repeat(self, N): 
        super(OneMore, self).repeat(N+1)

#Instead of explicitly having all your
#classes inherit from object,an equivalent alternative is to add the following assignment
#statement close to the start of every module that defines any classes

#__metaclass__ = type


class Temperature(object):
    coefficients = {'c': (1.0, 0.0, -273.15), 'f': (1.8, -273.15, 32.0),
                  'r': (1.8, 0.0, 0.0)}
    def __init__(self, **kwargs):
# default to absolute (Kelvin) 0, but allow one named argument,
# with name being k, c, f or r, to use any of the scales
        try:
            name, value = kwargs.popitem()
        except KeyError:
# no arguments, so default to k=0
            name, value = 'k', 0  
    # error if there are more arguments, or the arg's name is unknown
        if kwargs or name not in 'kcfr':
                kwargs[name] = value # put it back for diagnosis
                raise TypeError, 'invalid arguments %r' % kwargs
        setattr(self, name, float(value))
        
    def __getattr__(self, name):
# maps getting of c, f, r, to computation from k
        try:
            eq = self.coefficients[name]
        except KeyError:
# unknown name, give error message
            raise AttributeError, name
        return (self.k + eq[1]) * eq[0] + eq[2]
        
    def __setattr__(self, name, value):
# maps settings of k, c, f, r, to setting of k; forbids others
        if name in self.coefficients:
# name is c, f or r -- compute and set k
                eq = self.coefficients[name]
                self.k = (value - eq[2]) / eq[0] - eq[1]
        elif name == 'k':
# name is k, just set it
            object.__setattr__(self, name, value)
        else:
# unknown name, give error message
            raise AttributeError, name
    def __str__(self):
# readable, concise representation as string
        return "%s K" % self.k
    def __repr__(self):
# detailed, precise representation as string
        return "Temperature(k=%r)" % self.k

t = Temperature(f=100)
print t.k
