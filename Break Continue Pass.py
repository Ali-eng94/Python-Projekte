# Break
# Continue
# Pass

while True:
    name = input("Please enter your name: ")
    if name != "":
        break                           #output:
                                        #Please enter your name:
                                        #Please enter your name:
                                        #Please enter your name:

number = "1234-5678-2545"
for i in range(0,10,1):
    if i == 2 :
        continue
    print(i,end="")                              #output: 013456789


for i in range(1,10,1):
    if i == 5 :
        pass
    else:
        print(i,end="")                         #output: 12346789
