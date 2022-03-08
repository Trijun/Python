#try and except

try:
    a = int(input("enter a"))
    b = int(input("enter b"))
    c = a/b
    print("a/b = %d" %c)
except:
    print("Division by zero is not possible")
else:
    print("hi I am else block")

#try and finally
    
try:
    file = open("hi.txt","r")
finally:
    file.close()
    print("file closed")

#try and create own exception messages
while(True):
    try:
        a=int(input("Input first nummber:"))
        b=int(input("Input second number:"))
        if a<=0 or b<0:
            raise Exception("Negative values not allowed! Try again")
        c = a/b
        print("Div is %d" %c)
        break
    except ValueError:
        print("please input integers only! Try again")
    except ZeroDivisionError:
        print("please input non-zero denominator")
