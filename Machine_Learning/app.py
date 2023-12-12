from flask import Flask, render_template, request
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

# Download the VADER Lexicon
nltk.download('vader_lexicon')
app = Flask(__name__)

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze_sentiment():
    if 'text' in request.form:
        user_text = request.form['text']
        # Analyze sentiment using VADER
        sentiment_score = sia.polarity_scores(user_text)['compound']

        return render_template('index.html', user_text=user_text, sentiment_score=sentiment_score,method=True)

    return render_template('index.html', error=True,method=False)

if __name__ == '__main__':
    app.run(debug=True)
