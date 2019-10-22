#! python3

# Class -> mechisnism to group data & its associated operations
# x = str() also = x = ""
# x = str() creating an object from a class. This = a constructor
# instantiation -> creating an object from a class
# classes are a maniquen and you add methods/attributes to make it different
# classes have methods and atributes/properties/props
#             functions                variables

# inheritance: 
# Class Mammal -> hair, milk for babes, warm blood, live birth
# inherit
# Class Dog(Mammal) -> Short & stubby, barks, good nose, better than a cat.
# inherit
# Class Cat(Mammal) -> mean
# Class weird-ass-thing() -> cloaca, venomous, webbed feet, bill, claws
# mix
# Class palatypus( Mammal, weird-ass-thing)

#example of initializer
# import math
# class Point:
#     # Initializer
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y

#     def __repr__(self):
#         return f"{self.x}, {self.y}"

#     def distance(self,p):
#         dx = self.x - p.x
#         dy = self.y = p.y
#         return math.sqrt((dx * dx) + (dy * dy))

# p1 = Point(5,2)
# p2 = Point(8,4)
# dist = p1.distance(p2)
# print(p1==p2)
# points = [p1, p2]
# for p in points:
#     print(p)