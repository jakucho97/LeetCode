import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    
    courses = courses.groupby('class', as_index=False).size()
    
    return courses[courses['size']>=5][['class']]