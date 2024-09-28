import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    
    result = queue.sort_values(by='turn')
    result['cumsum']=result['weight'].cumsum()


    return result[result['cumsum']<=1000].tail(1)[['person_name']]