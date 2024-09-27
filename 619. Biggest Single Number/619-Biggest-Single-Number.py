import pandas as pd

def biggest_single_number(my_numbers: pd.DataFrame) -> pd.DataFrame:
    
    
    return pd.DataFrame(my_numbers.drop_duplicates(keep=False).max(), columns=['num'])