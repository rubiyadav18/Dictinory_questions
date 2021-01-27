dict={2,6,2,6,8,9,10}
i=0
dict2= {}
a=list(dict)
print(a)
while i<len(a):
    j=0
    while j<i:
        if a[i]>a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
        j=j+1
    i=i+1
# dict2=[dict[j]]=dict
print("disending",a)
i=0
while i<len(a):
    j=0
    while j<i:
        if a[i]<a[j]:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
        j=j+1
    i=i+1
# dict2=a[j]
print("acending",a)
