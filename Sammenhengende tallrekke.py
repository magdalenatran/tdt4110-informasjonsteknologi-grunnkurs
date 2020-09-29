import random

def randList(size, lower_bound, upper_bound):
    random_numbers = []
    for i in range(size):
        random_numbers.append(random.randint(lower_bound, upper_bound))
    return random_numbers

def compareLists(list1, list2):
    list_both = []
    for element in list1:
        if element in list2:
            list_both.append(element)
            for element in list1:
                list1.remove(element) #Hvordan fjerne uten å bruke innebygde funksjoner?
    return list_both

#multiCompList(lists):
    list_multi = []
    #for i in range(n):
        #for element in i:

def longestEven(list):
    count = 0
    for i in range(len(list)-1):
        if list[i]%2 == 0:
            count = 1
            if list[i+1]%2 == 0:
                count += 1
            else:
                #lagre count
                count = 0
        position = list.find(lagretcount)
    return position, count


random_list = randList(5, 1, 10)
print(random_list)

list1 = [1, 2, 3, 2, 2, 5]
list2 = [2, 3, 6, 2, 3, 5]
list_both = compareLists(list1, list2)
print(list_both)

#list_multi = [[1,2,3],[4,5,6],[7,8,9]]
#print(list_multi[2])

list3 = [1, 2, 2, 2, 3, 3, 4, 4, 4, 4]
count = longestEven(list3)
print(count)