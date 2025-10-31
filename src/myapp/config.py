"""Provide global constants for the project."""
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = Path("data")
DATA_PATH = (PROJECT_ROOT / DATA_DIR).resolve()
# blog storage
BLOG_FILE = Path("blog.json")
BLOG_FILE_PATH = (DATA_PATH / BLOG_FILE).resolve()
# sequence storage
SEQUENCE_FILE = Path("sequence.json")
SEQUENCE_FILE_PATH = (DATA_PATH / SEQUENCE_FILE).resolve()
# Flask templates folder
TEMPLATES_DIR = "templates"
TEMPLATES_PATH = (PROJECT_ROOT / TEMPLATES_DIR).resolve()
# Flask static folder
STATIC_DIR = "static"
STATIC_PATH = (PROJECT_ROOT / STATIC_DIR).resolve()
