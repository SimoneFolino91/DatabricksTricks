from pyspark.sql.types import *
import pyspark.sql.functions as F
from pyspark.sql.window import Window
from functools import reduce
from pyspark.sql import Row, DataFrame


def transformInDataFrame(lista :list):
  return spark.createDataFrame([Row(**i) for i in lista])

df_1 = transformInDataFrame([{'nome':'Simone', 'surname': 'Folino'}])
df_2 = transformInDataFrame([{'nome':'Mario'}])
df_3 = transformInDataFrame([{'nome':'Gino'}])


def concat(*dataframes: DataFrame):
  assert len(dataframes) > 1, 'insert at least two element'
  return reduce(lambda x,y: x.unionByName(y, allowMissingColumns= True), dataframes[1:], dataframes[0])
  
display(concat(df_1, df_2, df_3))
