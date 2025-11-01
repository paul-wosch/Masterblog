from flask import Flask, render_template, abort
from myapp.config import TEMPLATES_PATH, STATIC_PATH
from myapp.models.blog import Blog

my_blog = Blog()

app = Flask(__name__, template_folder=TEMPLATES_PATH, static_folder=STATIC_PATH)

@app.route("/")
def index():
    """Show the index page for the blog."""
    my_blog.get_posts()
    blog_posts = my_blog.get_posts()
    return render_template('index.html', posts=blog_posts)


@app.route("/show/<post_id>")
def show(post_id):
    """Show a single blog post."""
    post_obj = None
    if post_id.isdigit():
        post_obj = my_blog.get(int(post_id))
    if post_obj is None:
        abort(404)
    return render_template('show.html', post=post_obj)


@app.route("/add", methods=["GET", "POST"])
def add():
    """Show a form for adding a blog post."""
    return "add"


@app.route("/update/<post_id>", methods=["GET", "POST"])
def update(post_id):
    """Show a form for updating a blog post."""
    return "update"


@app.route("/like/<post_id>", methods=["POST"])
def like(post_id):
    """Route to like a blog post."""
    return "like"


@app.route("/delete/<post_id>", methods=["POST"])
def delete(post_id):
    """Route to delete a blog post."""
    return "delete"


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)