from flask import Flask
import pandas as pd
import pickle

app = Flask(__name__)

movies = pickle.load(open('Data/Model/movies.pkl', 'rb'))
similartiy = pickle.load(open('Data/Model/similarity.pkl', 'rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]

    distances = similartiy[movie_index]

    movies_list = sorted(
        list(enumerate(distances)),
        reverse=True,
        key=lambda x: x[1]
    )[1:6]

    recommended_movies = []

    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)

    return recommended_movies

print (recommend('Avatar'))

if __name__ == '__main__':
    app.run(debug=True)