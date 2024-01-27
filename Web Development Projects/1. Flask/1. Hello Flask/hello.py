from flask import Flask

print(__name__)
app = Flask(__name__)

###################################################
# Decoradores
###################################################
def make_bold(function):
    def wrapper():
        return "<b>" + function() + "</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return "<em>" + function() + "</em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return "<u>" + function() + "</u>"
    return wrapper
##################################################   

@app.route("/")
def hello_world():
    return "<h1 style='text-align:center'>¡Hola, estoy en la ruta principal!</h1>" \
            "<p>Esto es un  <u><em><b>párrafo</u></em></b></p>" \
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXppcHludHlhbzl5bnh6OGZ3YnJydTR2aWd3OWt5NWR0dHg2c3BidyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/urvsFBDfR6N32/giphy.gif" width=200>'

@app.route("/second_page")
@make_bold
@make_emphasis
@make_underline
def page_secondary():
    return "<h1>Hola estoy en la ruta secundaria</h1>"

@app.route("/username/<name>/<int:age>")
def greet(name, age):
    return f"<h2>Hola {name} y tienes {age} años!</h2>"

if __name__ == "__main__":
    app.run(debug=True)