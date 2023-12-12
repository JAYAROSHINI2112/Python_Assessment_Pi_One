 # TMDb Web Scraping and Visualization

## Overview

This Python script demonstrates web scraping of movie data from The Movie Database (TMDb) using the TMDb API. The script retrieves information about the top-rated movies and creates a bar chart visualization of their ratings using the Matplotlib library.

## Features

- Retrieves top-rated movies from TMDb.
- Creates a bar chart of movie ratings using Matplotlib.
- Embeds the chart in an HTML page for easy visualization.

## Prerequisites

- Python 3
- Required Python packages: `requests`, `matplotlib`, `flask`

## Getting Started

1. **API Key:**
    - Obtain an API key from TMDb by signing up on their website.
    - Singup to www.themoviedb.org
    - Login in to themoviedb.org
    - Go to settings/api
    - Create an API key by providing input


2. **Install Dependencies:**
    ```bash
    pip install requests matplotlib Flask
    ```

3. **Run the Script:**
    ```bash
    python app.py
    ```

4. **Access the Visualization:**
    - Open your web browser and visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to view the top movies ratings chart.

## Project Structure

- `app.py`: Python script for web scraping and visualization.
- `templates/index.html`: HTML template for displaying the chart.

## Acknowledgments

- The Movie Database (TMDb) for providing the API.


<div align="center">
   <a href="https://ibb.co/nQS63q2"><img src="https://i.ibb.co/tY5QZwf/webscrapping-chart.png" alt="webscrapping-chart" border="0"></a>
</div>
