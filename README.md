
# Content based **Movie Recommendation System**.

A content-based Movie Recommendation Web App built using **Machine Learning** and **Streamlit**, which **suggests similar movies** based on user selection and displays movie posters using the **TMDB POSTERS**.

🔗 Live App:
[**https://movie-recommender-system-9gidw4bcivwireegktvxrc.streamlit.app/**](https://movie-recommender-system-9gidw4bcivwireegktvxrc.streamlit.app/)

 ### 1.Features

 1.Recommend movies based on similarity

 2.Content-based filtering using cosine similarity

 3.Fetches movie posters from TMDB API

 4.Fast & interactive UI using Streamlit

 5.Pre-computed similarity matrix for efficiency

### 2.Tech Stack

1.Python

2.Streamlit

3.Pandas

4.NumPy

5.Scikit-learn

6.TMDB API

### 3.How It Works

1.Movie data is processed and vectorized.

2.Cosine similarity is used to compute similarity between movies.

3.When a user selects a movie:

4.Top similar movies are retrieved.

5.Posters are fetched using TMDB POSTER_PATH.

6.Results are displayed via Streamlit UI.

### Installation & Setup (Local)
git clone https://github.com/your-username/movie-recommender-system.git
cd movie-recommender-system
pip install -r requirements.txt

## Dataset Info:
Movie dataset sourced from TMDB / Kaggle
Preprocessed before training
**Link**: [https://www.kaggle.com/datasets/sakshisemalti/movies-dataset-with-posters](https://www.kaggle.com/datasets/sakshisemalti/movies-dataset-with-posters)

### Contributions:
Contributions are welcome!

### Acknowledgements

1.TMDB API
2.Streamlit Community
3.Scikit-learn Documentation