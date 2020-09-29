def is_six_at_edge(list):
    if list[0] == 6 or list[len(list)-1] == 6:
        return True
    else:
        return False

def average(list):
    sum = 0
    for number in list:
        sum += number
    average = sum/len(list)
    return average

def median(list):
    list = sorted(list)
    print(list)
    return list[((len(list)-1)//2)]

list = [6, 1, 3, 6, 5, 6, 8]

six = is_six_at_edge(list)
print(six)

average = average(list)
print(average)

median = median(list)
print(median)





