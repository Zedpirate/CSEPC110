#Helaman Menk
#Doing file alone, team mates were unable to meet on specified date.

hr_system = [
Alexia 1913 Engineer 84000
Herman 4266 Manager 106000
Jay 5849 Engineer 93000
Ahmad 1326 Tester 85000
]

#name id_number job_title salary

#iterate through each line of this file, gather the information from each field and display or take certain actions depending on the data

for data in hr_system:
  each_part = data.split()
  name = each_part[0]
  person_id = each_part[1]
  job_title = each_part[2]
  salary = each_part[3]
  print(each_part)
