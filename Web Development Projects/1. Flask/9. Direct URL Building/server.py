from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route('/')
def get_home():
    return render_template("index.html")

@app.route('/blog/<num>')
def get_blog(num):
    print(num)
    #Fake blog: https://www.npoint.io/docs/c790b4d5cab58020d391
    response = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391")
    response.raise_for_status()
    all_posts = response.json()
    
    return render_template("blog.html", posts=all_posts)


if __name__ == "__main__":
    app.run(debug=True)