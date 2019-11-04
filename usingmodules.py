import modules
import people as peep
import platform as pf
import datetime
import json

modules.say_hi("Robert")
z = peep.person4["name"]
modules.say_hi(z)

x = pf.system()
print(x)
y = dir(pf)
print(y)

print("----------")

v = dir(datetime)
print(v)

print("----------")

c = datetime.datetime.now()
print(c)
print(c.year)
print(c.strftime("%A"))
print(c.day)

print("----------")

d = '{"name":"Robert", "age":22, "city":"Tokyo"}'

e = json.loads(d)
print(e["city"])