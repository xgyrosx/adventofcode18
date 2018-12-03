import array

# list = array.array('i')
# sumlist = array.array('i')
duplicates = array.array('i')
freq_set = set([0])
freq = 0


with open("data.txt") as f:
    while(len(duplicates) == 0):
        for line in f:
            freq = freq + int(line)
            if(freq in freq_set):
                duplicates.append(freq)
            else:
                freq_set.add(freq)
        f.seek(0)
print(duplicates)