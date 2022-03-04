import imp

from numpy import number
import pandas as pd
from timer import Timer
import seaborn as sns
from matplotlib_venn import venn2
import pandas as pd

def plt_ven(_df_1: pd.Series,  _df_2: pd.Series, left_filter: any = 1, right_filter: any = 1):
  """2 つの Series からベン図を

  Args:
      _df_1 (pd.Series): Series 1
      _df_2 (pd.Series): Series 2
      left_filter (any, optional): 図示する値. Defaults to 1.
      right_filter (any, optional): 図示する値. Defaults to 1.
  """
  venn2(subsets=[set(_df_1[_df_1 == left_filter].index), set(_df_2[_df_2 == right_filter].index)])
