f = open('ext_index.csv', 'r')
fr = open('out.csv', 'w')

for str in f.read():
    counter = 0
    for chrr in str:
        if chrr.isspace():
            fr.write(",")
            counter += 1
        else:
            fr.write(chrr)
        if counter >= 13:
            print(counter)
            fr.write("\n")
        
f.close()
fr.close()
