from flask import Flask, render_template
from operator import itemgetter

app = Flask(__name__)


@app.route('/')
def top_150():
    '''this is just a placeholder for now, but demonstrates the structure we need'''
    items = [['Weak Pea Shooter Thing', 3],
             ['Super Ridiculous Ion Cannon', 7]]
    sorted_items = sorted(items, key=itemgetter(1), reverse=True)
    return render_template('top-150.html', items=sorted_items)


if __name__ == '__main__':
    app.run()
