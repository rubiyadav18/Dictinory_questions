num=(input("enter a any number---"))
num=num.split(' ')
dicts={"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"ten":10}
a=''
for i in num:
	a+=str(dicts[i])
print(int(a))