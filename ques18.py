total=0
with open("expenses.txt","r") as file:
    for i in file:
        i=int(i)
        total=total+i
print(total)
