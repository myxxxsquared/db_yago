
import redis
import collections

DB_SERVICE_NAME = 'redis-server.service'

def getkey(x):
    return x.split(b' ')[0]

def geto(x):
    return x.split(b' ')[1]

SLISTNAME = b' '

def add_to_db(r, data, _):
    r.flushdb()
    pipeline = r.pipeline(transaction=False)
    count = 0
    for s, p, o in data:
        k = s + b' ' + p
        pipeline.sadd(SLISTNAME, s)
        pipeline.sadd(k, o)
        pipeline.sadd(o, k)
        count += 1
        if count >= 10000:
            pipeline.execute()
            pipeline = r.pipeline(transaction=False)
            count = 0
    pipeline.execute()

def search_si(r, si):
    keys = r.keys(si + b' *')
    return {geto(k): list(r.smembers(k)) for k in keys}

def search_oi(r, oi):
    return list(r.smembers(oi))

def search_p1p2(r, p1, p2):
    keys1 = set(map(getkey, r.keys(b'* ' + p1)))
    keys2 = set(map(getkey, r.keys(b'* ' + p2)))
    return keys1.intersection(keys2)

def search_maxo(r, oi):
    counter = collections.Counter()
    counter.update(map(getkey, r.smembers(oi)))
    return counter.most_common(1)[0]

def init_db():
    return redis.Redis()
