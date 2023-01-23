from flask import Flask, render_template
import requests


app = Flask(__name__)


@app.route('/')
def home():
    blogs_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blogs_endpoint)
    blog_posts = response.json()
    return render_template("index.html", blog_posts=blog_posts)


@app.route('/post/<blog_id>')
def blog_page(blog_id):
    blogs_endpoint = "https://api.npoint.io/c790b4d5cab58020d391"
    response = requests.get(blogs_endpoint)
    blog_posts = response.json()
    post = [post for post in blog_posts if post["id"] == int(blog_id)][0]
    return render_template("post.html", post=post)


if __name__ == "__main__":
    app.run(debug=True)
