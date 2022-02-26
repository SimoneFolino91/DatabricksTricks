from itertools import chain
from pyspark.sql.types import *
import pyspark.sql.functions as F
from pyspark.sql.window import Window
from functools import reduce
from pyspark.sql import Row, DataFrame

def mapping_column(df: DataFrame, dictionary: dict, column: F.col, newColumnName: str):
  map_spark = F.create_map(list(chain.from_iterable([(F.lit(key), F.lit(value)) for (key, value) in dictionary.items()])))
  return df.withColumn(newColumnName, map_spark.getItem(column))

job_map = {'DE':'Data Engineer', 'DA': 'Data Analyst'}
display(test)
display(mapping_column(test, job_map, F.col('job'), 'Job_Description'))
