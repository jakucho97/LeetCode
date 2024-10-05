import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    
    activity['timestamp']=activity.apply(lambda x: -x['timestamp'] if (x['activity_type']=='start') else x['timestamp'], axis=1)
    activity = activity.groupby(by=['machine_id','process_id'], as_index=False)['timestamp'].sum()
    activity = activity.groupby('machine_id', as_index=False)['timestamp'].mean().round(3).rename(columns={'timestamp':'processing_time'})
    
    
    return activity