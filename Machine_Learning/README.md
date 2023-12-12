# Flask Sentiment Analysis

This project is a simple web-based Sentiment Analysis tool using Flask and NLTK's VADER sentiment analysis model.

## Purpose of the Project
The purpose of this project is to demonstrate how to create a web application for sentiment analysis. Users can input text, and the application will analyze the sentiment and display the sentiment score along with a classification of positive, negative, or neutral sentiment.

## Project Structure

- **`app.py`**: The main Flask application file.
- **`templates/index_sentiment.html`**: HTML template for the main page.
- **`templates/result_sentiment.html`**: HTML template to display the sentiment analysis result.

## Setup Instructions

1. Install the required libraries:

    ```bash
    pip install Flask nltk
    ```

2. Import the NLTK sentiment module:

    ```python
    import nltk
    nltk.download('vader_lexicon')
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

4. Open a web browser and go to `http://127.0.0.1:5000/`. You should see the main page with a text area for sentiment analysis.

## Usage

1. Enter text into the provided text area on the main page.

2. Click the "Analyze Sentiment" button.

3. The application will display the sentiment score along with a classification of positive, negative, or neutral sentiment.

4. To run the application locally, ensure that you have Python and the required libraries installed.

 <div style="text-align: center;">
        <h2>Top Movies Ratings</h2>
        <a href="https://ibb.co/k0mjQPq"><img src="https://i.ibb.co/4M1zP04/webscrapping-chart.png" alt="webscrapping-chart" border="0"></a>
  </div>
