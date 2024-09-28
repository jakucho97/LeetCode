import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    
    employee['rank']= employee.groupby(by='departmentId')['salary'].rank(method='dense', ascending=False)
    result = employee[employee['rank']==1].rename(columns={'name':'Employee'})
    department = department.rename(columns={'id':'departmentId','name':'Department'})

    result = result.merge(department, on='departmentId', how='left')

    return result[['Department','Employee','salary']]