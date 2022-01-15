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


#### Using the Array Function
def filter_out_empty_string(column):
  return F.filter(column, lambda x: x != '') # Remember the element value value of an array is a column object!!!!

def lower_case_for_element_in_array(column):
  return F.transform(column, lambda x: F.lower(x)) # Remember the element value of an array is a column object!!!!

display(df.select(F.explode(lower_case_for_element_in_array(filter_out_empty_string(F.split(F.regexp_replace('phrase', '\n', ' '),' ')))).alias('words'))
        .groupby('words')
         .count().orderBy(F.col('count'), ascending = False)
       )
"""
Comments: 
1) Replace the \n with " " with F.regex_replace
2) Split the words into an array 
3) Filter out using the function filter_out_empty_string (No UDF) the " " char from the array
4) Map the words of the array into a 
"""
