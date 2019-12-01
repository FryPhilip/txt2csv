f_read = open('ext_index.csv', 'r')
##f_write = open('ext_index.csv', 'w')

line = f_read.readline()

for str in f_read:
    for chrr in str:
        if chrr.isspace():
            print("is space")
        else:
            print(chrr)
