

"""Types of functions in Python"""

##empty

def wishe():
    print("goodmorning")

wishe()

##arguments

def wishe(person):
    print("goodmorning"+person)

wishe("trijun")

##multiple args
def wishe(person1, person2):
    print("goodmorning "+person1+person2)

wishe()

##arbitary - will save as tuple in function

def wishe(*person):
    print("goodmorning "+person[0])

wishe()

##keyword - directly speicifying the value of the argument in function call

def wishe(person):
    print("goodmorning"+person)

wishe(person="trijun")

##arbitary keyword - will save as dictionary 

def wishe(**person):
    print("goodmorning"+person["name"])

wishe(name="trijun")

##default

def wishe(person="trijun"):
    print("goodmorning "+person)

wishe()
wishe('3G')
