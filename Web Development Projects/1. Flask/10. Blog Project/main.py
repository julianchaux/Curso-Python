from flask import Flask, render_template
from post import Post

app = Flask(__name__)
post = Post()
all_posts = post.get_post()

@app.route('/')
def home():
    global all_posts
    return render_template("index.html", render_posts=all_posts)

@app.route('/post/<int:num_post>')
def get_post(num_post):
    global all_posts
    return render_template("post.html", id_post=num_post, render_posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
