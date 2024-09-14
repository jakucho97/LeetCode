import pandas as pd

def find_customers(customer: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
   
    grouped = customer.groupby(by='customer_id', as_index=False)['product_key'].apply(set)
    
    grouped = grouped[grouped['product_key']== set(product['product_key'])]

    return grouped[['customer_id']]   