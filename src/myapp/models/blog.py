"""Provide the Blog class."""
from myapp.models.post import Post
from myapp.storage import read_json_file, write_json_file, get_next_id, save_id_to_sequence
from myapp.config import BLOG_FILE_PATH


class Blog:
    """Manage a collection of blog posts."""

    def __init__(self, blog_data: list = None):
        """Initialize a Blog instance."""
        self.posts = None
        self.load_blog(blog_data)

    def get(self, id):
        """Return a single post object by its id or None if no matching was found."""
        return next((post for post in self.posts if post.id == id), None)

    def get_posts(self):
        """Return all posts as a list of dictionaries."""
        return [post.get() for post in self.posts]

    def add(self, post: dict | Post = None, **kwargs):
        """Add a post to the collection.

        Input:
            - post object instance
            - post as dictionary
            - post as key-word arguments
        """
        # -------------------------------------------------------------
        # Reference given or create new Post instance
        if isinstance(post, Post):
            new_post = post
        elif isinstance(post, dict):
            new_post = Post(**post)
        else:
            new_post = Post(**kwargs)
        # -------------------------------------------------------------
        # Auto increment id for new post and update sequence
        new_post.set_id(get_next_id("post"))
        self.posts.append(new_post)
        save_id_to_sequence("post", new_post.get_id())
        self.save_blog()

    def update(self, post_id=None, post_object=None, **kwargs):
        """Update a post in the collection.

        Accepted input:
            - post id or post object instance
            - key-word arguments providing updated fields
            - ...or a dictionary passed as **dictionary instead
        """
        # Validate input
        if post_id is None and post_object is None:
            raise TypeError("Missing argument: post_object or post_id.")
        # Use existing post object or get one from post id
        if post_object is None:
            post_object = self.get(post_id)
        # Update post and save blog posts
        post_object.update(**kwargs)
        self.save_blog()

    def like(self, post_id=None, post_object=None):
        """Like a post in the collection.

        Accepted input:post id or post object instance
        """
        # Validate input
        if post_id is None and post_object is None:
            raise TypeError("Missing argument: post_object or post_id.")
        # Use existing post object or get one from post id
        if post_object is None:
            post_object = self.get(post_id)
        # Like post and save blog posts
        post_object.like()
        self.save_blog()

    def delete(self, post):
        """Delete the given post from the collection."""
        self.posts.remove(post)
        self.save_blog()

    def save_blog(self):
        """Save the current collection of posts persistently."""
        write_json_file(BLOG_FILE_PATH, self.get_posts())

    def load_blog(self, blog_data: list = None):
        """Load blog data from argument or persistent storage."""
        if blog_data is None:
            blog_data = read_json_file(BLOG_FILE_PATH)
        self.posts = [Post(**item) for item in blog_data]


def main():
    """Main function for testing."""


if __name__ == "__main__":
    main()
