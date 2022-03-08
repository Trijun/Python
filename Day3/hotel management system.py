menu=[]
price=[]
#add items in menu

length = int(input("Enter the number of items in menu"))

for item in range(length):
    menu.append(input(("What is today's special item {}?").format(str(item+1))))
    price.append(input(("what is the price of {}?").format(menu[item])))


option="1"
option_list=["1","2","3"]
while(option in option_list):
    print(" Enter \n 1 for removing item in menu,\n 2 for displaying menu,\n 3 for taking order")
    option=input("enter your option")
    
    if option in "1":
        #remove item from menu
        remove_item=input("what item do you want to remove")
        if remove_item in menu:
            menu.remove(remove_item)
        else:
            print("item isnt available in menu")
        print (menu)
        
    if option in "2":
        #display menu
        print("\n\t\t CAFE PONDY \nITEM   PRICE\t\n")
        for i in range(length):
            print(("{0} : {1}\n").format(menu[i],price[i]))
        
    if option in "3":
        #take order
        user_item=input("what do you want to order?")
        if user_item in menu:
            user_item_count=int(input(("how many {} do you want?").format(user_item)))
            item_index=menu.index(user_item)
            bill=user_item_count*int(price[item_index])
            print("Your bill is $"+str(bill))
            
    if option not in option_list:
        print("invalid option, sorry")
        


