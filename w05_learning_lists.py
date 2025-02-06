#Helaman Menk
#Week05 Leearning Activity

#Using square brakets we can create lists in python [ ] 

clients = []
clients = ["John", "Mary"]
clients = list()

#Can't use the word "list" as a variable because it's a keyword
#Considered good practice to use plural word for variable chose for list name i.e. clients not client; players not player

#To add new clients to the list we use append method.

clients = ["John", "Mary"]
clients.append("Lucas")
clients.append("Lisa")
print(clients)
print()
new_client = input("New client name: ")
clients.append(new_client)

for client in clients:
  print(client)

#Creating loops and list
#User input into lists

clients = []
new_client = ""

while new_client != "quit":
  new_client = input("New client name: ")
  if new_client != "quit":
    clients.append(new_client)

print("The clients are: ")
for client in clients:
  print(f" {client}")

#Working with Lists of Numbers

points_scored = [5,2,5,7,8,9,5,]
running_total = 0

for point_amount in points_scored
  running_total = running_total + point_amount

print(f"The player has scored {running_total} points")
