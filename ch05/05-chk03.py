#%% 중간점검 3, 05-chk03.py 
lst = [1, 5]
lst[0] = 3
lst.append(7)
lst[1:3] = [10]
print(lst)

lst = [1, 5, 1, 7, 1]
lst[lst.count(1)] = 70
lst[len(lst)-1] = 80
lst.insert(1, 50)
print(lst)
