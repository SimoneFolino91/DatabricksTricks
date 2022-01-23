from pymongo import MongoClient, DESCENDING

cars = [ {'name': 'Audi', 'price': 52642,'nation':'Germany'},
    {'name': 'Mercedes', 'price': 57127,'nation':'Germany'},
    {'name': 'Skoda', 'price': 9000,'nation':'Sweden'},
    {'name': 'Volvo', 'price': 29000,'nation':'Germany'},
    {'name': 'Bentley', 'price': 350000,'nation':'UK'},
    {'name': 'Citroen', 'price': 21000,'nation':'France'},
    {'name': 'Hummer', 'price': 41400,'nation':'UK'},
    {'name': 'Volkswagen', 'price': 21600,'nation':'Germany'} ]

client = MongoClient('mongodb://localhost:27017/')
with client:
    db = client.testdb
    db.cars.insert_many(cars)
    agr2 = [ {'$group': {'_id': '$nation', 'allPrice': { '$sum': '$price' },'gruppi':{'$push':'$name'} } } ]
    ## Pass a list of dict
    ## in the _id you need to insert the keys from which you want to aggregate
    ## in the other name_of_new_variable : {operation: key_of_the_operation}
    val2 = list(db.cars2.aggregate(agr2))    
    
def remove_keys(diz: dict,*args):
    return dict((x,y) for (x,y) in diz.items() if x not in args)
aggregated_data = dict((x['_id'],remove_keys(x, '_id')) for x in val2)
