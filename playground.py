# 1.
print("Hello World")
print("--------------------")

# 2.
msg = "Hello World"
print(msg)
print("--------------------")

# 3.
num1 = 20
num2 = 2
sumnum = num1 + num2
print(sumnum)
print("--------------------")

# 4.
hobbies = []
print(len(hobbies))
print("--------------------")

# 5. Lists
hobbies.append("Coding")
print(hobbies)
print(hobbies[0])

print("--------------------")

hobbies.append('Photography')
print(hobbies)
print(hobbies[1])

print("--------------------")

hobbies.append("Real Estate")
print(hobbies)
print(len(hobbies))

print("--------------------")

hobbies.pop(1)
print(hobbies)

print("--------------------")

hobbies.append("Dancing")
print(hobbies)
hobbies.remove("Dancing")

print("--------------------")

# 6 For loops
print("Here are my hobbies:")
for one_hobby in hobbies:
  print(one_hobby)
print("--------------------")
x = 0
for one_hobby in hobbies:
  x = x + 1
  print(x, one_hobby)
print("--------------------")

# 6.1 For loops through strings
random_word = "Robert"
for x in random_word:
  print(x)

print("--------------------")

# 6.2 Using Break
random_word = "Robert"
for x in random_word:
  print(x)
  if x == "b":
    break
print("--------------------")

# 6.3 Using Continue
moving = ["Crawling", "Walking", "Running", "Sprinting"]
for type_of_movement in moving:
  print(type_of_movement)
  if type_of_movement == "Running":
    continue
print("--------------------")

# 6.4 Using range()
for z in range(7):
  print(z)

print("--------------------")

# 6.4.1 Using starting parameter
for v in range(3,7):
  print(v)

print("--------------------")

# 6.4.2 Using incrementing value
for a in range(5, 20, 5):
    print(a)

print("--------------------")

# 6.5 Using else
for b in range(5):
  print(b)
else:
  print("Finally done counting! Whew")

print("--------------------")

# 6.6 Using nested loops
japanese_cars = ["Toyota", "Honda", "Nissan"]
toyoto_car_models = ["Camry", "Corolla", "Highlander"]

for c in japanese_cars:
  for d in toyoto_car_models:
    print(c,d)

print("--------------------")

# 7 Using Objects

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age
  def my_function(self):
    print("Hello my name is " + self.name)

p1 = Person("Robert", 22)
print(p1)
print(p1.name)
print(p1.age)

p1.my_function

print("--------------------")

# Can delete any object using del
# Example del p1.age
# Classes cannot usually be empty but can use the pass statement so it's technically not empty but it is.

class Car:
  def __init__(self, company_name, model_name):
    self.company_name = company_name
    self.model_name = model_name

  def print_name(self):
    print(self.company_name, self.model_name)

x = Car("Toyota", "Camry")
x.print_name()

print("--------------------")
