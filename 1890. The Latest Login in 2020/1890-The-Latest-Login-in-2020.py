import pandas as pd

def latest_login(logins: pd.DataFrame) -> pd.DataFrame:
    
    result = logins[logins['time_stamp'].dt.year==2020].rename(columns={'time_stamp':'last_stamp'}).groupby(by='user_id', as_index=False).max()
    

    return result