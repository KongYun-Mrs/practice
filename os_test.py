import os

# version = os.environ
# print(version)
# if os.path.exists('./test'):
#     os.removedirs('./test')
# print(os.listdir())
# # 不可递归创建
# # os.mkdir('./public/dir2/tops2/toto2')
# if not os.path.exists('./public/dir2/tops2/toto2'):
#     os.makedirs('./public/dir2/tops2/toto2')
#
# # 文件路径操作
# print(os.path.basename('public'))  # /返回当前文件或者目录名称
# print(os.path.dirname(''))  # 返回当前目录的上层目录
#
# print(os.path.split('./public/dir2/tops2/toto2'))
# 将文件后缀进行分离，返回一个元组，元组的第一个元素为除过文件名称后缀剩余部分，第二个元素为文件后缀；当文件没有后缀的时候，第二个元素为空。
# os.path.splitext('./Smart.py')

list1 = os.listdir('./Soul')
print(list1)
for name in list1:
    oldname = os.path.join('./Soul', name)
    new_name = os.path.join('./Soul', os.path.splitext(name)[0] + '.py')
    os.renames(oldname, new_name)
