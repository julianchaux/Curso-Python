#Dictionary Comprehension

# From list
# new_dict = {new_key:new_value for item in list}

# From Dictionary
# new_dict = {new_key:new:value for (key,value) in dict.items()}
# new_dict = {new_key:new:value for (key,value) in dict.items() if test}
import random

# From list
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_scores = {student:random.randint(1, 100) for student in names}
print(students_scores)

# From other dictionary
passed_students = {student:score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)
