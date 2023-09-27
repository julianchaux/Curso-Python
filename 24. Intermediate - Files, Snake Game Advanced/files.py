#file = open("my_file.txt")
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

#Escribir en un archivo pero borra el contenido
# with open("my_file.txt", mode="w") as file:
#     file.write("New Text.")

#Escribir en un archivo y no borra el contenido
# with open("my_file.txt", mode="a") as file:
#     file.write("\nNew Text.")

#Escribir en un archivo, y si no existe, lo crea
with open("my_other_file.txt", mode="w") as file:
    file.write("New Text.")