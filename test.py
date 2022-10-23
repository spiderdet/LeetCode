# 计算一个文件夹所有文件的大小
import os


def getTotalsize(path_add):
    size = 0
    # 遍历并装载第一层的文件和文件夹
    list = os.listdir(path_add)

    for i in list:
        # 拼接成完整的绝对路径
        pathfile = os.path.join(path_add, i)
        # 文件 OR NOT
        if os.path.isfile(pathfile):
            # print(i," is FILE")
            # print(pathfile)
            # 统计文件大小
            size += os.path.getsize(pathfile)
        # 文件夹 OR NOT
        elif os.path.isdir(pathfile):
            # print(i," is FOLDER")
            # print(pathfile)
            # 递归统计文件夹里面的文件名称
            size += getTotalsize(pathfile)

    return size


num = 100
path_cwd = r'H:/pt资源/极客时间/'
lst = os.listdir(path_cwd)
print(lst)
map1 = {}
for dir in lst:
    if int(dir[0:2])<=num:
        path_add = os.path.join(path_cwd, dir)  # 添加指定的文件夹
        print(path_add)
        result = getTotalsize(path_add)
        map1[dir]=result
        print("Total size:{}字节({}MB)".format(result, result // 1024 // 1024))  # 输出总大小

path_cwd = r'H:/pt资源/极客时间-2/'
lst2 = os.listdir(path_cwd)
print(lst2)
map2 = {}
for dir in lst:
    if int(dir[0:2]) <= num:
        path_add = os.path.join(path_cwd, dir)  # 添加指定的文件夹
        print(path_add)
        result = getTotalsize(path_add)
        map2[dir]=result
        print("Total size:{}字节({}MB)".format(result, result // 1024 // 1024))  # 输出总大小

bundle = []
result = []
size = 0
for key,value in map1.items():

    if value == map2[key]:
        print(key,value/1024/1024/1024)
        if value >11:
            size+= value
print(size/1024/1024/1024)

