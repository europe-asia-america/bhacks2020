from flask import Flask
app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static")

@app.route('/')
def hello_world():
    return 'Hello, World!'