#Helaman Menk

#Milestone
#Assignment
#Download the dataset and write a Python program to analyze it to answer the following questions:
#What is the year and country that has the lowest life expectancy in the dataset?
#What is the year and country that has the highest life expectancy in the dataset?
#Allow the user to type in a year, then, find the average life expectancy for that year. 
#Then find the country with the minimum and the one with the maximum life expectancies for that year.

#File Format:
#Entity,Code,Year,Life expectancy (years)

life_expectancy = [
Afghanistan,AFG,1950,27.638
Afghanistan,AFG,1951,27.878
Afghanistan,AFG,1952,28.361
Afghanistan,AFG,1953,28.852
Afghanistan,AFG,1954,29.35
]


#with ("life-expectancy.csv") as f:
  #for line in f:
  for line in life_expectancy:
        parts = line.split(" ")
