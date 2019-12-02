#open streams
f = open('ext_index.csv', 'r') 
fr = open('out.csv', 'w')   

##Number of colums on source file.
print("Enter number of colums:")
input(colum_num) 

counter = 0

## Interates through the input file.
for str in f.read():
    if str.isspace(): 
        fr.write(",") ##writes comma to output 
        counter += 1
    else:
        fr.write(str) ##writes current character to output
    if counter >= colum_num: ##checks for line break through number of colums
        fr.write("\n")
        counter = 0

fr.write(",") ##comma at the end of file

#close streams      
f.close()
fr.close()
