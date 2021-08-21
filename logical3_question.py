"in this program i put one and two and any opraters so output will came 3"

num=(input("enter a any number---"))
l=["zero","one","two","three","four","five","six","seven","eight","nine","ten"]
num= num.split(' ')
a=l.index(num[0])
b=l.index(num[2])
if num[1]=='+':
	print(a+b)
elif num[1]=='-':
	print(a-b)
elif num[1]=='*':
	print(a*b)
elif num[1]=='/':
	print(a/b)
    "how put on input so here see"
    " first which number u want add and subract and multiply what ever"
    "so like one and space what ever oprates after that which u want u can give number"
    "exmaple----one + two "