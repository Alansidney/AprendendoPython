d = dict()

file = open('file.txt', 'r')

txt = file.read()
words = txt.split()

for word in words:
    d[word] = d.get(word,0)+1

bVal = None
bKey = None
for key,val in d.items():
    if bVal is None or val > bVal:
        bKey = key
        bVal = val

print ((bVal,bKey))
