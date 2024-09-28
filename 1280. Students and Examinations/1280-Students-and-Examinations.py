import pandas as pd

def students_and_examinations(students: pd.DataFrame, subjects: pd.DataFrame, examinations: pd.DataFrame) -> pd.DataFrame:
    
    merged = students.merge(subjects, how='cross')

    examinations = examinations.groupby(by=['student_id','subject_name'], as_index=False).size()
    merged = merged.merge(examinations,on=['student_id','subject_name'], how='left').rename(columns={'size':'attended_exams'})
    merged['attended_exams'] = merged['attended_exams'].fillna(0)

    return merged.sort_values(by=['student_id','subject_name'])