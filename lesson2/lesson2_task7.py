lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
list_length=len(lst)
sumOfElements=0
for i in range(list_length):
    sumOfElements=sumOfElements+lst[i]

print("Sum of all the elements in the list is:", sumOfElements)