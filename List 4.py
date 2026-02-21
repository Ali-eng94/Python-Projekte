list = [5,47,8,6,55,5,2,6,456,454,65756,5]


for i in range(len(list)-1):
    for j in range(len(list)-1-i):
        if list[j] > list[j+1]:
            temp = list[j]
            list[j] = list[j+1]
            list[j+1] = temp

print(list)                            #sort the array from smallest number to largest number