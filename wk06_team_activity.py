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




#2 - Split the line into parts and change your display, so that it shows only the names (instead of the whole line).
for data in hr_system:
  each_part = data.split()
  name = each_part[0]
  person_id = each_part[1]
  job_title = each_part[2]
  salary = each_part[3]
  print(name)

#3 - For each line, get the name and the job title for each person, and display those to the screen.
for data in hr_system:
  each_part = data.split()
  name = each_part[0]
  person_id = each_part[1]
  job_title = each_part[2]
  salary = each_part[3]
  print(f"Name: {name}, Title: {job_title}")

#Stretch Challenge
#Display all four values in this format: name (ID: id_number), job_title - $salary

for data in hr_system:
  each_part = data.split()
  name = each_part[0]
  person_id = each_part[1]
  job_title = each_part[2]
  salary = each_part[3]
  print(f"Name: {name}, Title: {job_title}")

