import pandas as pd

def triangle_judgement(triangle: pd.DataFrame) -> pd.DataFrame:
    
    triangle['triangle']=triangle.apply(lambda x: 'Yes' if ((x['x']+x['y']>x['z']) & (x['x']+x['z']>x['y']) & (x['y']+x['z']>x['x'])) else 'No', axis=1)

    return triangle