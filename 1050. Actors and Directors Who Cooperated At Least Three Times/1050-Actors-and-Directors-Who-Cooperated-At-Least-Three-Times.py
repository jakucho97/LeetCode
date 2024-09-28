import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    
    new = actor_director.groupby(by=['actor_id','director_id'], as_index=False).size()

    return new[new['size']>=3][['actor_id','director_id']]