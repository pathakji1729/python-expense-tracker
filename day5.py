category_total={}

file=open("expenses.txt")
for line in file:
    line=line.strip()
    amount,description=line.split(",")
    amount=int(amount)
    category=description

    if category in category_total:
       category_total[category]=category_total[category]+amount
    else:
        category_total[category]=amount
        
file.close()
for category in category_total:
     print(category,"=",category_total[category])
       