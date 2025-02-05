
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

#Making a chane to test.
