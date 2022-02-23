dict = {}
count_1 = 0
count_2 = 0
count_3 = 0
i = 0
num = 0
info_1 = ''
info_2 = ''
info_3 = ''
import os
path = os.getcwd()
file_name_1 = '1.txt'
full_1_path = os.path.join(path, file_name_1)
file_name_2 = '2.txt'
full_2_path = os.path.join(path, file_name_2)
file_name_3 = '3.txt'
full_3_path = os.path.join(path, file_name_3)
with open(full_1_path, 'r', encoding = 'utf-8') as file:
    for line in file:
        count_1 += 1
        info_1 += line
    if count_1 > i:
        i = count_1
with open(full_2_path, 'r', encoding = 'utf-8') as file:
    for line in file:
        count_2 += 1
        info_2 += line
    if count_2 > i:
        i = count_2
with open(full_3_path, 'r', encoding = 'utf-8') as file:
    for line in file:
        count_3 += 1
        info_3 += line
    if count_3 > i:
        i = count_3
dict[str(count_1)] = file_name_1
dict[str(count_2)] = file_name_2
dict[str(count_3)] = file_name_3
while num <= i:
    if str(num) in dict.keys():
        print(dict[str(num)])
        print(num)
        if num == count_1:
            print(info_1)
        if num == count_2:
            print(info_2)
        if num == count_3:
            print(info_3)
    num += 1