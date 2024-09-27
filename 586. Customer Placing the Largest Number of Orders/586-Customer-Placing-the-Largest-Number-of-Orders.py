import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    
    grouped = orders.groupby('customer_number', as_index=False).count()
    
    return grouped[grouped['order_number'] == grouped['order_number'].max()][['customer_number']]