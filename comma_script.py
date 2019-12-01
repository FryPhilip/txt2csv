f = open('ext_index.csv', 'r')


line = f.readline()

for line in f:
    for str in line:
        print(str)
