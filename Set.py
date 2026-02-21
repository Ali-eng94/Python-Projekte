names1 = {"John", "Michael", "David"}
names2 = {"Ali", "Dennis", "Joe"}

names1.add("Mostafa")
names1.remove("Michael")
names1.update(names2)

for name in names1:
    print(name)                         #output:David Joe Mostafa Dennis Ali John


#list = []
#tuple = ()
#set = {}