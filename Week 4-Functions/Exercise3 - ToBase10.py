def to_base10(binary):
    sum = 0
    reversed = str(binary) [::-1] #reverses the string
    for i in range (len(reversed)):
        if str(reversed[i]) == "1":
            sum = sum + (1*pow(2,i))
        else:
            sum = sum + (0*pow(2,i))
    return sum
binary = input("Whats your binary")
print(to_base10(binary))