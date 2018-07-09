__author__ = 'cosmic'
from flask import Flask
print __name__
app = Flask(__name__)

# @app.route('/')
def hello_world():
    return "Hello, World!"

app.add_url_rule("/", 'hello_world', hello_world)

if __name__ == '__main__':
    app.run()