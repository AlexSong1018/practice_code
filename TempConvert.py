TempStr=input("输入一个温度值，以F或C结尾：")
l=TempStr[-1]
inputTemp=int(TempStr[0:-1])
if l in ['c','C']:
    F=inputTemp*1.8+32
    print("转换为F为：",F,"F")
elif l in ['f','F']:
    C=(inputTemp-32)/1.8
    print("转换为C为：",C,"C")
else:
    print("格式错误，请重新输入")