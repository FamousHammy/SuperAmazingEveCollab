from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hammy is definitely the coolest person I know. But Steven will always be smarter.'


if __name__ == '__main__':
    app.run()
