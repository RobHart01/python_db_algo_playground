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

# 6. For loops
print("Here are my hobbies:")
for one_hobby in hobbies:
  print(one_hobby)
print("--------------------")
x = 0
for one_hobby in hobbies:
  x = x + 1
  print(x, one_hobby)
print("--------------------")



