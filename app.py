from textblob import TextBlob
from flask import Flask
app = Flask(__name__)

@app.route('/<message>')
def index(message):
    sentiment = "positive"
    if (TextBlob(message).sentiment.polarity < 0.0):
        sentiment = "negative"

    return app.make_response(sentiment)

@app.route('/')
def main():
    return app.make_response("hello")