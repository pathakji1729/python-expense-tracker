total=0
file=open("expenses.txt","r")

for line in file:
    line=line.strip()
    amount,description=line.split(",")
    total=total+int(amount)

print(total)
print("Day 4 completed")