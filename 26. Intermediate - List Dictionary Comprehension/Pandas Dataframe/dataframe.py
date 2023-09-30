import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)

#Loog through rows of a data frame
# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
for (index, row) in student_data_frame.iterrows():
    #row is a Series
    #print(row["student"])
    #print(row.student)
    if row.student == "Angela":
        print(row.score)