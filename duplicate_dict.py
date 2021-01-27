student_data={'a':'raam','b':'raaj','c':'raani','d':'class','g':'raam','h':'class'}
dict={}
for key,value in student_data.items():
    if value not in dict.values():
        dict[key]=value
print(dict)