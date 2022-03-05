import pandas as pd
from matplotlib_venn import venn2
import matplotlib.pyplot as plt
import seaborn as sns
from .shaper import str_by_age
from typing import Tuple

def plt_count(
  col: str, 
  data: pd.DataFrame, 
  title: str = "", 
  xlab: str = "", 
  x_rotate: bool = False, 
  order: bool = True, 
  ann: bool = True,
  figsize: Tuple[int, int] = (6, 4)
  ):
  """Create Count plot from DataFrame.

  Args:
      col (str): col name
      data (pd.DataFrame): dataFrame
      title (str, optional): title Defaults to "".
      xlab (str, optional): xlab Defaults to "".
      x_rotate (bool, optional): xlab Rotate Defaults to False.
      order (bool, optional): order Defaults to True.
      ann (bool, optional): annotate Defaults to True.
      figsize (Tuple[int, int], optional): figsize Defaults to (10, 6).
  """
  _order = None
  fig, ax = plt.subplots(figsize=figsize)

  if order:
    _order = data[col].value_counts().index
  
  sns.countplot(x=col ,data=data, order = _order, ax=ax)
  plt.title(title)
  plt.xlabel(xlab)
  if ann:
    for p in ax.patches:
      ax.annotate('{:.2f}%'.format(100 * p.get_height() / len(data[col])), (p.get_x()+0.3, p.get_height()+1.5))
  
  if x_rotate:
    ax.set_xticklabels(ax.get_xticklabels(),rotation = 30)
  
  
  plt.show()


def plt_venn(
  _df_1: pd.Series,  
  _df_2: pd.Series, 
  ax: any,
  left_filter: any = 1,
  right_filter: any = 1,
  title: str = "",
  left_lab: str = "A",
  right_lab: str = "B",
  ):
  """Create Venn Diagrams from 2 Series.

  Args:
      _df_1 (pd.Series): Series 1
      _df_2 (pd.Series): Series 2
      left_filter (any, optional): count value. Defaults to 1.
      right_filter (any, optional): count value. Defaults to 1.
      title (str, optional): title. Defaults to ''".
      left_lab (str, optional): label1. Defaults to A.
      right_lab (str, optional): label2. Defaults to B.
  """
  venn2(
    subsets=[set(_df_1[_df_1 == left_filter].index), set(_df_2[_df_2 == right_filter].index)],
    set_labels=(left_lab, right_lab),
    ax=ax
  )
  plt.title(title)
  plt.show()


def plt_by_age(
  df: pd.DataFrame, 
  col: str, 
  min_age: int = 0, 
  max_age: int = 120, 
  by: int = 5, 
  fill: bool = False, 
  title: str = "", 
  xlab: str = "", 
  order: bool = False,
  figsize: Tuple[int, int] = (6, 4)
  ):
  """Create Count plot from Stratified by Age

  Args:
      df (pd.DataFrame): _description_
      col (str): _description_
      min_age (int, optional): _description_. Defaults to 0.
      max_age (int, optional): _description_. Defaults to 120.
      by (int, optional): _description_. Defaults to 5.
      fill (bool, optional): _description_. Defaults to False.
      title (str, optional): _description_. Defaults to "".
      xlab (str, optional): _description_. Defaults to "".
      order (bool, optional): _description_. Defaults to False.
      figsize (Tuple[int, int], optional): figsize Defaults to (10, 6).
  """
  _df = str_by_age(df, col, min_age, max_age, by, fill)
  plt_count(col, data=_df, title=title, xlab=xlab, x_rotate=True, order=order, figsize=figsize)