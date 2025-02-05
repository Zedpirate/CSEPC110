
#Author: Helaman Menk
#ID Badge

print("Please fill out the following information: ")
print()

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
email = input("What is your email address? ")
phone_number = input("What is your phone number? ")
job = input("What's your job title? ")
id_number = input("What's your ID number? ")
hair_color = input("What is your hair color? ")
eye_color = input("What is your eye color? ")
month_started = input("What month did you start? ")
advanced_training = input("Have you completed advance training? Yes or No: ")


print()
print("The ID Card is:")
print("--------------------------------")
print(f"{last_name.upper()}, {first_name.capitalize()}")
print(job.title())
print(f"ID Number: {id_number}")
print()
print(email.lower())
print(phone_number)

#Stretch Challange n1
print()
print(f"{'Hair: '  + hair_color:<20} Eyes: {eye_color}")
print(f"{'Month: ' + month_started:<20} Training: {advanced_training}")
print("--------------------------------")