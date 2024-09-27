import pandas as pd

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    
   
    transactions['trans_date'] = pd.to_datetime(transactions['trans_date']).dt.strftime('%Y-%m')

    
    
    countries_total_amount = transactions.groupby(by=['country','trans_date'], as_index=False, dropna=False)['amount'].sum().rename(columns={'amount':'trans_total_amount'})

    countries_approved_amount = transactions[transactions['state']=='approved'].groupby(by=['country','trans_date'], as_index=False, dropna=False)['amount'].sum().rename(columns={'amount':'approved_total_amount'})
    
    approved_count = transactions[transactions['state']=='approved'].groupby(by=['country','trans_date'], as_index=False, dropna=False).size().rename(columns={'size':'approved_count'})
    
    all_count = transactions.groupby(by=['country','trans_date'], as_index=False, dropna=False).size().rename(columns={'size':'trans_count'})
    
    dfs = [approved_count,countries_total_amount,countries_approved_amount]

    for x in dfs:
        all_count = all_count.merge(x, on = ['country','trans_date'], how = 'left')
    
    all_count = all_count.rename(columns={'trans_date':'month'})
    all_count[['trans_count','approved_count','trans_total_amount','approved_total_amount']] = all_count[['trans_count','approved_count','trans_total_amount','approved_total_amount']].fillna(0)


    return all_count