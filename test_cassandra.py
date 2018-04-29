
import collections

from cassandra.cluster import Cluster, BatchStatement, ConsistencyLevel  # pylint: disable=E0611

DB_SERVICE_NAME = 'cassandra.service'

def add_to_db(session, data, _):
    session.execute('drop table yago')
    session.execute('create table if not exists yago (i int primary key, s varchar, v varchar, o varchar)')
    session.execute("create index if not exists sindex on yago (s)")
    session.execute("create index if not exists vindex on yago (v)")
    session.execute("create index if not exists oindex on yago (o)")

    prepared = session.prepare('insert into yago (i, s, v, o) values (?, ?, ?, ?)')
    batch = BatchStatement(consistency_level=ConsistencyLevel.ANY)
    count = 0
    i = 0
    for s, v, o in data:
        batch.add(prepared, (i, s.decode('latin1'), v.decode('latin1'), o.decode('latin1')))
        count += 1
        i += 1
        if count >= 10:
            session.execute_async(batch)
            batch = BatchStatement(consistency_level=ConsistencyLevel.ANY)
            count = 0
    session.execute(batch)

def search_si(session, si):
    result = session.execute('select v, o from yago where s = %s allow filtering', (si.decode('latin1'),))
    return [tuple(x) for x in result]

def search_oi(session, oi):
    result = session.execute('select s, v from yago where o = %s allow filtering', (oi.decode('latin1'),))
    return [tuple(x) for x in result]

def search_p1p2(session, p1, p2):
    result1 = session.execute('select s from yago where v = %s allow filtering', (p1.decode('latin1'),))
    result1 = set((x[0] for x in result1))
    result2 = session.execute('select s from yago where v = %s allow filtering', (p2.decode('latin1'),))
    result2 = set((x[0] for x in result2))
    print(p1)
    print(len(result1), len(result2))
    return result1.intersection(result2)

def search_maxo(session, oi):
    counter = collections.Counter()
    counter.update((x[0] for x in session.execute('select s from yago where o = %s allow filtering', (oi.decode('latin1'),))))
    return counter.most_common(1)[0]

def init_db():
    cluster = Cluster(['127.0.0.1'])
    session = cluster.connect()
    session.execute("create keyspace if not exists test with replication={'class':'SimpleStrategy', 'replication_factor': 1}")
    session.execute('use test')
    session.execute('create table if not exists yago (i int primary key, s varchar, v varchar, o varchar)')
    session.execute("create index if not exists sindex on yago (s)")
    session.execute("create index if not exists vindex on yago (v)")
    session.execute("create index if not exists oindex on yago (o)")

    return session
