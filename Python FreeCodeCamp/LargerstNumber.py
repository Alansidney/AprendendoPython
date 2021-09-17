array = [10,-45,43,78,52,75,-21,7,24]
ln= array[0]
for i in array:
    if ln < i:
        ln = i

print ('Largerst Number is:', ln)