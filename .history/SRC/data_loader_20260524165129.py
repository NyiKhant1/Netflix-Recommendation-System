import pandas as pd
import os 
def dataloader():
    movies = pd.read_csv('../Data/Raw/tmdb_5000_movies.csv')
    credits = pd.read_csv('../Data/Raw/tmdb_5000_credits.csv')

    df = movies.merge(credits, on='title')

    return df

file_path = 'D:\University of Sunderland\Netflix-Spotify-Recommendation-System - Copy\Data\Clean\cleaned_data.csv'
def delete_file ():
    if os.p