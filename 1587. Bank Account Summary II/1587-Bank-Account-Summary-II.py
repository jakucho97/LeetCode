import pandas as pd

def account_summary(users: pd.DataFrame, transactions: pd.DataFrame) -> pd.DataFrame:
    

    transactions = transactions.groupby('account', as_index=False)[['amount']].sum()
    result = transactions.merge(users, on='account', how='left')[transactions['amount']>10000]
     


    return result.rename(columns={'amount':'balance'})[['name','balance']]