def sum_digits(number):
    if number == 0:
        return 0
    else:
        return number%10 + sum_digits(number//10)
    #number % 10 will return the last digit
    #number //10 will remove the last digit from whole number
    #repeat this till its added all the numbers
print(sum_digits(1234))