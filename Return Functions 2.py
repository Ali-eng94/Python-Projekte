def sum(num1,num2):
    result = 0
    for i in range(num1,num2 + 1):
        result = result + i
    return result

print(sum(1,100))             #output 5050
print(sum(5,10))              #output 45



x = int(input("input a number : "))
y = int(input("input another number : "))


print(sum(x,y))                                             #output:input a number : 1
                                                                   #input another number : 10
                                                                   #55

def factorial(number):
    result = 1
    for i in range(1,number + 1):
        result = result * i
    return result

print(factorial(5))             #output is 120



def power(basenum,exponent):
    result = 1
    for i in range(exponent ):
        result = result * basenum
    return result

print(power(5,2))        #output is 25