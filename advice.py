import requests
from flask import Flask, render_template, request

app = Flask(__name__)

url = 'https://api.adviceslip.com/advice'
response = requests.get(url).json()
advice = response['slip']['advice']

def update_advice():
    url = 'https://api.adviceslip.com/advice'
    response = requests.get(url).json()
    global advice
    advice = response['slip']['advice']

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        update_advice()
        return render_template("home.html", advice = advice)

    else:
        return render_template('home.html', advice = advice)

if __name__ == '__main__':
    app.run()