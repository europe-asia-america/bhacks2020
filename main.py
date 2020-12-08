from flask import Flask
from flask import render_template
from flask import url_for

app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static")


@app.route('/')
@app.route('/home')
def home():
    """Landing page route."""
    nav = [
            {"name": "Home", "url": url_for('home')},
            {"name": "About", "url": url_for('about')},
            {"name": "Add", "url": "https://example.com/3"},
            ]
    return render_template(
        "home.html",
        nav=nav,
        title="Increment",
        description="An incremental task management application.",
    )

@app.route('/about')
def about():
    """About page route."""
    nav = [
            {"name": "Home", "url": url_for('home')},
            {"name": "About", "url": url_for('about')},
            {"name": "Add", "url": "https://example.com/3"},
            ]
    return render_template(
        "home.html",
        nav=nav,
        title="About",
        description="An incremental task management application.",
    )

