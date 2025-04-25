#Restaurant Order System - Assignment 07: The Great Lists Adventure!
"""
This project is a text-based Restaurant Order System built using Python.
It allows the user to view a menu, add items to their order, calculate the total bill,
remove or update items, apply discount offers, randomly suggest an item, filter premium menu items,
and save the order to a text file. It uses core Python concepts such as:
- Lists (including nested lists)
- Loops (while and for)
- Conditional statements (if, elif, else)
- Random module (random.choice)
- List methods (append, pop)
- List comprehension
- File handling (write order to a file)
"""
import random   # import random module for random item suggestion.

# Step 1- Define menu item just like a nested list where each item have a name and price.
menu = [
    ["Biryani half plate 🍽",200],
    ["Biryani full plate 🍽",350],
    ["Burger Shami 🍔",150],
    ["Burger Zinger🍔",250],
    ["Fries🍟", 150],
    ["Small pizza 🍕", 500],
    ["Large pizza 🍕",1000],
    ["Sandwich 🥪", 200],
    ["8 pice Nuggets ",800],
    ["Pasta ice-cream 🍦",120],
    ["cold Drink", 100]
    ]
# Step 2: Create an empty list to store the customer's order.
order_list = []

# Step 3: Display the menu to the user.
def show_menu():
    print("\n***---MENU---***")
    """ This function display the menu of Resturant ,with each item name and price.""" # This is docstring that define the purpose of function.
    for index, item in enumerate(menu):
        # with the help of enumerate function ,iterate in the menu list, so that we could find both index and item 
        
        print(f"{index+1}. {item[0]} - Rs.{item[1]}")  # index+1 is liye kar rahe hain kyunki Python list indexing 0 se hoti hai, lekin menu numbering 1 se dikhani hoti hai.
        #Each Element in a  item itself is a list ,e.g (["burger",200]) ,item[0] is a name and item[1] is a price
        
# Step 4: Add an item to the order_list based on user input.
def add_item():
    """ This function add selected item to the customer order.Ask item number from user and then validate that input ,
    after validation add corresponding item to the order list of customer."""
    show_menu()  # first of all show menu so that user check available items in a menu.
    choice = int(input("Enter the number of the item you want to add:"))-1  #get user choice and adjust them for  0-indexed
    # "Sir, because Python lists start from index 0, but humans count from 1, we subtract 1 from the user's input to align with list indexing."
    
    if 0<=choice< len(menu):  # this condition check choice is a valid index in a menu list.
        order_list.append(menu[choice])  # add selected menu item to order_list.
        print(f"{menu[choice][0]} added to your order")  # tell the user ,which item is added to your order.

        # menu[choice][0] list ke andar nested list ka pehla element access karta hai — yani item ka naam.
    else:
        print("Invalid choice")
		
# Step 5: Remove an item from the current order_list.
def remove_item():
    """This function remove a selcted item from customer order_list.first check current order_list and ask the user to pass
    item number to remove that item ,then validate the user input,finally remove the item from the order_list."""
    if not order_list:
        print("your order_list is empty!")  #check if order list is empty
        return
    print("\nYour current order_list")   #Check current order
    for index,item in enumerate(order_list):  #enumerate() function list ke har element ke sath uska index bhi return karta hai.
        print(f"{index+1}. {item[0]}. -Rs {item[1]}") # check order items with index 
    choice = int(input("Enter the number of the items you want to remove"))-1  # ask the user to pass item number that he want to remove
    if 0<=choice <len(order_list):
        removed =order_list.pop(choice)  #using pop() remove the item and also return the popped item.
        print(f"{removed[0]} removed from your order_list.")  #tell the user which item is removed form order_list
    else:
        print("Invalid Selection") # handle the invalid item number 
		
		
# Step 6: Show the user's full order and total cost with optional discount.
def show_order():
    """ This function show the item in customer order_list and calculate the total cost of that item.
    if total cost is greater than 1000 then apply 10% discount and also ask the user did he want to save the order in a file.
    """
    if not order_list:
        print("Your order is empty")
        return
    print("\n--^^--Your Order Summary--^^--")
    total = 0
    for item in order_list:
        print(f"-{item[0]}. -Rs.{item[1]}")
        total = total+item[1]  # in order_list just add up the prices of item.

        # Store original total before discount
        original_total = total

    if total>1000:
        print("Congratulations!🎊 you got a 10% discount!")
        discount = total * 0.10  # 10% of total
        discounted_total = total - discount
        total =total*0.9 # apply a 10% discount on total cost
        print(f"Discount Amount: Rs. {round(discount)}")
        print(f"Discounted Total: Rs. {round(discounted_total)}")
        print(f"Final Bill       : Rs. {round(discounted_total)}")
        # check final bill amount with rounded in nearest integer.
    else:
        print(f"Final Bill       : Rs. {round(total)}")


# Order confirmation from user
confirmation = input("Confirm your Order? (yes/no)").lower()
if confirmation == "yes":
    print("Your order has been confirmed!")
    # Ask the user to save order in file or not 
    save = input("Do you want to save this order in a file? (yes/no)").lower()
    if save == "yes" :
        save_order_list_to_file(round(total))
    else:
        print("Your Order has been Canceled!")
        order_list.clear()  # clear the order_list
        
    

# Step 7: Randomly suggest an item from the menu.
def suggest_random():
    """ This function suggest the user random item from menu,using random.choice() select a random item for user."""
    suggestion = random.choice(menu)  # select a random item from menu with (name and price list of item)
    print(f"Chef's Recommendation:Try our {suggestion[0]} Only for Rs {suggestion[1]}!")

# Step 8: Show premium menu items using list comprehension.

def show_premium_item():
    """ This function show the premium items whose price is greater than 300 using list comprehension. """

    premium = [item for item in menu if item[1]>300]  # To creat a new list with premium name in which only contains that items whose price >300.
    print("\n****___Premium Items (Price >300)___**** ")
    for item in premium:
        print(f"-{item[0]} -Rs.{item[1]}")  #Check the list of premium item
        
		
# Step 9:Main loop to interact with the user.
while True:
    print("\n---*** WELCOME TO AL-REHMAT FOOD HUB ***---")
    print("1.view Menu")
    print("2.Add item to Order")
    print("3.Remove Item from Order")
    print("4.Show MY Order")
    print("5.Suggest Me Something Random")
    print("6.Show Premium Item")
    print("7.Exit")

    choice = input("Enter your choice number:")  # Take user action choice

    if choice == "1":
        show_menu()  # call function to check a menu
    elif choice == "2":
        add_item()   # call a function to add item in order_list
    elif choice == "3":
        remove_item()  # call a function to remove a item from order_list
    elif choice == "4":
        show_order()  # call a function to see order and total cost of order
    elif choice == "5":
        suggest_random() # call a function for suggestions of random item
    elif choice == "6":
        show_premium_item() # call a function for checking premium items
    elif choice == "7":
        print("THANK YOU FOR VISITING AL- REHMAT FOOD HUB! GOODBAY!")
        break  # terminate the program come outside the loop
    else:
        print("Invalid choice.please try again!")
        