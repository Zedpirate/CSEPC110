#Helaman Menk
#Doing file alone, team mates were unable to meet on specified date.

hr_system = [
"Alexia 1913 Engineer 84000",
"Herman 4266 Manager 106000",
"Jay 5849 Engineer 93000",
"Ahmad 1326 Tester 85000",
]

#name id_number job_title salary

#iterate through each line of this file, gather the information from each field and display or take certain actions depending on the data

with open("hr_system.txt") as hr_system:
  for line in hr_system:
        parts = line.split(" ")
  

#2 - Split the line into parts and change your display, so that it shows only the names (instead of the whole line).
with open("hr_system.txt") as hr_system:
  for data in hr_system:
    each_part = data.split(" ")
    name = each_part[0]
    person_id = each_part[1]
    job_title = each_part[2]
    salary = each_part[3]
    print(name)

#3 - For each line, get the name and the job title for each person, and display those to the screen.
with open("hr_system.txt") as hr_system:
  for data in hr_system:
    each_part = data.split()
    name = each_part[0]
    person_id = each_part[1]
    job_title = each_part[2]
    salary = each_part[3]
    print(f"Name: {name}, Title: {job_title}")

#Stretch Challenge
#Display all four values in this format: name (ID: id_number), job_title - $salary

with open("hr_system.txt") as hr_system:
  for data in hr_system:
    each_part = data.split()
    name = each_part[0]
    person_id = each_part[1]
    job_title = each_part[2]
    salary = int(each_part[3])
    salary = (salary/12)/2
    if job_title == "Engineer":
      salary = salary + 1000
    print(f"{name} (ID: {person_id}), {job_title} - ${salary:.2f}")

#2 - Instead of displaying the salary information, calculate and display a paycheck amount for the employee. Assume that they are paid twice a month.
#Added salary = (salary/12)/2 before the Print statement to do this

#3 - Change the program so that it generates bonuses for anyone who is an engineer. For each of these employees, add $1000 to their paycheck amount.
 #if job_title == "Engineer":
 #   salary = salary + 1000
#This If statement ran right after salary, checked if job_title is "engineer" and would add 1000

