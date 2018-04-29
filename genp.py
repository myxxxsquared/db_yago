
import loaddata

if __name__ == '__main__':
    props = set()

    data = loaddata.loaddata()
    for line in data:
        if line[1] not in props:
            props.add(line[1])

    props = sorted(props)

    with open('data/p', 'wb') as outputfile:
        for p in props:
            outputfile.write(p)
            outputfile.write(b'\n')
