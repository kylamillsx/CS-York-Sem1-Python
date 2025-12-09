def display_dico(dico):
    for key, val in dico.items():
        print(key, '-->',val)
dico = {'un':1,'duex':2,'trois':3,}
print(dico)
print(display_dico(dico))