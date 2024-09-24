import pandas as pd

def average_selling_price(prices: pd.DataFrame, units_sold: pd.DataFrame) -> pd.DataFrame:
    
    merged = units_sold.merge(prices, on = 'product_id', how='outer')
    merged['units'] = merged['units'].fillna(0)
    filtered = merged[((merged['purchase_date']>=merged['start_date']) & (merged['purchase_date']<=merged['end_date'])) | (merged['units']==0)]

    result = pd.DataFrame()
    result[['product_id','average_price']] = filtered.groupby(by='product_id', as_index=False).apply(lambda x: ((x['units']*x['price']).sum()/x['units'].sum()).round(2)).fillna(0)
    
    return result