for i in range(0,3,1):
    for i in range(0,3,1):
        print("*", end="")
    print()                     #output= ***
                                #        ***
                                #        ***


rows = int(input("Enter number of rows? "))
colums = int(input("Enter number of columns? "))

for i in range(0,rows,1):
    for j in range(0, colums ,1):
        print("*", end="")
    print()                         #output:
                                    #Enter number of rows? 5
                                    #Enter number of columns? 5
                                    #*****
                                    #*****
                                    #*****
                                    #*****
                                    #*****

number = int(input("Enter number a number? "))

for i in range(number):
    for j in range(i+1):
        print("*", end="")
    print()                             #output:
                                        #Enter number a number? 5
                                        #*
                                        #**
                                        #***
                                        #****
                                        #*****