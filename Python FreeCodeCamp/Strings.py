str1 = "AlanDisney da Silva"
print ('Lenght str1 = ', len(str1))

#iterate in Strings
for letter in str1:
    print(letter)

#slicing
print(str1[0:10])

#String functions
print (str1.upper())
print (str1.find('Disney'))
str2 = str1.replace('Disney','sidney')
print (str2)
nomes = str2.strip(' ')
print (nomes)