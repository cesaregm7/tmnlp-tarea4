from typing import List
import pandas as pd
import os

#Funcion para leer los datos de entrenamiento
def read_sample() -> List[str]:
    basePath = os.path.dirname(os.path.abspath(__file__))
    df = pd.read_csv(basePath+'/../../data/raw/results.csv')
    return df.review.values.tolist()