import pandas as pd

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    
    
    lista=[]
    for i in range (len(stadium)-2):
        if stadium.iloc[i]['people']>=100 and stadium.iloc[i+1]['people']>=100 and stadium.iloc[i+2]['people']>=100:
            lista = lista+(stadium.iloc[i:i+3].values.tolist())
    
    result = pd.DataFrame(lista, columns=['id','visit_date','people'])
    
    return result.drop_duplicates()