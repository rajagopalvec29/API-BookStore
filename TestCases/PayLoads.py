from Utilities.Configuration import *


def DBAddBookData(query):
    body = {}
    res = getQuery(query)
    body['name']   = res[0]
    body['isbn'] = res[1]
    body['aisle'] = res[2]
    body['author'] = res[3]
    return  body


def Addbook(isbn):
    dbody = {
        'name' : 'Python',
        'isbn' : isbn,
        'aisle' :'562',
        'author' : 'Raja'
    }
    return dbody