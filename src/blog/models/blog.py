"""Provide the Blog class."""
from post import Post
from blog.storage.filestore import read_json_file, write_json_file
from blog.storage.sequence import get_next_id, save_id_to_sequence

TEMP_POST_ID = -1


class Blog:
    """Manage a collection of blog posts."""

    def __init__(self, blog_posts: list):
        """Initialize a Blog instance."""
        self.posts = [Post(**item) for item in blog_posts]

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
        new_post.set_id(TEMP_POST_ID)
        new_post.set_id(get_next_id("post"))
        self.posts.append(new_post)
        save_id_to_sequence(new_post.id)

    def delete(self, post):
        """Delete the given post from the collection."""
        self.posts.remove(post)

    def save_blog(self):
        """Save the current collection of posts persistently."""


def main():
    """Main function for testing."""
    """
    blog_posts = [{"id": 1, "author": "John Doe", "title": "First Post", "content": "This is my first post.", "likes": 0},
                  {"id": 2, "author": "Jane Doe", "title": "Second Post", "content": "This is another post.", "likes": 0},
                  {"id": 3, "author": "Anonymous", "title": "Third Post", "content": "This is another post.", "likes": 0},
                  {"id": 4, "author": "Mad Max", "title": "Forth Post", "content": "This is another post.", "likes": 0},
                  {"id": 5, "author": "Lisa Max", "title": "Fifth Post", "content": "This is another post.", "likes": 0},

    ]"""
    # """
    my_blog = Blog(read_json_file("data/test.json"))
    print(my_blog.get(1).content)
    print(my_blog.get_posts())
    """
    my_blog.get(1).update(author="Test")
    print(my_blog.get_posts())
    my_blog.delete(my_blog.get(1))
    print(my_blog.get_posts())
    """
    # """


if __name__ == "__main__":
    main()
