import os

import argparse

import loaddata
import utils

import test_redis
import test_mongodb
import test_cassandra

TIMER = utils.timer()

def test_db(db):
    print(db.__name__)
    d = db.init_db()

    result = []

    TIMER.tic()
    print(db.search_si(d, b'Mel_Thompson'))
    TIMER.toc(result)

    TIMER.tic()
    print(len(db.search_oi(d, b'England')))
    TIMER.toc(result)

    TIMER.tic()
    print(len(db.search_p1p2(d, b'graduatedFrom', b'isLeaderOf')))
    TIMER.toc(result)

    TIMER.tic()
    print(db.search_maxo(d, b'England'))
    TIMER.toc(result)

    print()
    print(result)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--db', type=str, required=True)
    parser.add_argument('--gen', type=bool, default=False)
    parser.add_argument('--index', type=bool, default=False)

    args = parser.parse_args()

    db = {
        'redis': test_redis,
        'mongodb': test_mongodb,
        'cassandra': test_cassandra
    }[args.db]

    d = db.init_db()
    if args.gen:
        db.add_to_db(d, loaddata.loaddata(), args.index)
    test_db(db)

if __name__ == '__main__':
    main()
