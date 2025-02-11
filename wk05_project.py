#Helaman Menk
#Week 05 Project

#Stretch: I added a running total that calculates the individual item prices times the quantity of items and adds them together to get a total.
#The hard part was figuring out how to remove an item from the list and then update the running total to reflect the change.
#I tried to just calculate multiplying indexes when I got to option 4 but that didn't work, but I remmebered from the Learning Lists we kept a running total, so I just used that.


shopping_cart = []
shopping_prices = []
qty_items = []
item = ""
running_total = 0

print("Welcome to the shopping cart program! \n type 'quit' to finish:")

while item != "quit":
    item = input("What item would you like to add to the shopping cart?: ")
    
    if item != "quit":    
        price = float(input("What is the price of the item?: "))
        qty_item = int(input("How many of this item would you like to add?: "))
        shopping_cart.append(item.capitalize())
        shopping_prices.append(price)
        qty_items.append(qty_item)
        running_total = running_total + (price * qty_item)
   
                
print("\n The contents of the shopping cart are:")
for i in range(len(shopping_cart)):
    item = shopping_cart[i]
    print(f"{i+1}. {item} - (${shopping_prices[i]:.2f} x {qty_items[i]}) - Total: ${shopping_prices[i] * qty_items[i]:.2f}")


"""
Please select one of the following: 
1. Add item
2. View cart
3. Remove item
4. Compute total
5. Quit
"""
option = 0

while option != 5:
    print("\nPlease select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit")
    
    option = int(input("What would you like to do?: "))
    if option == 1:
        item = input("What item would you like to add to the shopping cart?: ")
        price = float(input("What is the price of the item?: "))
        qty_item = int(input("How many of this item would you like to add?: "))
        shopping_cart.append(item.capitalize())
        shopping_prices.append(price)
        qty_items.append(qty_item)
        running_total = running_total + (price * qty_item)
    elif option == 2:
        print("\n The contents of the shopping cart are:")
        for i in range(len(shopping_cart)):
            item = shopping_cart[i]
            print(f"{i+1}. {item} - (${shopping_prices[i]:.2f} x {qty_items[i]}) - Total: ${shopping_prices[i] * qty_items[i]:.2f}")
    elif option == 3:
        print("\n The contents of the shopping cart are:")
        for i in range(len(shopping_cart)):
            item = shopping_cart[i]
            print(f"{i+1}. {item} - (${shopping_prices[i]:.2f} x {qty_items[i]}) - Total: ${shopping_prices[i] * qty_items[i]:.2f}")
        remove = int(input("Which item would you like to remove?: "))
        shopping_cart.pop(remove - 1)
        shopping_prices.pop(remove - 1)
        qty_items.pop(remove - 1)
        running_total = running_total - (price * qty_item)
        print("\n The contents of the shopping cart are:")
        for i in range(len(shopping_cart)):
            item = shopping_cart[i]
            print(f"{i+1}. {item} - (${shopping_prices[i]:.2f} x {qty_items[i]}) - Total: ${shopping_prices[i] * qty_items[i]:.2f}")
    elif option == 4:
        print(f"The total is: {running_total:.2f}") 
    elif option == 5:
        print("Goodbye!")
    else:
        print("Invalid option. Please try again.")


print("\n The contents of the shopping cart are:")
for i in range(len(shopping_cart)):
    item = shopping_cart[i]
    print(f"{i+1}. {item} - (${shopping_prices[i]:.2f} x {qty_items[i]}) - Total: ${shopping_prices[i] * qty_items[i]:.2f}")

print("\nThank you for using the shopping cart program!")


