import pandas as pd

def rising_temperature(weather: pd.DataFrame) -> pd.DataFrame:
    
    result = weather.sort_values(by='recordDate', ascending=True)
    result = result[(result['temperature'].diff()>0) & (result['recordDate'].diff()=='1 days')]
    
    return result[['id']]