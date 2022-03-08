canteen={'item':[],'quantity':[]}
for x in range(2):
    temp=input()
    temp1=input()
    temp2=canteen['item']
    temp2.append(temp)
    temp3=canteen['quantity']
    temp3.append(temp1)
canteen['item']=temp2
canteen['quantity']=temp3

print(canteen)
    
