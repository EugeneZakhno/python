from lists import numbers
from operators import result

names = {"Euegne", "Certys", 'James', "Kitty"}

print(names)

#for loop
for name in names:
    print(name)

person = {
    "name":"Eugene",
    "age": 38,
    "address": "USA"
}
for key in person:
    print(key)

for value in person.values():
    print(value)

for key in person:
    print(f"key {key} , value {person[key]}")

for key, value in person.items():
    print(f"key {key} , value {value}")
#############################33

result = 0
numbers = [8,9,12,77,974,48,67,784]

for number in numbers:
    result += number
    print(f" result is {result}")