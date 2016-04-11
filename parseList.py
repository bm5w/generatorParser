file = 'list.txt'
types = {}


def parse(line):
    _type = line[10:]
    if _type in types:
        types[_type] += 1
    else:
        types[_type] = 1

with open(file, 'r') as file:
    for line in file:
        parse(line.rstrip())

for typ, count in types.iteritems():
    print '{}: {}'.format(typ, count)