import pyspark.sql.functions as F
from pyspark.sql.types import *
from pyspark.sql.window import Window
from itertools import chain
from pyspark.sql import Row, DataFrame

def melt(dataframe: DataFrame, id_columns: list, value_vars: list = None):
  if value_vars == None:
    value_vars = [i for i in dataframe.columns if i not in id_columns]
  mappa_other = F.create_map(list(chain.from_iterable([(F.lit(i), F.col(i)) for i in value_vars])))
  return dataframe.select(*id_columns, F.explode_outer(mappa_other).alias('variable','value'))

display(df)
display(melt(df,id_columns=['id','Name'], value_vars=['height','nationality']))
