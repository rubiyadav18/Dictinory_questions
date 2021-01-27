list=['M','I','S','S','I','S','S','I','P','P','I']
i=0
dict= {}
while i<len(list):
    j=0
    count=0
    dict1={}
    while j<len(list):
        if list[i]==list[j]:
            count=count+1
        j=j+1
        # e1.append(list[i])
        # dict1.update(count)
        # if e not in e1:
    dict[list[i]] = count
    i=i+1
print(dict)