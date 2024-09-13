import pandas as pd

def top_travellers(users: pd.DataFrame, rides: pd.DataFrame) -> pd.DataFrame:
    distances = rides.groupby(by=['user_id']).sum()
    users = users.rename(columns={'id':'user_id'})

    result = distances.merge(users, on=['user_id'], how='right')[['name','distance']].sort_values(by=['distance'], ascending=False).rename(columns={'distance':'travelled_distance'}).fillna(0)

    return result