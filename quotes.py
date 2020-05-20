import datetime
import json

from flask import Flask, render_template

app = Flask(__name__)

@app.template_filter('datetime')
def format_datetime(value):
    date = datetime.datetime.fromtimestamp(value)
    print(date.strftime('%Y-%m-%d %H:%M'))
    return date.strftime('%Y-%m-%d %H:%M')

@app.route('/')
def index():
    quotes = json.load(open('quotes.json'))
    return render_template('index.html', quotes=quotes[:20])

if __name__ == "__main__":
    app.run(port=5000, debug=True)