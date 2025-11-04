# Masterblog 📝

![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Flask](https://img.shields.io/badge/flask-2.x-lightgrey)
![Code style: PEP8](https://img.shields.io/badge/code%20style-PEP8-yellow)
![Status](https://img.shields.io/badge/status-learning--project-orange)
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
[![Quick Start](https://img.shields.io/badge/⚡-Quick%20Start-orange)](#-quick-start)

---

## 📑 Table of Contents  

- [⚠️ Disclaimer](#-disclaimer)  
- [📝 Description](#-description)  
- [✨ Features](#-features)  
- [🛠️ Tech Stack](#-tech-stack)  
- [📦 Key Dependencies](#-key-dependencies)  
- [📁 Project Structure](#-project-structure)  
- [🛠️ Development Setup](#-development-setup)  
  - [🚀 Quick Start](#-quick-start)  
  - [📖 Step‑by‑Step Guide](#-step-by-step-guide)  
- [👥 Contributing](#-contributing)  
- [📄 License](#-license)  

---

## ⚠️ Disclaimer  
This project was created as part of my learning journey during a multi‑month software engineering course. It should be viewed as such: a work in progress where I applied my best effort and current knowledge. The focus of this project was on **Object‑Oriented Programming (OOP)**, **Flask**, **Jinja2 templates**, and **Python packaging**. While not production‑ready, it reflects my growth and dedication to learning software engineering principles.

---

## 📝 Description  
**Masterblog** is a simple blogging application built with Flask. It allows users to create, view, update, delete, and like blog posts. Posts are stored in JSON files with auto‑incrementing IDs, simulating database‑like persistence without requiring a database server.  

The project demonstrates:  
- Clean separation of concerns (models, storage, app, templates).  
- Use of Flask with Jinja2 templates and CSS styling.  
- JSON‑based persistence with sequence tracking for IDs.  
- OOP design with `Blog` and `Post` classes.  
- A progression from backend foundations to a functional web UI (as seen in the commit history).  

---

## ✨ Features  
- 📋 Display a list of blog posts  
- 🔍 View a single blog post  
- ➕ Add new blog posts  
- ✏️ Update existing blog posts  
- ❌ Delete blog posts  
- ❤️ Like posts with instant feedback  
- 🖼️ Styled UI with reusable templates and centralized layout  
- ⚡ JSON persistence with auto‑increment IDs  

---

## 🛠️ Tech Stack  
- **Language:** Python 3  
- **Framework:** Flask  
- **Templating:** Jinja2  
- **Styling:** CSS  
- **Persistence:** JSON file storage with sequence tracking  
- **Packaging:** `pyproject.toml` with setuptools  

---

## 📦 Key Dependencies  
- [Flask](https://flask.palletsprojects.com/) – lightweight web framework  
- Python standard library (`pathlib`, `json`, etc.)  

---

## 📁 Project Structure  

```
.
├── .gitignore           # Ignore sensitive/generated files
├── LICENSE              # MIT license text
├── pyproject.toml       # Project metadata and dependencies
├── README.md            # Project documentation
├── Data            	 # JSON data storage
│   └── .gitkeep		 # Keeps Data dir in Git
├── src/                 # Main application source code
│   └── masterblog
│       ├── app.py       # Flask app with routes
│       ├── config.py    # Centralized configuration and paths
│       ├── models/      # Data models
│       │   ├── blog.py  # Blog class managing posts
│       │   └── post.py  # Post class with attributes and methods
│       └── storage/     # Persistence layer
│           ├── filestore.py  # JSON read/write helpers
│           └── sequence.py   # Auto-increment ID handling
├── static/              # Static assets
│   └── style.css        # Stylesheet for UI
└── templates/           # Jinja2 templates
    ├── base.html        # Base layout
    ├── index.html       # Homepage with posts list
    ├── post.html        # Partial for rendering a post
    ├── show.html        # Single post view
    ├── add.html         # Add post form
    ├── update.html      # Update post form
    ├── form.html        # Shared form partial
    └── 404.html         # Custom error page
```

---

## 🛠️ Development Setup  

### 🚀 Quick Start  
For experienced users who just want to get the app running:  
```bash
git clone https://github.com/paul-wosch/Masterblog.git \
&& cd Masterblog \
&& pip install -e . \
&& python src/masterblog/app.py
```
Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.  
On a fresh install, you’ll see a message with a link to **Add Post**.  

---

### 📖 Step‑by‑Step Guide  
1. **Clone the repository**:  
   ```bash
   git clone https://github.com/paul-wosch/Masterblog.git
   cd Masterblog
   ```

2. **Create virtual environment** (optional):  
   ```bash
   python -m venv .venv
   ```

3. **Activate virtual environment** (optional):  
   ```bash
   source .venv/bin/activate   # Mac/Linux
   .venv\Scripts\activate      # Windows
   ```

4. **Install local package**:  
   ```bash
   pip install -e .
   ```

5. **Run the app**:  
   ```bash
   python src/masterblog/app.py
   ```

6. **Access the app**:  
   Open your browser and go to [http://127.0.0.1:5000](http://127.0.0.1:5000).  
   - On a fresh install, no posts will be listed.  
   - You’ll see a message with a link to **Add Post**.  
   - Use that link to create your first blog entry.  

7. **Stop the server and deactivate environment** (optional):  
   - Stop the Flask server with `CTRL+C` in the terminal.  
   - Then deactivate the virtual environment:  
     ```bash
     deactivate
     ```

The `pip install -e .` makes `masterblog` importable, ensuring `app.py` can resolve imports correctly.  

---

## 👥 Contributing  
This project is primarily a learning exercise, but contributions, suggestions, or feedback are welcome. If you’d like to propose improvements:  
1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/your-feature`)  
3. Commit your changes (`git commit -m "feat: Add your feature"`)  
4. Push to the branch (`git push origin feature/your-feature`)  
5. Open a Pull Request  

---

## 📄 License
This project is licensed under the terms of the [MIT License](./LICENSE).
See the LICENSE file for full details.