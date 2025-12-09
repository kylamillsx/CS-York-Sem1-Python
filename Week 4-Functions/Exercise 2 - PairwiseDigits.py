def pairwise_digits(number_a,number_b):
    result = []
    length_num_a = str(number_a)
    length_num_b = str(number_b)
    if len(length_num_a) > len(length_num_b):
        for i in range (len(length_num_b)):
            if length_num_a[i] == length_num_b[i]:
                result.append(1)
            else:
                result.append(0)
        while len(result)<len(length_num_a):
            result.append(0)
    else:
        for i in range (len(length_num_a)):
            if length_num_b[i] == length_num_a[i]:
                result.append(1)
            else:
                result.append(0)
        while len(result)<len(length_num_b):
            result.append(0)
    s = ''.join(str(i) for i in result) #converts int in list to str then joins list to string
    return s

number_a = int(input("Enter num a"))
number_b = int(input("Enter number b"))
print(pairwise_digits(number_a,number_b))