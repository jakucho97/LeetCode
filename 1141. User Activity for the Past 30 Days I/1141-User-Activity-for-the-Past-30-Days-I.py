import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    
    activity = activity[(activity['activity_date']>pd.to_datetime('2019-07-27')- pd.Timedelta(days=30) ) & (activity['activity_date']<='2019-07-27')]

    activity = activity.groupby(by=['activity_date'], as_index=False)['user_id'].nunique()

    return activity.rename(columns={'activity_date':'day','user_id':'active_users'})