username = input("Enter username:")
print("Username is: " + username)

price = 50
txt = "The price is {} dollars"
print(txt.format(price))

myorder = "I have a {carname}, it is a {model}."
print(myorder.format(carname = "Telsa", model = "Model Y"))

age = 21
name = "Alex"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))