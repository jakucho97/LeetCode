import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    
    ids = pd.DataFrame(set(products['product_id']), columns = ['product_id'])
    valid_dates = products[products['change_date']<='2019-08-16']
    valid_dates = valid_dates.loc[valid_dates.groupby(by='product_id')['change_date'].idxmax()]
    
    result  = ids.merge(valid_dates, on = 'product_id',how='left').fillna(10)

    return result.rename(columns={'new_price':'price'})[['product_id','price']]