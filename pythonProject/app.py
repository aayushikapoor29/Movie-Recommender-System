import pandas as pd
import streamlit as st
import pickle
import requests


def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data = response.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_movie_posters  = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].id
        recommend_movies.append(movies.iloc[i[0]].title)
        recommend_movie_posters.append(fetch_poster(movie_id))
    return recommend_movies, recommend_movie_posters

movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl', 'rb'))
st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Hey!', movies['title'].values)
if st.button('Recommend'):
    names, poster = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    for i, col in enumerate([col1, col2, col3, col4, col5]):
        with col:
            st.text(names[i])
            st.image(poster[i])

  
