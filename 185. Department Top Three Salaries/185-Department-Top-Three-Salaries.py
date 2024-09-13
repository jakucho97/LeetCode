import pandas as pd

def top_three_salaries(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    employee['rank'] = employee.groupby(by='departmentId').salary.rank(method='dense', ascending=False)
    result = employee[employee['rank']<=3].sort_values(by=['departmentId','salary'], ascending=[True,False])
    department=department.rename(columns={'name':'Department','id':'departmentId'})

    final = result.merge(department,how='left',on='departmentId')
    final=final.rename(columns={'name':'Employee','salary':'Salary'})
    return final[['Department','Employee','Salary']]
    return result[['Department','Employee','Salary']]