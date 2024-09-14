import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    result = employees.groupby(by=['emp_id','event_day'], as_index=False).sum().rename(columns={'event_day':'day'})
    result['total_time']=(result['in_time']-result['out_time']).abs()
    
    return result[['day','emp_id','total_time']]