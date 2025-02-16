#Helaman Menk

#Milestone
#Assignment
#Download the dataset and write a Python program to analyze it to answer the following questions:
#What is the year and country that has the lowest life expectancy in the dataset? - Ok
#What is the year and country that has the highest life expectancy in the dataset? - Ok
#Allow the user to type in a year, then, find the average life expectancy for that year. - ok
#Then find the country with the minimum and the one with the maximum life expectancies for that year. - ok

#Stretch Goal: Allow the user to type in a country, then, find the average life expectancy for that country. - ok
#Appended entities into a list, then turned the list into a set to remove duplicates, then turned it back into a list to restore the original order.
#Print out the list of available countries for the user to choose from



#File Format:
#Entity,Code,Year,Life expectancy (years)

"""
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
"""

lowest_life_expectancy = 999
lowest_entity = " "
lowest_year = -1

highest_life_expectancy = 1
highest_entity = " "
highest_year = 1
data = []
countries = []


with open("life-expectancy.csv") as expectancy_file:
	next(expectancy_file) #skip header 
	for line in expectancy_file:
		parts = line.split(",")
		entity = parts[0]
		code = parts[1]
		year = int(parts[2]) #Should be format YYYY
		life_expectancy = float(parts[3])
		data.append((entity, year, life_expectancy))
		countries.append(entity)
		if life_expectancy < lowest_life_expectancy:
			lowest_life_expectancy = life_expectancy
			lowest_entity = entity
			lowest_year = year
			
		if life_expectancy > highest_life_expectancy:
			highest_life_expectancy = life_expectancy
			highest_entity = entity
			highest_year = year

print(f"Country with lowest life expectancy was {lowest_entity} in {lowest_year} with just {lowest_life_expectancy} years")
print(f"Country with highest life expectancy was {highest_entity} in {highest_year} with {highest_life_expectancy} years")
print()

set_countries = set(countries)
restored_countries = list(set_countries)

#Menu - Type 1 to search by year or Type 2 to search by country
option = ""
while option != "quit":
	print("Please select an option:")
	print("DATE")
	print("COUNTRY")
	print("QUIT")
	option = (input("\nWhat would you like to do?: ")).lower()

	if option == "date":
		print()
		user_year = int(input("Please type in a year: "))
		while user_year != 5:
			total_life_expectancy = 0
			count = 0
			lowest_year_life_expectancy = float(999)
			highest_year_life_expectancy = 0
			lowest_year_entity = ""
			highest_year_entity = ""
			
			for entity, year, life_expectancy in data:
				if year == user_year:
					total_life_expectancy += life_expectancy
					count += 1					
					if life_expectancy < lowest_year_life_expectancy:
						lowest_year_life_expectancy = life_expectancy
						lowest_year_entity = entity
					if life_expectancy > highest_year_life_expectancy:
						highest_year_life_expectancy = life_expectancy
						highest_year_entity = entity
			
			if count > 0:
				average_life_expectancy = total_life_expectancy / count
				print(f"Average life expectancy for {user_year} is {average_life_expectancy:.2f} years")
				print(f"Country with lowest life expectancy in {user_year} was {lowest_year_entity} with {lowest_year_life_expectancy} years")
				print(f"Country with highest life expectancy in {user_year} was {highest_year_entity} with {highest_year_life_expectancy} years")
			else:
				print(f"\n No data available for the year {user_year}")
			print()
			user_year = int(input("Please type in another year or 5 to exit: "))
		
	

	if option == "country":
		print()
		print(restored_countries)
		user_country = input("Please type in a country or quit to exit: ").lower()
		while user_country != "quit":
			total_life_expectancy = 0
			count = 0
			lowest_country_life_expectancy = float(999)
			highest_country_life_expectancy = 0
			lowest_country_year = -1
			highest_country_year = -1

			for entity, year, life_expectancy in data:
				if entity.lower() == user_country:
					total_life_expectancy += life_expectancy
					count += 1
					if life_expectancy < lowest_country_life_expectancy:
						lowest_country_life_expectancy = life_expectancy
						lowest_country_year = year
					if life_expectancy > highest_country_life_expectancy:
						highest_country_life_expectancy = life_expectancy
						highest_country_year = year

			if count > 0:
				average_life_expectancy = total_life_expectancy / count
				print(f"Average life expectancy for {user_country} is {average_life_expectancy:.2f} years")
				print(f"Year with lowest life expectancy for {user_country} was {lowest_country_year} with {lowest_country_life_expectancy} years")
				print(f"Year with highest life expectancy for {user_country} was {highest_country_year} with {highest_country_life_expectancy} years")
			else:
				print(f"\nNo data available for the country {user_country}")
			print()
			
			user_country = input("Please type in another country or 'quit' to exit: ").lower()
		if user_country == "quit":
			print("Goodbye!")

	if option == "quit":
		print("Goodbye!")
		break



