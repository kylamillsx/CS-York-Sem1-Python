def map_list(keys,values):
    dict = {}
    for i in range(len(keys)):
        dict.update({keys[i]:values[i]})
    print(dict)
keys = ['un','two']
values = [1,2]
print(map_list(keys,values))