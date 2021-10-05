import pickle
import streamlit as st

def recommend(movie):
    index = movies[movies['Title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    for i in distances[1:6]:
        recommended_movie_names.append(movies.iloc[i[0]].Title)

    return recommended_movie_names

page_bg_img = '''
<style>
      .stApp {
  background-image: linear-gradient(rgba(0, 0, 0, 0.527),rgba(0, 0, 0, 0.5)) , url(https://i.imgur.com/9GyUbrB.jpeg);
  background-size: cover;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)





st.title('Cineguide - Movie Recommendation')
st.markdown('<style>h1{color : white;}</style>', unsafe_allow_html=True)



movies = pickle.load(open('movie_list.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movie_list = movies['Title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)


def header(obj):
     st.markdown(f'<p style="background-color:transparent;color:white;font-size:24px;border-radius:2%;font-weight:bold;">{obj}</p>', unsafe_allow_html=True)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend(selected_movie)
    for i in recommended_movie_names:
        header(i)
        
        
        
        
