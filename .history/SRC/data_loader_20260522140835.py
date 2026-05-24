import pandas as pd
def dataloader():
    movies = pd.read_csv('../Data/Raw/tmdb_5000_movies.csv')
    credits = pd.read_csv('../Data/Raw/tmdb_5000_credits.csv')

    df = movies.merge(credits, on='title')

    return df