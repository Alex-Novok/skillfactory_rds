f = open('StudentsPerformance.csv')
education_list_1=[]
education_list_2=[]
for line in f:
    list_string=line.split(',')
    if list_string[2][1:-1]=="parental level of education":
        continue
    else:
        education_list_1.append(list_string[2][1:-1])
education_list_1.sort()
education_list_2.append(education_list_1[0]) 
for i in range(len(education_list_1)):
    if i+1==len(education_list_1):
        break
    elif education_list_1[i+1]!=education_list_1[i]:
        education_list_2.append(education_list_1[i+1])
    else:
        continue
print(education_list_2)