import pyspark.sql.functions as F
from pyspark.sql import Row

frase = """
Sopra la panca
la capra campa
sotto la panca
la capra crepa
"""
df = spark.createDataFrame([Row(phrase = frase)])
display(df.select(F.explode(F.split(F.regexp_replace('phrase', '\n', ' '),' ')).alias('words')) # First Create An Array Column Splitting the phrase col and the explode it
        .withColumn('words', F.lower('words')) # make all the word in lower case
        .filter(F.trim(F.col('words')) != '')# filter out empty words
        .groupby('words') # Group by word
         .count().orderBy(F.col('count'), ascending = False) # then count it
       )


#### Using the 
