menu={'name_value':[],'price_value':[],'quantity_value':[]}
#add items in menu

length = int(input("Enter the number of items in menu"))

#for storing different values in the key, you need to first access the list in the dictionary so we are storing the list in a temporary variable which in this case is name_value_list

name_value_list = menu['name_value']
price_value_list = menu['price_value']
quantity_value_list = menu['quantity_value']

for item in range(length):

    name_value_list.append(input(("What is today's special item {}?").format(str(item+1))))
   
    price_value_list.append(input(("what is the price of {}?").format(name_value_list[item])))

    quantity_value_list.append(input(("how much of {} is present?").format(name_value_list[item])))

#fianlly after storing all the different values in each list, we need to update the key in the dictionary with the list

#update menu
def update_menu(name_value_list,price_value_list,quantity_value_list):
    menu['name_value'] = name_value_list
    menu['price_value'] =  price_value_list
    menu['quantity_value'] = quantity_value_list

update_menu(name_value_list,price_value_list,quantity_value_list)

option="1"
option_list=["1","2","3"]


while(option in option_list):
    print(" Enter \n 1 for removing item in menu,\n 2 for displaying menu,\n 3 for taking order")
    option=input("enter your option")

    item_list = menu['name_value']
    value_list = menu['price_value']
    quantity_list = menu['quantity_value']

    length_new=len(item_list)

    #display menu
    def display_menu():
        print("\n\t\t CAFE PONDY \nITEM   \tPRICE     QTY\t\n")
        for i in range(length_new):
            print(("{0} : {1} : \t{2}\n").format(item_list[i],value_list[i],quantity_list[i]))
    
    #remove item 
    def remove_item_automatic(remove_item):
            item_index=item_list.index(remove_item)
            item_list.remove(item_list[item_index])
            value_list.remove(value_list[item_index])
            quantity_list.remove(quantity_list[item_index])

    #remove item from menu
    def remove_item():
        remove_item=input("what item do you want to remove")
        if remove_item in item_list:
            remove_item_automatic(remove_item)
        else:
            print("item isn't available in menu")
    
    if option in "1":
        remove_item()     
        
    if option in "2":
        display_menu()
        
    if option in "3":
        #take order
        user_item=input("what do you want to order?")
        if user_item in item_list:
            user_item_count=int(input(("how many {} do you want?").format(user_item)))
            item_index=item_list.index(user_item)
            if (user_item_count <= int(quantity_list[item_index])):
                bill=user_item_count*int(value_list[item_index])
                print("\nYour bill is $"+str(bill)+"\n")
                quantity_list[item_index]=int(quantity_list[item_index])-user_item_count
                if(quantity_list[item_index]==0):
                    remove_item_automatic(user_item)
                    update_menu(item_list,value_list,quantity_list)
                
            else:
                remaining=user_item_count-int(quantity_list[item_index])
                if remaining==0:
                    print("item is finished")
                    
                else:
                    print(("sorry, we only have {1} {0}").format(item_list[item_index],int(quantity_list[item_index])))

            
    if option not in option_list:
        print("invalid option, sorry")
