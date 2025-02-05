#Helaman Menk

#Week 03 If statements Homework

"""
number1 = input("Please write a number 1 through 100: ")
number2 = input("Please choose a second number also 1 through 100: ")

if number1 > number2:
    print("First number is greater.")

else:
    print("The first number is not greater.")


if number1 == number2:
    print("The numbers are equal.")
else:
    print("The numbers aren't equal.")

if number1 < number2:
    print("The first number is smaller than the second number.")
else:
    print("The first number is not smaller than the first.")

favorite_animal = input("What's your favorite animal?: ")

if favorite_animal.lower() == "Wolf":
    print("That's my favorite animal too!")
else:
    print("That's not my favorite, my favorite is a wolf.")



#Week03 Complex Conditions

#Boolean Expressions

men = int(input("How many men are playing?: "))
women = int(input("How many women are playing?: "))

total = men + women

has_enough_players = total >= 7
has_enough_women = women >= 4


if has_enough_players and has_enough_women:
    print("You can play")
else:
    print("You cannot play a game.")
if not has_enough_players:
    print("Ask the other team if the want to practice.")

#"Not" is 1, "and" is 2 and "for" is 3



temperature = float(input("What temperature is it outside today?: "))

if temperature <5 and temperature >-15:
    print("Ask some other questions...")
    weather = input("What is the weather like (snow, rain, sunny)?: ")

    if weather == "snow":
        print("Better stay inside")
    elif weather == "rain":
        print("Go ahead and run but bring raing gear")
    elif weather == "sunny":
        print("Dress warm and enjoy")
    else:
        print("I didn't understand your response.")         
elif temperature <-15:
    print("It is too cold. Don't go.")
else:
    print("Enjoy your run.")




#Common Mistakes

x = int(input("What is the value of X?: "))

if x == 5 or x==6:
    print("X is 5 or 6")


age = input("How old are you?: ")
age_number = int(age)

if age_number == 18:
    print("You're 18!")



rewards = 0
choice = "drink"
total_order = 6

if total_order >5 and (choice == "drink" or choice == "cookie"):
    rewards += 5

print(f"You have {rewards} reward points!")




#Exercise - Qualifying for a Loan


loan_size = int(input("How large is the loan 1-10?: "))
credit_history = int(input("How good is the credit history 1-10?: "))
income = int(input("How high is the income 1-10?: "))
downpayment = int(input ("How large is the downpayment?: "))

#First check:

if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        print("Loan Approved because of good credit and income")
    elif (credit_history >= 7 or income >= 7) and downpayment >= 5:
        print("Loan Approved because of downpayment")
    else:
        print("Loan rejected")
elif loan_size < 5:
    if credit_history < 4:
        print("Loan rejected because of credit history")
    elif income >= 7 or downpayment >= 7:
        print("Small Loan accepted: high income or downpayment")
    elif income >= 4 and downpayment >= 4:
        print("Small loan accepted: Medium income and medium downpayment")
    else:
        print("Loan rejected, not enough income or downpayment.")



"""

x = 5
y = 10

if x == 5:
    print("a")

    if y == 6:
        print("b")
else:
    print("c")

    if y == 10:
        print("d")


x = 5
y = 6

if x == 5:
    print("a")

    if y == 6:
        print("b")
else:
    print("c")

    if y == 10:
        print("d")


print("-------------------") 

x = 6
y = 6

if x == 5:
    print("a")

    if y == 6:
        print("b")
else:
    print("c")

    if y == 10:
        print("d")