#Absolute Path
# / denota la raiz de la unidad
with open("/OneDrive - Servicio Nacional de Aprendizaje/Desktop/my_file.txt") as file:
    contents = file.read()
    print(contents)

#Relative Path
# D:\2. DESARROLLO PYTHON\1. Curso-Python-Udemy-100dias\Curso-Python\24. Intermediate - Files, Snake Game Advanced
with open("../../../../OneDrive - Servicio Nacional de Aprendizaje/Desktop/my_file.txt") as file1:
    contents1 = file1.read()
    print(contents1)

#Absolute Path
# En otra unidad
with open("C:/Users/Julian Rene Chaux/Documents/my_file.txt") as file2:
    contents2 = file2.read()
    print(contents2)
    