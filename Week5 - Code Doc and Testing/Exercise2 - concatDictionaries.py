def concat_dico(dic1,dic2):
    joined = {**dic1,**dic2} #used to merge the two dictionaries
    print(joined) 
    merged = []
    for y in (dic1,dic2):
        for key, val in y.items():
            merged[key].append(val)
    print(merged)
dic1 = {'one':1,'two':2,'three':3,'five':5}
dic2 = {'four':4,'five':'101'}
print(concat_dico(dic1,dic2))
