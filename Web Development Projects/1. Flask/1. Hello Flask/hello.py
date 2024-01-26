from flask import Flask

print(__name__)
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hola, estoy en la ruta principal!</p>"

@app.route("/second_page")
def page_secondary():
    return "<h1>Hola estoy en la ruta secundaria</h1>"

if __name__ == "__main__":
    app.run()