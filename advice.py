import requests
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

def generate_new_advice():
    url = 'https://api.adviceslip.com/advice'
    response = requests.get(url).json()
    advice = response['slip']['advice']
    return advice


first_advice = generate_new_advice()


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', advice = first_advice)

if __name__ == '__main__':
    app.run()