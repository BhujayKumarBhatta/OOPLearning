class Robot:
    pass


# instance
x = Robot()



# instance attributres
x.name = 'Marvin'
x.age = 2

print("Name of the robot is %s and age is %s" % (x.name, x.age))

print(x.__dict__)

# Attributes can be bound to class names as well , these are class atributes
Robot.metal = 'steel'
y = Robot()
# If you try to access y.brand, Python checks first, if "brand" is a key of the y.__dict__ dictionary. If it is not, Python checks, if "brand" is a key of the Robot.__dict__. If so, the value can be retrieved. 

print(y.metal)
print(Robot.__dict__)

e = getattr(y, 'energy', 100)
print(e)


# Example of class attributes
class IdealRobot:

    Three_Laws = (
"""A robot may not injure a human being or, through inaction, allow a human being to come to harm.""",
"""A robot must obey the orders given to it by human beings, except where such orders would conflict with the First Law.,""",
"""A robot must protect its own existence as long as such protection does not conflict with the First or Second Law."""
)

    def __init__(self, name, build_year):
        self.name = name
        self.build_year = build_year



for number, text in enumerate(IdealRobot.Three_Laws):
    print(str(number+1) + ":\n" + text) 




