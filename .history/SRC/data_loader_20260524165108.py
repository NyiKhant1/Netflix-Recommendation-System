import pandas as pd
import os 
def dataloader():
    movies = pd.read_csv('../Data/Raw/tmdb_5000_movies.csv')
    credits = pd.read_csv('../Data/Raw/tmdb_5000_credits.csv')

    df = movies.merge(credits, on='title')

    return df

file_path = 
def delete_file ()