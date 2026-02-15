import math

first_name = 'Patricia'
surname = 'J'
country = 'Sweden'
age = 200
is_light_on = True

first_name, surname, country, age, is_light_on = 'Patricia', 'J', 'Sweden', 200, True

print(type(first_name))
print(type(surname))
print(type(country))
print(type(age))
print(type(is_light_on))

print(len(first_name))
print(len(surname))

num_one = 5
num_two = 4
total = num_one + num_two
print(total)

diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_two % num_one
exp = num_one ** num_two
floor_division = num_one // num_two

area_of_circle = math.pi * 30 ** 2
circum_of_circle = 2 * math.pi * 30
print(area_of_circle, circum_of_circle)

radius = float(input('Enter the radius of the circle (cm): '))
area_of_circle = math.pi * radius ** 2
circum_of_circle = 2 * math.pi * radius
print(area_of_circle, circum_of_circle)
