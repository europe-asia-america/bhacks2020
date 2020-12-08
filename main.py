from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from add import AddTask
import task


app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static")
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
@app.route('/home')
def home():
    """Landing page route."""
    nav = [
            {"name": "Home", "url": url_for('home')},
            {"name": "About", "url": url_for('about')},
            {"name": "Add", "url": url_for('add')},
            ]
    return render_template(
        "task_view.html",
        nav=nav,
        title="Increment",
        task=task.get_next_task()
    )

@app.route('/about')
def about():
    """About page route."""
    nav = [
            {"name": "Home", "url": url_for('home')},
            {"name": "About", "url": url_for('about')},
            {"name": "Add", "url": url_for('add')},
            ]
    return render_template(
        "home.html",
        nav=nav,
        title="Increment",
        description="An incremental task management application.",
    )


@app.route('/add', methods=('GET', 'POST'))
def add():
    """Form to add task"""
    nav = [
            {"name": "Home", "url": url_for('home')},
            {"name": "About", "url": url_for('about')},
            {"name": "Add", "url": url_for('add')},
            ]
    form = AddTask()
    if form.validate_on_submit():
        return redirect(url_for('add_success'))
    return render_template(
            'add.html',
            nav=nav,
            title="Add",
            description="Add new task.",
            form=form
            )

@app.route('/add_success')
def add_success():
    nav = [
            {"name": "Home", "url": url_for('home')},
            {"name": "About", "url": url_for('about')},
            {"name": "Add", "url": url_for('add')},
            ]
    return render_template(
            'home.html',
            nav=nav,
            title="Success!",
            description="You have successfully submitted a task."
            )

