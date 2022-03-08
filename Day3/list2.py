list=[]
length=int(input("how many items do you need in the list"))
for i in range(length):
    list.append(input("Enter item number "+str(i)))   #append()
for i in list:
    print(i)
