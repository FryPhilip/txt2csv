f_read = open('ext_index.csv', 'r')
##f_write = open('ext_index.csv', 'w')

line = f_read.readline()

for str in f_read:
    print(str)
