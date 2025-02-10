#Helaman Menk
#Other members were unable to meet on Tuesday 12m UTC

#Ask the user for a series of numbers, and append each one to a list. Stop when they enter 0.

number_list = []
number = 1
running_total = 0

while number != 0:
    number = -1
    number = int(input("Enter number: "))
    if number != 0:
        number_list.append(number)

#Compute the sum, or total, of the numbers in the list.

for number in number_list:
    running_total = running_total + number
    
# Display the total
print(f"The total is: {running_total:.2f}") 

