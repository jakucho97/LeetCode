import pandas as pd

def capital_gainloss(stocks: pd.DataFrame) -> pd.DataFrame:

    grouped = stocks.groupby(by=['stock_name','operation'], as_index=False)['price'].sum()
    grouped['price'] = grouped.apply(lambda x: -x['price'] if x['operation']=='Buy' else x['price'], axis=1)
    grouped = grouped.groupby('stock_name', as_index=False)['price'].sum().rename(columns={'price':'capital_gain_loss'})

    

    return grouped
    