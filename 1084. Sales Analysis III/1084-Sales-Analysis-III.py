import pandas as pd

def sales_analysis(product: pd.DataFrame, sales: pd.DataFrame) -> pd.DataFrame:
    
    merged = sales.merge(product, on = 'product_id', how='left')

    merged['sold_all'] = merged.groupby('product_id').transform('size')
    merged = merged[(merged['sale_date']<='2019-03-31') & (merged['sale_date']>='2019-01-01')]
    merged['sold_first'] = merged.groupby('product_id').transform('size')
    merged=merged[merged['sold_all']==merged['sold_first']][['product_id','product_name']].drop_duplicates()
    
    return merged