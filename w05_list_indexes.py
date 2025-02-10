#Helaman Menk

#Started a new file because the last one apparently wasn't synchronizing between github and VSC on my PC

#Index     0     1     2
colors = ["red", "blue", "yellow"]

#indexes always start at zero and count up by one

print(colors[1])

for color in colors:
  print(color)

colors.pop(1)
colors.insert(2,"orange")

for i in range(len(colors)):
  color = colors[i]
  human_count = i + 1
  print(f"{human_count} - {color}")

#Use .pop() to remove something from the list


#Please enter the items of the shopping list (type: quit to finish):

shopping_list = [""]
add_list = ""

while add_list != "quit"
  
