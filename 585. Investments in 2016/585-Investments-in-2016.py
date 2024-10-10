import pandas as pd

def find_investments(insurance: pd.DataFrame) -> pd.DataFrame:
    
    location = insurance.drop_duplicates(subset=['lat','lon'], keep=False)
    investments = insurance[insurance.duplicated(subset=['tiv_2015'], keep=False)]

    result = insurance[insurance['pid'].isin(location['pid']) & insurance['pid'].isin(investments['pid'])]

    return pd.DataFrame({'tiv_2016':[result['tiv_2016'].sum()]})