# coding=utf-8
# Function：将体积较大、分辨率较高的小萝莉的照片挑选出来
# Time：2017.9.23.00:23
import os
import shutil   #名字来源于 shell utilities
count = 1
for root,dirs,files in os.walk("E:\图片\【批量下载】动漫图包全部等".decode('utf-8')):  #递归列出该文件夹下的所有子目录及子文件
        #根目录，目录文件名，文件名
    for file in files:
        fullName = os.path.join(root,file)      #将文件名合并为绝对路径
        if (os.stat(fullName).st_size >300000):    #如果文件大于300k
            shutil.copyfile(fullName, "E:\\temp\\" + str(count) + ".JPG")  # 将该文件复制至另一个文件并重命名
            count = count+1
print "finished"

# for filename in os.listdir(path.decode('utf-8')):       #中文路径需要设置编码格式
#     if filename.find(".JPG")>0:                         #如果找到.JPG的图片
#         print os.stat(path.decode('utf-8') + filename).st_size  #查看文件大小
#         #if(300000)
#         if(os.stat(path.decode('utf-8') + filename).st_size>500000):
#             shutil.copyfile(path.decode('utf-8')+filename,"E:\\temp\\"+str(count)+".JPG")   #将该文件复制至另一个文件
#             count = count+1



