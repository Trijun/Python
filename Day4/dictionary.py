data = {'name':'Trijun','age':23,'occ':'freelancer'}
data['name']= '3G'
data.update({"age":20})
data.pop("occ")
for x in data:
    print (data[x])

temp = data.keys()
temp1= data.values()
print(temp)
print(temp1)
