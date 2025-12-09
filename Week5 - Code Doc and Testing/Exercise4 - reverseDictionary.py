def reverse_dictionary(dico):
    newDicVals = []
    newDicKeys = []
    for key, val in dico.items():
        newDicVals.append(key)
        newDicKeys.append(val)
    reverse = {}
    for i in range(len(dico)):
        reverse.update({newDicKeys[i]:newDicVals[i]})
    return reverse
dico = {"one":1,"two":2}
print(reverse_dictionary(dico))