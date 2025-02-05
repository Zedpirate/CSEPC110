#W02 Learning Activity 1 of 2: Numeric Variables

"""
song1 = "213 seconds" #This is a string
song2 = 213 #This is a number (interger)

song3 = 213.5 #This is a number (floater - has number after decimals)

song4 = "150"
song5 = 250.25


song01 = 162
song02 = 250
song03 = float(input("What is the length of the song?: "))
song03_input = int(song03)


playlist = song01 + song02 + song03

print(f"The play list has {playlist} seconds")



#Activity Instructions
#Prompt user for age. Convert to number, add one and tell them how old they'll be next birthday


age = input("How are you now?: ")
age_number = int(age)

new_age = age_number + 1
print(f"You'll be {new_age} after your next birthday. ")

print()

cartons = input("How many egg cartons do you have?: ")
total_eggs = int(cartons) * 12

print(f"You have {total_eggs} eggs.")

print()

cookies = input("How many cookies do you have?: ")
people = input("How many people are going to eat cookies?: ")

cookie_person = int(cookies) / int(people)

print(f"Each person can eat {cookie_person} cookies.")

print()





#W02 Learning Activity 2 of 2: Mathematical Expressions

import math

number = 5.12
rounded_up_number = math.ceil(number)

print(rounded_up_number)

number_new01 = 3.1456236

print(f"The number is ${number_new01:.2f}.") #using the : and . you have to specify quantity after decimal point

number_new02 = round(number_new01, 3)
print(number_new02)

"""

#Assignment Fahrenheit to Celsius

fahrenheit = input("What is the temperature in Fahrenheit?: ")

celsius = (int(fahrenheit) - 32) * (5/9)
print(f"The temperature in Celsius is {celsius:.1f} degrees")
