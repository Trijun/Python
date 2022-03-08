canteen=("ice cream","fruity","bonda","kitkat")

#1st method

output=canteen[0]
for i in range(1,len(canteen),1):
    output+=","
    output+=canteen[i]
print(output)


#2nd method

temp=""
for x in range(0,len(canteen)):
    temp+=canteen[x]
    if(len(canteen)-1>x):
        temp+=","
print(temp)

