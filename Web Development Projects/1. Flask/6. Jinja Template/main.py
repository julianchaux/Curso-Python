from flask import Flask, render_template
import random
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def home():
    random_number = random.randint(0, 10)
    current_year = datetime.now().year
    print(current_year)
    name = "Julian Chaux"
    #Se envían argumentos con nombre **kwargs
    return render_template("index.html", num=random_number, current_year=current_year, name=name)


if __name__ == "__main__":
    app.run(debug=True)


