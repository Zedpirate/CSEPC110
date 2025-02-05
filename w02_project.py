#W02 Project: Meal Price Calculator
#Author: Helaman Menk

child_meal = input("What is the price of a child's meal?: ")
adult_meal = input("What is the price of an adult's meal?: ")

print()
number_children = input("How many children are there?: ")
number_adult = input("How many adults are there?: ")

subtotal = (int(number_adult) * float(adult_meal)) + (int(number_children) * float(child_meal))
print(f"Subtotal: ${subtotal:.2f}")

sales_tax = input("What is the sales tax rate?: ")
tax_amount = subtotal * (float(sales_tax)/100)

print()
print(f"Sales tax: ${tax_amount:.2f}")
print()

total = subtotal + tax_amount

print(f"The total for the meal is: ${total:.2f}")

print()
tip = input("Would you like to leave a tip? \n Yes or No: ")
print()

#Added if then statement asking if the customer wants to leave a tip.
#If they don't leave a tip, just calculate the change
#If customer decides to leave a tip, ask the percentage, calculate the amount and add to the total

if tip == "No":
    payment = input("What is the payment amount?: ")
    change = float(payment) - total
    print(f"Your change is ${change:.2f}")
else:    
    tip_percent = input("Input percentage you would like to tip: ")
    print()
    tip_total = total * (float(tip_percent)/100)
    print(f"Your total tip is: ${tip_total:.2f}")
    final_amount = total + tip_total
    print(f"Your total now comes to ${final_amount:.2f}.")
    payment = input("What is the payment amount?: ")
    change = float(payment) - final_amount
    print(f"Your change is ${change:.2f}")


