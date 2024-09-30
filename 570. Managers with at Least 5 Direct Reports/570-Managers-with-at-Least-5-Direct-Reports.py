import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    
    
    first = employee[(employee['managerId'].isnull()) | (employee['id'].isin(employee['managerId'].tolist()))]
    second = employee.groupby('managerId', as_index=False).size().rename(columns={'managerId':'id'})

    result = first.merge(second, on='id', how='left')

    return result[result['size']>=5][['name']]