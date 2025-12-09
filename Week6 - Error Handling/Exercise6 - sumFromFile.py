def sum_numbers(a_string):
    sum = 0
    value = ""
    for i, char in enumerate(a_string):
        if i<len(a_string)-1:
            if char.isdigit():
                if a_string[i+1].isdigit():
                    value = value+char
                if a_string[i+1]==" " :
                    value = value+str(char)
                    sum = sum+int(value)
                    value = ""
        if a_string[-1] == char:
                value = value + str(char)
                sum = sum +int(value)
    return sum
fileUsed = open('fileUsed.txt','w')
fileUsed.write("1 30 4 5")
fileUsed.close()
def sum_from_file(fileUsed):
    fileUsed = open('fileUsed.txt','r')
    a_string = str(fileUsed.read())
    fileUsed.close()
    return a_string
a_string = (sum_from_file(fileUsed))
print(sum_numbers(a_string))