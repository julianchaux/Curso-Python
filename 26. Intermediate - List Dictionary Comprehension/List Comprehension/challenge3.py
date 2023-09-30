with open("./file1.txt") as file1:
    contents1 = file1.readlines()

with open("./file2.txt") as file2:
    contents2 = file2.readlines()

result = [int(number.strip()) for number in contents1 if number in contents2]

# Write your code above 👆

print(result)