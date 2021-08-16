a=[{'item':'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':750}]
newlist={}
for i in a:
    item=i['item']
    if item not in newlist:
        newlist[item]=i['amount']
    else:
        add= newlist[item]
        add+=i['amount']
        newlist[item]=add

print('Counter(',newlist,')')