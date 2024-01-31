from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/guess/<name>')
def home(name):
    response = requests.get(url=f"https://api.genderize.io?name={name}")
    response.raise_for_status()
    data = response.json()
    gender = data["gender"]

    response = requests.get(url=f"https://api.agify.io?name={name}")
    response.raise_for_status()
    data = response.json()
    age = data["age"]
    
    return render_template("index.html", render_name=name, render_gender=gender, render_age=age)


if __name__ == "__main__":
    app.run(debug=True)
