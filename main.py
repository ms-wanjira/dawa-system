from os import rename
from flask import Flask,render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/insights')
def insights():
    return render_template('insights.html')

@app.route('/sales')
def sales():
    return render_template('sales.html')

@app.route('/inventories')
def inventories():
    return render_template('inventories.html')
    


app.run(debug=True)