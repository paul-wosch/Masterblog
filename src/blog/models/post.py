"""Provide the Post class."""


class Post:
    """Represent a specific post in a blog."""

    def __init__(self, id: int, author: str, title: str, content: str, likes: int):
        """Create a new Post instance."""
        self.id = id
        self.author = author
        self.title = title
        self.content = content
        self.likes = likes

    def get(self):
        """Return a Post instance as dictionary."""
        return self.__dict__

    def update(self, author: str = None, title: str = None, content: str = None):
        """Change author, title or content of a Post instance."""
        if author:
            self.author = author
        if title:
            self.title = title
        if content:
            self.content = content

    def like(self):
        """Increment the like value by one."""
        self.likes += 1

    def set_id(self, id):
        """Set id for a Post instance."""
        self.id = id


def main():
    """Main function for testing."""


if __name__ == "__main__":
    main()
