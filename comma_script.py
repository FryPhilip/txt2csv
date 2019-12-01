f = open('test.txt', 'r')
fr = open('out.txt', 'w')

line = f.readline()

for str in line:
    for chrr in str:
        if chrr.isspace():
            fr.write(",")
            print(2)
        else:
            fr.write(chrr)
            print(1)
        
f.close()
fr.close()
