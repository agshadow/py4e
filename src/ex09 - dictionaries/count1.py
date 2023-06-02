#fname = input('Enter the file name: ')
try:
    fhand = open("romeo.txt")
except:
    print('File cannot be opened:')
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

print(counts)

# Code: http://www.py4e.com/code3/count1.py