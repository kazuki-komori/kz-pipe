import pandas as pd
from matplotlib_venn import venn2
import matplotlib.pyplot as plt
import seaborn as sns

def plt_count(col: str, data: pd.DataFrame, title: str = "", xlab: str = ""):
  """Create Count plot from DataFrame.

  Args:
      col (str): col name
      data (pd.DataFrame): dataFrame
      title (str, optional): title Defaults to "".
      xlab (str, optional): xlab Defaults to "".
  """
  ax = sns.countplot(x=col ,data=data, order = data[col].value_counts().index)
  plt.title(title)
  plt.xlabel(xlab)
  for p in ax.patches:
      ax.annotate('{:.2f}%'.format(100 * p.get_height() / len(data[col])), (p.get_x()+0.3, p.get_height()+1.5))
  plt.show()


def plt_venn(
  _df_1: pd.Series,  
  _df_2: pd.Series, 
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
    set_labels=(left_lab, right_lab)
  )
  plt.title(title)
