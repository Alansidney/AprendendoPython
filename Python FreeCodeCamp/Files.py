handle = open("file.txt",'r')

txt = handle.read()
txt.strip()
print (txt)
print (len(txt))