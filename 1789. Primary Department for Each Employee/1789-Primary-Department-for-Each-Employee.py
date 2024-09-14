import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    
    result = employee[(~employee.duplicated(subset=['employee_id'], keep=False)) | (employee['primary_flag']=='Y')]

    return result[['employee_id','department_id']]