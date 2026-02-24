def sum(*args):
    sum = 0
    for i in args:
        sum = sum + i
    return sum

print(sum(1,2,4,5,8,56,45564,5564,65))         #output: 51269