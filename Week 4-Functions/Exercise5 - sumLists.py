
def sum_lists(list_2d):
    total = 0
    output = []
    for r in list_2d:
        for num in r:
            total = num + total
        output.append(total)
        total = 0
    return output
list_2d = [[1,2,3],[2],[1,2,3,4]]
print(sum_lists(list_2d))
