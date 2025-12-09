
number = int(input("Type in a number"))
def sum_digits(number):
    string = str(number)
    sum = 0
    for i in range(len(string)):
        value = int(string[i])
        sum = sum + value
    return sum
print(sum_digits(number))