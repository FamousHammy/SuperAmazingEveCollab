from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def top_150():
    return render_template('top-150.html')


if __name__ == '__main__':
    app.run()
