import pandas as pd

def project_employees_i(project: pd.DataFrame, employee: pd.DataFrame) -> pd.DataFrame:
    
    experiences = project.merge(employee, on = 'employee_id', how = 'left').groupby('project_id', as_index=False)['experience_years'].mean().round(2).rename(columns={'experience_years':'average_years'})

    return experiences