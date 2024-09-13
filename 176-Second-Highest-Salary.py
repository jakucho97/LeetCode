import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_salary = employee.sort_values(by=['salary'], ascending=False).drop_duplicates(subset=['salary'])

    result = pd.DataFrame()

    if len(sorted_salary)<2:
        result['SecondHighestSalary']=[None]
    else:
        result['SecondHighestSalary']=[sorted_salary.iloc[1,1]]
    
    return result