from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '¡Hola! Mi web en Azure funciona correctamente.'

if __name__ == '__main__':
    app.run()
