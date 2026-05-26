import pandas as pd
import os 
def dataloader():
    movies = pd.read_csv('../Data/Raw/tmdb_5000_movies.csv')
    credits = pd.read_csv('../Data/Raw/tmdb_5000_credits.csv')

    df = movies.merge(credits, on='title')

    return df

def load_clean_data():
    cleaned_data_path = '../Data/Clean/cleaned_data.csv'
    df = pd.read_csv(cleaned_data_path)
    return df

def load_data(path):
    if not os.path.exists(path):
        raise FileNotFoundError(f"The file {path} does not exist.")
    
    df = pd.read_csv(path)
    return df