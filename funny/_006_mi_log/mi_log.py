import os

def countPv():
    path = r'C:\Users\Administrator\Desktop\zawu\20200306'
    list_count = 0
    detail_count = 0
    for file_name in os.listdir(path):
        file = open(os.path.join(path, file_name), 'r', encoding='utf-8')
        list_one_count = 0
        detail_one_count = 0
        while True:
            line = file.readline()
            if line:
                line = line.replace('\n', '')
                if line == 'method_name:getNewsListByCategoryId':
                    list_one_count += 1
                    list_count += 1
                elif line == 'method_name:getNewsDetailByNewsId':
                    detail_one_count += 1
                    detail_count += 1
            else:
                break
        print(file_name, '--', list_one_count, detail_one_count)
    print('list_count:', list_count)
    print('detail_count:', detail_count)

countPv()