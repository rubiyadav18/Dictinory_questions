"in this program i am checking leepyear or not "
"and i put 2017 so output will came 13.09.2017"

num=int(input("enter  any   number==========+"))
if num<1918:
    if num%4==0:
        print("12.09."+str(num))
    else:
        print("13.09."+str(num))
elif num>1918:
    if num%400==0 or (num%4==0 and num%100!=0):
        print("12.09."+str(num))
    else:
        print("13.09."+str(num))
else:
    print("26.09.1918")