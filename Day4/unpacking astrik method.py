dept=("Trijun","3G","Frost","junie")

##x,y,z = dept
##
##print(x)
##print(y)
##print(z)

"""It will say too many values to unpack since there are only three variables but the list has four elements"""

a,b,*c = dept
print(a)
print(b)
print(c)

""" putting astrik  before a variable will create a list and store the remaining elements in the string which  can help overcome the problem faced before"""


a,*b,c = dept
print(a)
print(b)
print(c)
