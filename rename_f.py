import glob
import os
import csv

# 指定文件夹的路径
n_a = 'A11'
folder_path1 = "D:\\desk\\DATA\\"+ n_a +"\\csv"
folder_path2 = "D:\\desk\\DATA\\"+n_a+"\\excle"

# 获取文件夹中所有的csv文件名
csv_list1 = glob.glob(folder_path1 + '/*.csv')

csv_list2 = glob.glob(folder_path2 + '/*.xls')


# 按照创建时间排序
csv_list1 = sorted(csv_list1, key=lambda x: os.path.getctime(x))
# 或者按照修改时间排序
csv_list2 = sorted(csv_list2, key=lambda x: os.path.getmtime(x))

# 遍历每个csv文件

for j,f3 in enumerate(csv_list1):
    # 对文件名进行处理，把序号作为文件名，如1.csv，2.csv等
    new_name = os.path.dirname(f3) + '\\' + str(j+1) + '_'+n_a+'.csv'
    # 重命名文件
    os.rename(f3, new_name)
    
for j,f3 in enumerate(csv_list2):
    # 对文件名进行处理，把序号作为文件名，如1.csv，2.csv等
    new_name = os.path.dirname(f3) + '\\' + str(j+1) + '_'+n_a+'.xls'
    # 重命名文件
    os.rename(f3, new_name)