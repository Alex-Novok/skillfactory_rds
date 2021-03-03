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
