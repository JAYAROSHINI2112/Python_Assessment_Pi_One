from flask import Flask, render_template
import requests
import matplotlib.pyplot as plt
from dotenv import load_dotenv
from io import BytesIO
import base64,os
load_dotenv()
app = Flask(__name__)

def get_top_movies(api_key):
    url = f'https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=en-US&page=1'

    response = requests.get(url)
    if response.status_code == 200:
        movies = response.json()['results']
        return movies
    else:
        print(f"Failed to retrieve top movies. Status Code: {response.status_code}")
        return None

def create_rating_bar_chart(top_movies):
    # Extracting titles and ratings
    titles = [movie['title'] for movie in top_movies]
    ratings = [movie['vote_average'] for movie in top_movies]

    # Create a bar chart of top movie ratings using Matplotlib
    plt.figure(figsize=(10, 6))
    plt.barh(titles, ratings, color='skyblue')
    plt.xlabel('TMDb Rating')
    plt.title('Top Movies on TMDb')
    plt.xlim(0, 10)

    # Save the plot to a BytesIO object
    img_data = BytesIO()
    plt.savefig(img_data, format='png')
    img_data.seek(0)
    plt.close()

    # Convert the image data to base64 for embedding in HTML
    img_base64 = base64.b64encode(img_data.read()).decode('utf-8')
    return img_base64

@app.route('/')
def index():
    api_key = os.environ.get("API_KEY")
    top_movies = get_top_movies(api_key)

    if top_movies:
        img_base64 = create_rating_bar_chart(top_movies)
        return render_template('index.html', img_base64=img_base64)
    else:
        return "Failed to retrieve top movies."

if __name__ == "__main__":
    app.run(debug=True)
