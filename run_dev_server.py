"""
Startup script for starting flask server.
TODO: Alex needs to tell Szabi how to ignore errors in pylint.
"""
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    """dummy documentation string"""
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
