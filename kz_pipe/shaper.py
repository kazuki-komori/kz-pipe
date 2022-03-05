import numpy as np
import pandas as pd

def str_by_age(df: pd.DataFrame, col: str, min_age: int = 0, max_age: int = 120, by: int = 5, fill: bool = False) -> pd.DataFrame:
  """Stratified by Age

  Args:
      df (pd.DataFrame): DataFrame
      col (str): column
      min_age (int, optional): lowest age. Defaults to 0.
      max_age (int, optional): highest age. Defaults to 120.
      by (int, optional): Stratified by. Defaults to 5.
      fill (bool, optional): fill na. Defaults to average.
  
  Returns:
      pd.DataFrame
  """
  if fill:
    df[col] = df[col].fillna(df[col].mean())
  labels = ["{0}-{1}".format(i, i + 5) for i in range(min_age, max_age-5, by)]
  _df = pd.DataFrame(pd.cut(df[col], bins=np.arange(min_age, max_age, by), labels=labels))
  return _df