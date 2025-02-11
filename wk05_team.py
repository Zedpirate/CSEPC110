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

#Compute the average of the numbers in the list.

average = running_total / len(number_list)
print(f"The average is: {average:.2f}")


#Find the maximum, or largest, number in the list.

print(f"The largest number is: {max(number_list):.2f}")

#Have the user enter both positive and negative numbers, then find the smallest positive number (the positive number that is closest to zero).

print(f"The smallest positive number is: {min(number for number in number_list if number > 0):.2f}")

#Sort the numbers in the list and display the new, sorted list. Hint: There are python libraries that can help you here, try searching the internet for them.

number_list.sort()
print(f"The sorted list is: {number_list}")
