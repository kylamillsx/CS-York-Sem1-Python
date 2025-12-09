def rec_sum(numbers):
    if numbers == []:
        return 0
    else:
        return numbers[0] + rec_sum(numbers[1:])
print(rec_sum([1,2,3,4]))
    