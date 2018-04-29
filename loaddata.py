
import sys

def loaddata():
    SIZE = 124307

    with open('data/yagoThree.txt', 'rb') as datafile:
        for i, line in enumerate(datafile):
            line = line[:-1] if line.endswith(b'\n') else line
            line = line[:-1] if line.endswith(b'\r') else line
            line = line.split(b' ')
            if i % 100000 == 0:
                print('processed: {:05.02f}%'.format(i / SIZE), file=sys.stderr)
            yield line

