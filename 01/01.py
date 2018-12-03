import array

list = array.array('i')
with open("data.txt") as f:
    for line in f:
        list.append(int(line))
print(sum(list))
