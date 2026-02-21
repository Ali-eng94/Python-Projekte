list  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 5, 4]
for i in range(len(list)//2):
    temp = list[i]
    list[i] = list[len(list) - 1 - i]
    list[len(list) - 1 - i] = temp

print(list)                                 #The code is there to reverse a list — that is,
                                            # to mirror the order of the elements.