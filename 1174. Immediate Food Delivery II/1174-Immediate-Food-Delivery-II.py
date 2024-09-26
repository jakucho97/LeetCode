import pandas as pd

def immediate_food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    
    first_orders = delivery.loc[delivery.groupby('customer_id')['order_date'].idxmin()]
    
   

    result = pd.DataFrame([len(first_orders[first_orders['order_date']==first_orders['customer_pref_delivery_date']])*100/len(first_orders)], columns=['immediate_percentage']).round(2)
    
    return result