
import collections
import sys

from pymongo import MongoClient, IndexModel, ASCENDING

DB_SERVICE_NAME = 'mongodb.service'

def init_db():
    client = MongoClient()
    db = client.test
    yago = db.yago
    return yago

def add_to_db(yago, data, indexes):
    lst = []
    yago.drop_indexes()
    yago.delete_many({})
    for s, v, o in data:
        lst.append({'s': s, 'o': o, 'v': v})
        if(len(lst) >= 10000):
            yago.insert_many(lst)
            lst.clear()

    if indexes:
        index1 = IndexModel([("s", ASCENDING)], name='s')
        index2 = IndexModel([("v", ASCENDING)], name='v')
        index3 = IndexModel([("o", ASCENDING)], name='o')
        yago.create_indexes([index1, index2, index3])

def search_si(yago, si):
    return [(d['o'], d['v']) for d in yago.find({'s': si})]

def search_oi(yago, oi):
    return [(d['s'], d['v']) for d in yago.find({'o': oi})]

def search_p1p2(yago, p1, p2):
    s1 = set((d['s'] for d in yago.find({'v': p1})))
    s2 = set((d['s'] for d in yago.find({'v': p2})))
    return s1.intersection(s2)

def search_maxo(yago, oi):
    counter = collections.Counter()
    counter.update((c['s'] for c in yago.find({'o': oi})))
    return counter.most_common(1)[0]
