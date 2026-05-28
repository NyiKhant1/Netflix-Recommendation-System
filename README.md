# Netflix Recommendation System

A simple content-based movie recommendation system built using **Python, Flask, Pandas, and Scikit-learn**.  
It recommends similar movies based on cosine similarity of movie features.

## Features

- Recommend top similar movies based on a selected movies
- Content-based filtering using similarity matrix
- Flask for the backend
- Precomputed model using pickle for fast predictions

---

## How it works

The system uses a **precomputed similarity matrix** between movies.  
When a user selects a movie:

1. The movie index is found from the dataset
2. Similarity scores are retrieved
3. Movies are sorted based on similarity score
4. Top 7 similar movies are returned

## Project Structure

Data/ 
└── raw (original datasets )

└── Clean (clean data)

└── processed (preprocesside data)

└── Ready (ready for model to compare)

└── Model (trained artifacts (movies.pkl, similarity.pkl))

Notebook/ 
└── 1_eda.ipynb(for data exploration)

└── 2_data_cleaning.ipynb (for data cleaning)

└── 3_data_preprocessing.ipynb (for preprocessing data)

└── 4_feature_engineering.ipynb (feature work)

└── model.ipynb (training)

SRC/ 
└── data_cleaning.py

└── data_loader.py

└── data_preprocessing.py

└── extract_names.py

## Tech Stacks

- Python 
- Flask 
- Pandas 
- Scikit-learn 
- Pickle (model serialization)


## Run the application

Install dependencies

pip install flask pandas scikit-learn

Enter the movies name in app.py

print (recommend('Movies Name'))

--> python app.py

## Example Output

recommend("Harry Potter and the Half-Blood Prince")

['Harry Potter and the Order of the Phoenix', 
'Harry Potter and the Chamber of Secrets', 
"Harry Potter and the Philosopher's Stone", 
'Harry Potter and the Goblet of Fire', 
'Harry Potter and the Prisoner of Azkaban', 
'Ask Me Anything', 
'Red Riding Hood']

## Notes 

- Ensure movies.pkl and similarity.pkl exist in Data/Model/
- Movie title must match exactly (case-sensitive)
- This is a content-based recommender, not collaborative filtering

## Future Improvements

Build frontend UI (React / HTML templates)
Add search autocomplete for movies
Deploy on Heroku / Render / AWS
Improve model with NLP + embeddings

## Author 
Nyi Khant Zaw (Nicky)
