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
    - For now i will provide my Apikey value="f1f6529de171f7d0521bdde174d3b23a"

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

## Configuration

- Replace `'f1f6529de171f7d0521bdde174d3b23a'` in the script with your actual TMDb API key.

## Project Structure

- `app.py`: Python script for web scraping and visualization.
- `templates/index.html`: HTML template for displaying the chart.

## Acknowledgments

- The Movie Database (TMDb) for providing the API.


<div align="center">
    <img src="[https://i.ibb.co/9Z4QcG5/chart.png](https://ibb.co/b68NHtb)" alt="Top Movies Ratings Chart" width="800" height="500" />
</div>
