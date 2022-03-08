class cse:
    def create_section(x):
        students=x
        print("created")

section_a = cse.create_section(45)



##class abc:

##    book_name=""
##
##    def inputing(name):
##        book_name=name
##        
##    def accessing(self):
##        print("Accessing the data memeber of the other function:"+book_name)
##
##b2= abc()
##b2.inputing("harry")
##b2.accessing()


"""The above code wont work since the data members declared in a class cant be directly accessed by other functions,
so we need to inherit the class's data members to the member functions, which is done by the keyword self in the below program"""


print("\n")


"""self is a keyword that help you access data members of other member functions"""
class lib:
    def __init__(self,a,b):
        self.book_name = a
        self.author = b

    #the above part is almost similar to constructor but it is a default function that is called when we pass arguments in the class name
        
    def accessing(self):
        print("Accessing the data memeber of the other function:"+self.book_name)


b1 = lib("harry","jk")

print(b1.accessing())

print("\n")

"""difference between these two lines below is that the first line will show none as output
since we are printing the function, which means printing the thing that the function returns.

since there is no return in the function, it returns none and that is what it is printing"""


b1.accessing()

print("\n")

