from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
@app.route('/<int:num>')
def home(num=None):
    blog_url = 'https://api.npoint.io/c790b4d5cab58020d391'
    response = requests.get(url=blog_url)
    all_posts = response.json()
    
    if num is not None:
        # If a specific post is requested, filter the post
        post = next((post for post in all_posts if post['id'] == num), None)
        return render_template("post.html", post=post)
    else:
        return render_template("index.html", posts=all_posts)

if __name__ == "__main__":
    app.run(debug=True)
