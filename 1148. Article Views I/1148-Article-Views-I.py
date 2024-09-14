import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    
    return pd.DataFrame(set(views[views['author_id']==views['viewer_id']]['author_id']), columns=['id']).sort_values(by='id')