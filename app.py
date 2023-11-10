import streamlit as st
import pickle
import pandas as pd
import requests

st.header("Welcome to")
st.title("MOVIE PLAZA")

st.markdown(
    """
    <style>
    .stApp{
        background-color: black;
        color: white;  
    }
    .css-183lzff{
        color: white;
    }
    .css-10trblm{
        color: lavenderblush;
        font-family: sans-serif;
    }
    .css-16idsys p{
        color: lavenderblush;
        margin-bottom:15px;
        font-family: sans-serif;
    }
    .css-1vbkxwb p{
        color: white;
        font-weight: 600;
        font-family: sans-serif;
    }
    .st-c5{
        cursor: auto;
        font-family: sans-serif;
        font-weight: 600;
        background-color: antiquewhite;
    }
    .css-uf99v8{
        background-image: url("https://wallpapercave.com/wp/wp1945939.jpg");
        background-size: cover;
        background-color: darkred;
        background-blend-mode:darken;
    }
    .css-7ym5gk{
        background-color: black;
        border-color: white; 
    }
     @media (max-width: 768px) {
        element.style {
            width: 260px;
        }
     }
    
    """, unsafe_allow_html=True
)




def fetch_poster(movie_id):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" +data['poster_path']
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_poster = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch poster from API
        recommended_movies_poster.append(fetch_poster(movie_id))
    return recommended_movies,recommended_movies_poster

movies_dict = pickle.load(open('movie_dict.pkl','rb'))
movies = pd.DataFrame(movies_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

selected_movie_name = st.selectbox(
    "Movie name please?",
    movies['title'].values)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])
