actor=["Trijun","Dulqar","SZ","Surya"]

"""Normal way of accessing items in list"""
for x in actor:
    print(x)

"""accessing list items using list comprehension"""
[print(x) for x in actor]


items=[]
for x in actor:
    if "u" in x:
        items.append(x)
print(items)


items1=[]
items1.append([x for x in actor if "u" in x])
print(items1)

"""in list comprenhension you will get the output as a list so dont use append to insert into in another list"""

items1=[]
items1=[x for x in actor if "u" in x]
print(items1)        


new=[]
new=["ak" if "surya" not in x else x for x in actor ]
print(new)

"""when you use if else in list comprehension, always remember to put the if else condition first before for condition"""

actor.sort()
print(actor)
"""destructive function"""

actor.sort(reverse=True)
print(actor.count())

