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

expectancy_file = [
  "Afghanistan,AFG,1950,25.00",
  "Afghanistan,AFG,1951,30.00",
  "Afghanistan,AFG,1952,28.361",
  "Afghanistan,AFG,1953,28.852",
  "Afghanistan,AFG,1954,29.35",
  "Hong Kong,HKG,1980,74.679",
  "Hong Kong,HKG,1981,75.043",
  "Iceland,ISL,1891,47.509998",
  "Iceland,ISL,1892,52.740002",
  "Morocco,MAR,2012,74.97",
  "Myanmar,MMR,1950,45.00"
]

lowest_life_expectancy = 999
lowest_entity = " "
lowest_year = -1

highest_life_expectancy = 1
highest_entity = " "
highest_year = 1


#with ("life-expectancy.csv") as f:
  #for line in f:
for line in expectancy_file:
  parts = line.split(",")
  entity = parts[0]
  code = parts[1]
  year = int(parts[2])
  life_expectancy = float(parts[3])
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


#Menu - Type 1 to search by year or Type 2 to search by country



print()
user_year = int(input("Please type in a year: "))

while user_year != 0:
    total_life_expectancy = 0
    count = 0
    lowest_year = float(999)
    highest_year = 0
    lowest_entity = ""
    highest_entity = ""

    for line in expectancy_file:
        parts = line.split(",")
        entity = parts[0]
        year = int(parts[2])
        life_expectancy = float(parts[3])

        if year == user_year:
            total_life_expectancy += life_expectancy
            count += 1
            if life_expectancy < lowest_year:
                lowest_year = life_expectancy
                lowest_entity = entity
            if life_expectancy > highest_year:
                highest_year = life_expectancy
                highest_entity = entity

    if count > 0:
        average_life_expectancy = total_life_expectancy / count
        print(f"Average life expectancy for {user_year} is {average_life_expectancy:.2f} years")
        print(f"Country with lowest life expectancy in {user_year} was {lowest_entity} with {lowest_year} years")
        print(f"Country with highest life expectancy in {user_year} was {highest_entity} with {highest_year} years")
    else:
        print(f"\n No data available for the year {user_year}")
    print()
    user_year = int(input("Please type in another year or 0 to exit: "))
