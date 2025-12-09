month = {'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
for key, val in month.items():
    print(key, ":",val)
periodicTable = {'H':'Hydrogren','He':'Helium','Li':'Lithium'}
roman ={} #creating dictionary
roman['100,000'] = 'T'
roman['1000']= 'M'#adding keys and values to it
roman['500']='D'
roman['100']='K'
roman['50']='L'
roman['10']='X'
roman['5']='V'
roman['1']='I'
print(roman)
roman['100'] = 'C' #changes value 
del roman['100,000'] #deletes value
print(roman)