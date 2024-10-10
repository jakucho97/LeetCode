import pandas as pd

def movie_rating(movies: pd.DataFrame, users: pd.DataFrame, movie_rating: pd.DataFrame) -> pd.DataFrame:
    
    merged = movie_rating.merge(movies, on='movie_id', how='left')

    merged = merged.merge(users, on = 'user_id', how='left')

    counted = movie_rating.groupby(by='user_id', as_index=False).size().merge(users, on='user_id', how='left').sort_values(by=['size','name'], ascending=[False, True])
    average = movie_rating[(movie_rating['created_at'].dt.month==2) & (movie_rating['created_at'].dt.year==2020)].groupby(by='movie_id', as_index=False)['rating'].mean().merge(movies, on='movie_id', how='left').sort_values(by=['rating','title'], ascending=[False, True])

    return pd.DataFrame({'results':[counted.iloc[0,2],average.iloc[0,2]]})