from pyspark.sql import Row, DataFrame
import pyspark.sql.functions as F

def renamedDataframe(df: DataFrame, **kwargs):
  return df.select(*[F.col(i).alias(kwargs.get(i, i)) for i in df.columns])

svin = spark.createDataFrame([Row(Id = '0001', Name= 'Simon', Ruolo = 'A', Valore = 100000, Esperienza = 10)])
display(svin)
## First Approach: Using Kwargs
display(renamedDataframe(svin, Id= 'GiocatoreId', Esperienza = 'Anzianita', Name= 'NamePlayer'))
## Second Approach: Using Dictionary
dizionario = {'Id':'IdPlayer', 'Esperienza':'Anzianita', 'Name':'PlayerName'}
display(renamedDataframe(svin, **dizionario))
