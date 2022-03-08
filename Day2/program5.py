""" Convert M.Trijun to Trijun.M """

input_string=input("enter your name")
output=""
if("." in input_string):
    name = input_string.split(".")
    length = len(name)
output+=name[length-1]
for x in range(length-1):
    output+="."
    output+=name[x]
print (output)
    
