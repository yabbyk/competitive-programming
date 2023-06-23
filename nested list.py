if __name__ == '__main__':
    records = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        sort_records = sorted(list(set([s[1] for s in records])))
    
    second_lowest = sort_records[1]



    low_list=[]
    for student in records:
        if second_lowest == student[1]:
            list.append(student[0])
    for student in sorted(low_list):
        print (student)
    
    
        
