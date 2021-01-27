n=int(input("enter  a number"))
i=1
dict={}
dict[i]=n
while i<=n:
    j=1
    list=[]
    # dict={}
    # dict[i]=n
    while j<=10:
        z=i*j
        list.append(z)
        j=j+1
    dict[i]=list
    i=i+1
print(dict)
    