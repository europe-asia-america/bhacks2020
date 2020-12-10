from flask import Flask
from flask import render_template
from flask import url_for
from flask import redirect
from add import AddTask
from taskfeedbackform import TaskFeedbackForm
import task

CURRENT_TASK = None

app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static")
import os
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
@app.route('/home', methods=['GET', 'POST'])
def home():
    """Homepage with tasks."""
    nav = [
            {"name": "Home", "url": url_for('home')},
            {"name": "About", "url": url_for('about')},
            {"name": "Add", "url": url_for('add')},
            ]
    CURRENT_TASK = task.get_next_task()
    ID = CURRENT_TASK["id"] if CURRENT_TASK else None
    form = TaskFeedbackForm(hidden_id=ID)
    if form.validate_on_submit():
        # use task.py feedback functions
        if form.hidden_id.data != '':
            ID = int(form.hidden_id.data)
            if form.skip.data and ID != None:
                print(ID)
                task.skip_task(ID)
            elif form.progress.data and ID != None:
                task.progress_task(ID)
            elif form.done.data and ID != None:
                task.mark_task_as_done(ID)
            elif form.delete.data and ID != None:
                task.delete_task(ID)
            else:
                raise Exception("What is going on?")
            return redirect(url_for('home'))
    return render_template(
        "task_view.html",
        nav=nav,
        title="Increment",
        task=CURRENT_TASK,
        form=form
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
        description="A task recommendation system for personal use.",
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
        task.add_new_task(form.description.data, form.project.data, form.due.data)
        return redirect(url_for('add_success'))
    return render_template(
            'add.html',
            nav=nav,
            title="Add",
            description="Add new task. Description is mandatory.",
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

