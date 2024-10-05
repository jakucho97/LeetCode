import pandas as pd

def users_percentage(users: pd.DataFrame, register: pd.DataFrame) -> pd.DataFrame:
    
    grouped = register.groupby('contest_id', as_index=False)['user_id'].apply(list)
    
    grouped['percentage']=(100*grouped['user_id'].apply(len)/len(users)).round(2)

    return grouped.sort_values(by=['percentage','contest_id'], ascending=[False,True])[['contest_id','percentage']]