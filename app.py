import streamlit as st
import pickle
import requests
from PIL import Image
logo = Image.open("my photo.jpeg")
st.logo(logo,size='large',link='https://www.linkedin.com/in/udayan-amipara-637b21324/')
st.sidebar.header('Movie Recommendation System')
#add text in slidebar
st.sidebar.space('medium')
st.sidebar.write("This the Content Based Movie Recommendation System made with Tag similarity matching")
#contect information on sidebar
st.sidebar.header("Contact Me")
st.sidebar.write("Email: <a href='mailto:udayanamipara0808@gmail.com'>udayanamipara0808@gmail.com</a>", unsafe_allow_html=True)
st.sidebar.write("Phone: +91 9773031244")
st.sidebar.markdown("---") # Adds a horizontal line
st.sidebar.write("Connect with Me on:")
st.sidebar.write("LinkedIn: <a href='https://www.linkedin.com/in/udayan-amipara-637b21324/'>Udayan Amipara</a>",unsafe_allow_html=True)

st.title("Movie Recommendation System")
movies  = pickle.load(open('movies.pkl','rb'))
similarity_mat  = pickle.load(open('similarity.pkl','rb'))
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity_mat[movie_index]
    recommended_mv = []
    recommended_mv_poster = []
    top_5 = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    for i in top_5:
        mv_id = movies.iloc[i[0]].movie_id
        #fetch poster from API using id
        recommended_mv.append(movies.iloc[i[0]].title)
        recommended_mv_poster.append(movies.iloc[i[0]]['poster'])
    return recommended_mv,recommended_mv_poster
st.title("Content Based Movie Recommendation System")
st.header("Insert your movie here:")
st.divider()
selected_mv=st.selectbox("select a movie you watched :", movies['title'].values)

if st.button('Recommend'):
    list_mv, list_poster = recommend(selected_mv)
    col1, col2, col3, col4, col5 = st.columns(5)

    cols = [col1, col2, col3, col4, col5]

    for i in range(5):
        with cols[i]:
            st.text(list_mv[i])
            if list_poster[i]:
                st.image(list_poster[i])
            else:
                st.write("Poster not available")

st.feedback('stars')