f = open('ext_index.csv', 'r')
fr = open('out.csv', 'w')

counter = 0

for str in f.read():
    if str.isspace():
        fr.write(",")
        counter += 1
    else:
        fr.write(str)
    if counter >= 13:
        print(counter)
        fr.write("\n")
        counter = 0

        
f.close()
fr.close()
