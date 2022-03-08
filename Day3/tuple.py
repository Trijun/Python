friends=('trijun','3G')
print(type(friends))
temp=list(friends)
print(type(temp))

"""list is changeable meaning you can use attributes like append(), replace()"""
"""tuple is not modifiable"""

##print(friends.slice(2))
##print(friends.replace(1,"MAG"))
##print(friends.pop())
print(friends.count('trijun'))
print(friends.index('trijun'))
##print(friends.clear())
##print(friends.update("trijun"))

friends_list=("frost","jack")
print(friends+friends_list)
