def flatten(mlist):
    flattenlist = []
    for num in mlist:
        if isinstance(num, list):
            flattenlist.extend(flatten(num))
        else:
            flattenlist.append(num)
    return flattenlist
print(flatten([1,[2,3],4]))