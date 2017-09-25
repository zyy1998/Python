
# coding=utf-8
# 计算全校学生体测BMI,并生成 out.xlsx
#    time: 2017.9.7
import xlrd
import xlwt
def calcuBMIScore(list,row)  :
    if list[6] == "" or list[7] == "" or list[5] == "": # 信息缺失
        outSheet1.write(row-9, 6, "")
        outSheet1.write(row-9, 7, 0)
        return
    BMI = 0.0
    BMIScore = 0
    dengJi = ""
    tempBMI = float(list[7] / ((list[6] / 100) * (list[6] / 100)))
    BMI = round(tempBMI, 1)

    if BMI >= 28.0:
        BMIScore = 60
        dengJi='肥胖'
    if (BMI >= 24.0 and BMI <= 27.9):
        BMIScore = 80
        dengJi = '超重'
    # 男生
    if int(list[5]) == 1:
        if (BMI<=17.8):
            BMIScore = 80
            dengJi = '低体重'
        if BMI >= 17.9 and BMI <= 23.9:
            BMIScore = 100
            dengJi='正常'
    # 女生
    if int(list[5]) == 2:
        if (BMI<=17.1):
            BMIScore = 80
            dengJi = '低体重'
        if (BMI >= 17.2 and BMI <= 23.9):
            BMIScore = 100
            dengJi='正常'

    outSheet1.write(row-9, 6, str(BMI)+";"+dengJi)
    outSheet1.write(row-9, 7, BMIScore)

if __name__ == "__main__":
    # 打开文件
    inData = xlrd.open_workbook('in.xlsx')
    # 获取工作表
    sheet1 = inData.sheets()[0]
    # 创建工作表
    outData = xlwt.Workbook(encoding='utf-8')
    outSheet1 = outData.add_sheet('sheet1', cell_overwrite_ok=True)
    # 写入表头
    row0 = ['年级编号', '班级编号', '班级名称', '学籍号', '姓名', '性别', 'BMI', 'BMI分数', '肺活量', '50米跑', '立定跳远', '坐位体前屈', '800米跑',
            '1000米跑', '一分钟仰卧起坐', '引体向上', '总分']
    for i in range(0, len(row0)):
        outSheet1.write(0, i, row0[i])

    oneRowData = []
    for i in range(10,15265,1):
        for column in range(0,16,1):
            oneRowData.append(sheet1.cell(i, column).value)
            if column > 5:
                 continue
            outSheet1.write(i-9, column, oneRowData[column])
        calcuBMIScore(oneRowData,i)
        for index in range(0,len(oneRowData),1):
            oneRowData.pop()
# 保存文件
    outData.save('out.xlsx')

print ("finished")
