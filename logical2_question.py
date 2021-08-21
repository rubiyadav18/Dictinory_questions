"in this question i want same values add and which keys of same values so that values add and keys "
a={"a":2,"b":3,"c":2}
c=[]
for i in a:
    if a[i] not in c:
        c.append(a[i])
d={}
for i in c:
    string=' '
    count=0
    for j in a:
        if i==a[j]:
            string+=j
            count+=1
    d[string]=i*count
print(d)
"i want output means a and c asame values so "
"output---ac 4 and b 3 "
