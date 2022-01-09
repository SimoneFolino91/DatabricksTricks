from itertools import groupby, chain
from functools import reduce

datalist = [{'name':'simone', 'surname':'Folino', 'language':'python', 'level':7}, {'name':'simone', 'surname':'Folino','language':'java', 'level':5},{'name':'simone','surname':'Folino', 'language':'javascript', 'level':6},{'name':'simone','surname':'Folino', 'language':'groovy', 'level':8}, {'name':'mario', 'surname':'Rossi','language':'python', 'level':5},{'name':'mario', 'surname':'Rossi','language':'java', 'level':9}]

# First Approach: using groupby
def sorting_list(lista,asc = True, *cols_to_sort): # Remember to sort the data upon keys
  return sorted(lista, key = lambda x: [x[i] for i in cols_to_sort], reverse=not asc)

def grouping_data(lista,keys, value,asc= True, operation = list):
  return dict((tuple(z), operation([i[value] for i in  list(y)])) for (z,y) in groupby(sorting_list(datalist, asc, *keys), key= lambda x: [x[m] for m in keys]))


grouping_data(datalist, ['name', 'surname'], 'language')

## Second Approach: using reduce
def grouping_data_reduce(inizio, fine, value, *keys):
  inizio[tuple([fine[i] for i in keys])] = inizio.get(tuple([fine[i] for i in keys]), [])
  inizio[tuple([fine[i] for i in keys])].append(fine[value])
  return inizio

dict((key, list(value)) for (key, value) in reduce(lambda x,y: grouping_data_reduce(x, y, 'language', 'name', 'surname'), datalist, {}).items() )

def grouping_data2(lista, value, keys, operation = list):
  #return reduce(lambda x,y: grouping_data_reduce(x, y, value, *keys), lista, {})
  return dict((key, operation(value)) for (key, value) in reduce(lambda x,y: grouping_data_reduce(x, y, value, *keys), lista, {}).items() )


grouping_data2(datalist, 'language', ['name', 'surname'], len)
