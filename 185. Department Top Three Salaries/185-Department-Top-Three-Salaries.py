import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['rank'] = employee.groupby(by='departmentId')['salary'].rank(method='dense', ascending=False)
    employee = employee.sort_values(by=['departmentId','salary'], ascending=[True,False]).rename(columns={'name':'Employee', 'salary':'Salary'})
    department = department.rename(columns={'id':'departmentId'})
    result = employee[(employee['rank']<=3)].merge(department, how='left', on='departmentId').rename(columns={'name':'Department'})
    return result[['Department','Employee','Salary']]