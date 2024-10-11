import pandas as pd

def restaurant_growth(customer: pd.DataFrame) -> pd.DataFrame:
    
    mean = customer.groupby('visited_on', as_index=False)['amount'].sum()

    mean['sum']=mean['amount'].rolling(7).sum()

    result = pd.DataFrame({'visited_on':mean['visited_on'],'amount':mean['amount'].rolling(7).sum(),'average_amount':mean['amount'].rolling(7).mean().round(2)}).dropna()

    return result