from flask import Flask

print(__name__)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align:center'>¡Hola, estoy en la ruta principal!</h1>" \
            "<p>Esto es un  párrafo</p>" \
            '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcXppcHludHlhbzl5bnh6OGZ3YnJydTR2aWd3OWt5NWR0dHg2c3BidyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/urvsFBDfR6N32/giphy.gif" width=200>'

@app.route("/second_page")
def page_secondary():
    return "<h1>Hola estoy en la ruta secundaria</h1>"

@app.route("/username/<name>/<int:age>")
def greet(name, age):
    return f"<h2>Hola {name} y tienes {age} años!</h2>"

if __name__ == "__main__":
    app.run(debug=True)