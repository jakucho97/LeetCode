import pandas as pd

def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:

    result = activities.sort_values(by='product').drop_duplicates().groupby('sell_date', as_index=False)['product'].apply(list)

    result['num_sold'] = result['product'].apply(len)
    result = result.rename(columns={'product':'products'})

    result['products'] = result['products'].apply(','.join)

    return result[['sell_date','num_sold','products']]
    