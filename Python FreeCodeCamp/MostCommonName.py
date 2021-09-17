
d = dict()
d = {}

while (True):
    name = input("insert a name: ")
    if (name in d):
         d[name] = d.get(name,0) + 1
    else:
         d[name] = d.get(name,1)
    ctn = input ("Wanna add more names? (y/n)")
    if ctn=='n':
        break

print (d)