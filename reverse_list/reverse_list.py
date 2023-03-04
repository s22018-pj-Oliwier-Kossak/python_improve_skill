to_reverse = [1,2,3,4,5]


revers_list = list(reversed(to_reverse))
print(revers_list)

revers_list2 = to_reverse[::-1]
print(revers_list2)
revers_list3 = []

for i in to_reverse:
    revers_list3.insert(0,i)

print(revers_list3)


