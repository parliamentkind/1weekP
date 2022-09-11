#1
p = int(input('Enter a price for 1kg of sweets: '))
i = 1
while i<10:
    i+=1
    p+=1
    print(p)

#2
x = 0
total = 0
list = []

for i in range(0, 100):
    A = int(input("Enter the number: "))
    if A == 0:
        break
    list.append(A)

while (x < len(list)):
    total += list[x]
    x += 1
print("Sum of all elements: ", total)
print("Number of elements in sequence: ", len(list))

