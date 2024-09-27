import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    
    orders_persons = sales_person.merge(orders, on = 'sales_id', how='left')

    all = orders_persons.merge(company, on = 'com_id', how = 'left')

    all = all.groupby('name_x', as_index=False)['name_y'].apply(list)

    return all[all['name_y'].apply(lambda x: 'RED' not in x)].rename(columns={'name_x':'name'})[['name']]