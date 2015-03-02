from lib import csv_io
from lib import json_io

'''
add category
'''
drug_list = csv_io.read_csv('hyper_drug_cate.csv')
name_list = csv_io.read_csv('drug_name_list.csv')
data_list = csv_io.read_csv('hyper_drug.csv')

drug_dic = {}

for i in range(0, len(drug_list)):
    drug_dic[drug_list[i][0]] = drug_list[i][1]

name_dic = {}
for i in range(0, len(name_list)):
    name_dic[name_list[i][0]] = name_list[i][1]

for i in range(0, len(data_list)):
    if data_list[i][1] in drug_dic:
        data_list[i].append(drug_dic[data_list[i][1]])
        if data_list[i][1] in name_dic:
            data_list[i][1] = name_dic[data_list[i][1]]
    else:
        data_list[i].append('')

'''
get repeat drug data
'''
data_list = sorted(data_list, key=lambda x: x[5])

p_list = {}
for row in data_list:
    if row[0] not in p_list:
        p_list[row[0]] = [row]
    else:
        p_list[row[0]].append(row)

date = ''
finish_date = ''
cate = []
repeat_dic = {}
for ID, records in p_list.iteritems():
    for row in records:
        if date == int(row[5]):
            continue
        if row[7] in cate and int(row[5]) < finish_date:
            repeat_dic[ID] = records
            break
        finish_date = int(row[5]) + int(row[6])
        date = int(row[5])
        cate.append(row[7])
    date =  ''
    cate = []
    finish_date = ''

json_io.write_json('hyper_drug_repeat.json', repeat_dic)
