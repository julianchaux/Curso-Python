#List Comprehension

# name ="Angela"
# new_list = [letter for letter in name]
# print(new_list)

# numbers = range(1, 5)
# double_numbers = [n*2 for n in numbers]
# print(double_numbers)

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)

long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)