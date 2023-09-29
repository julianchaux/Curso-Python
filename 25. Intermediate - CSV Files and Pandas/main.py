# with open("weather_data.csv", mode="r") as data_file:
#     print(data := data_file.readlines())

# import csv

# with open("weather_data.csv", mode="r") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("./weather_data.csv")
data_dict = data.to_dict()
print(data_dict)

#Series.to_list()
#Una serie es una columna de datos
temp_list = data["temp"].to_list()
print(temp_list)

average = sum(temp_list) / len(temp_list)
print(average)
print(data["temp"].mean())
print(data["temp"].max())

#Get Data in Columns
print(data["condition"])
print(data.condition)

#Get Data in Rows
#Devulve toda la fila donde el día es Monday
print(data[data["day"] == "Monday"])
#Devuelve toda la fila donde el valor de temp es el máximo
print(data[data["temp"] == data["temp"].max()])
print(data[data.temp == data.temp.max()])
print(data.temp == data.temp.max())

monday = data[data["day"] == "Monday"]
monday_temp = monday.temp[0]
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

#Create a dataframe from scratch
data_dict_students = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 55]
}
print(data1 := pandas.DataFrame(data_dict_students))
data1.to_csv("new_data.csv")