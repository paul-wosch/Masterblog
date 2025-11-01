from flask import Flask, render_template, abort, redirect, url_for, request
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


@app.route("/show/<int:post_id>")
def show(post_id):
    """Show a single blog post."""
    post_obj = get_post_obj_or_404(post_id)
    return render_template('show.html', post=post_obj)


@app.route("/add", methods=["GET", "POST"])
def add(post=None):
    """Show a form for adding a blog post."""
    if request.method == 'POST':
        new_post = dict(request.form)
        my_blog.add(new_post)
        return redirect(url_for('index'))
    return render_template('add.html')


@app.route("/update/<int:post_id>", methods=["GET", "POST"])
def update(post_id):
    """Show a form for updating a blog post."""
    post_obj = get_post_obj_or_404(post_id)
    if request.method == 'POST':
        post_data = dict(request.form)
        my_blog.update(post_id=post_id, **post_data)
        return redirect(url_for('index'))
    return render_template('update.html', post=post_obj)


@app.route("/like/<int:post_id>", methods=["POST"])
def like(post_id):
    """Route to like a blog post.

    Redirect to single post view afterward.
    """
    post_obj = get_post_obj_or_404(post_id)
    post_obj.like()
    return redirect(url_for('show', post_id=post_id))


@app.route("/delete/<int:post_id>", methods=["POST"])
def delete(post_id):
    """Route to delete a blog post.

    Redirect to index route afterward.
    """
    post_obj = get_post_obj_or_404(post_id)
    my_blog.delete(post_obj)
    return redirect(url_for("index"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html', error=error), 404


def get_post_obj_or_404(post_id):
    """Return a post object for the given id or raise 404."""
    if not (post_obj := my_blog.get(post_id)):
        abort(404)
    return post_obj


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)