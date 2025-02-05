
#Week 04 Learning Activities: Loops

#Author: Helaman Menk

#Week 04 Learning Activity Loops

payment = float(input("What is the payment amount?: "))

if payment < 0:
	print("Sorry the payment cannot be negative.")
	payment = float(input("What is the payment amount?: "))

#When using "while" it creats a loop when conditions aren't met or "as long as"
#When the user inputs a number less than zero, it'll loop back and print the original input asking for the payment amount.

while payment < 0:
	print("Sorry the payment cannot be negative.")
	payment = float(input("What is the payment amount?: "))

print(f"The amount is ${payment:.2f}")


#Keep Looping while number is less than 0
number = float(input("What is your number?: "))

while number <= 0:
	print("Sorry, the number must be positive.")
	number = input("What is your number?: ")
print("Loop finished")

#Child asking for candy Loop
candy = input("Can I have some candy? YES or NO: ")
answer = candy.lower()

while answer != "yes":
	candy = input("Can I have some candy? YES or NO: ")
	answer = candy.lower()
print("Thank you, mom and dad for the candy")


print("Testing the change")
#Making a change to test.

print("Change was done on browser Github. Check if appears in VSC")

##
##wk04 - Learning about "For" Loops
##

citis = ["New York City", "London", "Tokyo", "Accra", "Mexico City", "Santiago"]

for city in cities:
	print(city)


numbers = [1,2,3,4,5]
for number in numbers:
	print(number)

#Range (start, stop, step)

numbers = [1,2,3,4,5]

#First number is where it Starts, second Stops, third is the amount of each incrament 
#IMPORTANT - The Value used in stop, The Range goes UP TO but does not include the number for Stop.
#So to account up to 10 I would need to range(1 ,11 ,1) and not range(1 ,10 ,1 )
for number in range(1 ,10 ,1 ): 
	print(number)

#It's common practice to use the letter "i" as variable name for counting purposes in programming.
#It would look like this

for i in range(1 ,10 ,1 ): 
	print(i)


#Next example
items = ["Crayon", "Pencil", "Scissors", "Pens", "Markers", "Glue"]

for item in items:
	print(f"This item is {item}")


for i in range(0 ,5 ,1 ):
    print(i)
    for j in range(10, 16):
        print(f"--{j}")


##Generally used "i" for simple counting loop. If there is a sublook the variable will generally be "j" and if there is a third look it'll be "k".
##After that point it's generally recognized there's probably another or an easier way to do it, or should start using more descriptive variable names.



colors = ["red", "blue", "green", "yellow"]

for color in colors
	print(color)

for i in range(1 , 9 ,1 )
	print(i)

for i in range(2 ,21 , 2)
	print(i)

##
##wk04 - Looping strings
##

#1 Thes 5:16
scripture = "Rejoice Evermore."
scripture_length = len(scripture)

for i in range(scripture_length):
	letter = scripture[i]
	print(letter)

letter = scripture [2] #Doing this can pull the item in position 2. Python starts counting at 0
print(letter)

for letter in scripture:
	print(letter)


#1 Thes 5:16
scripture = "Rejoice Evermore."

#Since calling for "len" is so common, it'll usually go straight into the code
for i in range(len(scripture)):
	letter = scripture[i]
	print(letter)
	

first_name = "Brigham"
for letter in first_name:
    print(f"The letter is: {letter}")

word = "book"
letter_book = len(word)

##Review at home
for index in range(letter_book):
    letter = word[index]
    print(f"Index: {index} Letter: {letter}")


#Activity

word = "commitment"
favorite_letter = input("What is your favorite letter? ")

for letter in range(word)
	if letter = "m":
	print(letter.upper(), end="")
	else:
	print(letter.lower(), end="")
print()



word = "commitment"
favorite_letter = input("What is your favorite letter? ")

for letter in range(word)
	if letter.lower() == favorite_letter.lower():
	print("_", end="")
	else: 
	print(letter.lower(), end="")
print()

S

