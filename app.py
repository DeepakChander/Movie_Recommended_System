import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    response = requests.get('/https://api.themoviedb.org/3/movie/{'}?api_key=6b0b0e27d6edbd99baa8b050b82824b1&language=en-US'.format(movie_id))
    data = response.json()
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]  # Fetching the index
    distances = similarity[movie_index]  # Measuring the similarity and distace wih all movies
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]  #

    recommend_movies =[]
    recommend_movies_poster = []
    for i in movie_list:
        movie_id = i[0]
        #fetch poster from API
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movies_poster.append(fetch_poster(movie_id))
    return recommend_movies,recommend_movies_poster

# Load the movie dictionary from the pickle file
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

# Streamlit app title
st.title('Movie Recommender System')

# Dropdown for movie selection
selected_movie_name = st.selectbox(
    'Select the movie',
    movies['title'].values  # Use the DataFrame to access movie titles
)

# Display the selected movie
st.write(f"You selected: {selected_movie_name}")

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    for i in recommendation:
        st.write(i)