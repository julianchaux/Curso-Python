try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["sdsfd"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    #Se ejecuta si no hay errores
    content = file.read()
    print(content)
finally:
    #Siempre se ejecuta, sin importar si hay errores o no
    file.close()
    print("File was closed.")