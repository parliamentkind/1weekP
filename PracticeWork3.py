a1 = int(input('Enter 1st number: '))
a2 = int(input('Enter 2nd number: '))
a3 = int(input('Enter 3th number: '))
if a1>a2:
    if a1>a3:
        z=a1
else:
    if a2>a3:
        z=a2
    else:
        z=a3
if a1<a2:
    if a1<a3:
        q=a1
else:
    if a2<a3:
        q=a2
    else:
        q=a3
print('Biggest number is: ' + str(z))
print('Smallest number is: ' + str(q))


