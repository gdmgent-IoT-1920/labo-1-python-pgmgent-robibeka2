names = open('namen.txt')

d = dict()

for name in names:
    name = name.strip()
    if name in d:
        d[name] = d[name] + 1
    else:
        d[name] = 1

for key in list(d.keys()):
    print('{}: {}'.format(key, d[key]))

names.close()
