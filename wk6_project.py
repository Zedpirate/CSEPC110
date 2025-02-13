#Helaman Menk

#Milestone
#Assignment
#Download the dataset and write a Python program to analyze it to answer the following questions:
#What is the year and country that has the lowest life expectancy in the dataset? - Ok
#What is the year and country that has the highest life expectancy in the dataset? - Ok
#Allow the user to type in a year, then, find the average life expectancy for that year. 
#Then find the country with the minimum and the one with the maximum life expectancies for that year.

#File Format:
#Entity,Code,Year,Life expectancy (years)

life_expectancy = [
  "Afghanistan,AFG,1950,27.638",
  "Afghanistan,AFG,1951,27.878",
  "Afghanistan,AFG,1952,28.361",
  "Afghanistan,AFG,1953,28.852",
  "Afghanistan,AFG,1954,29.35",
  "Hong Kong,HKG,1980,74.679",
  "Hong Kong,HKG,1981,75.043",
  "Iceland,ISL,1891,47.509998",
  "Iceland,ISL,1892,52.740002",
  "Morocco,MAR,2012,74.97",
  "Myanmar,MMR,1957,40.528"
]

lowest_life_expectancy = 999
lowest_entity = " "
lowest_year = -1

highest_life_expectancy = 1
highest_entity = " "
highest_year = 1

part_three = []


#with ("life-expectancy.csv") as f:
  #for line in f:
for line in life_expectancy:
  parts = line.split(",")
  entity = parts[0]
  code = parts[1]
  year = int(parts[2])
  life_expectancy = float(parts[3])
  part_three.append(life_expectancy)
  if life_expectancy < lowest_life_expectancy:
      lowest_life_expectancy = life_expectancy
      lowest_entity = entity
      lowest_year = year
      print(f"Country with lowest life expectancy was {lowest_entity} in {lowest_year} with just {lowest_life_expectancy} years")
  if life_expectancy > highest_life_expectancy:
        highest_life_expectancy = life_expectancy
        highest_entity = entity
        highest_year = year
      print(f"Country with highest life expectancy was {highest_entity} in {highest_year} with {highest_life_expectancy} years")


print()
user_year = int(input("Please type in a year: "))
user_year_int = int(user_year)
while user_year_int != 0:
        for line in expectancy_file:
            parts = line.split(",")
            entity = parts[0]
            code = parts[1]
            year = int(parts[2])
            life_expectancy = float(parts[3])
        if user_year_int == year:
            part_three = []
            part_three.append(life_expectancy)
            count_part_three = len(part_three) + 1
            real_average = sum(part_three) / count_part_three
        print(real_average)
        user_year = input("Please type in a year: ")
