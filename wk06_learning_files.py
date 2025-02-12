#Helaman Menk

#Week06 - 12/02

#Learning using Files

#using strip()

name = "   Helaman Menk    "
print(f"***{name}***")

name = name.strip()
print(f"***{name}***")


colors = "red, orange, blue, yellow"
color_list = colors.split()
print(color_list)
print(color_list[1].strip())

"If add "," with parentheses inside the split() then it'll use commas as seperator to create the list
