import pandas as pd

def market_analysis(users: pd.DataFrame, orders: pd.DataFrame, items: pd.DataFrame) -> pd.DataFrame:
    orders_2019 = orders[orders['order_date'].dt.year == 2019].groupby(by='buyer_id', as_index=False).size()

    result = users.rename(columns={'user_id':'buyer_id'})
    result = result.merge(orders_2019,on='buyer_id', how='left').drop(['favorite_brand'],axis=1)
    result=result.rename(columns={'size':'orders_in_2019'}).fillna(0)
    return result