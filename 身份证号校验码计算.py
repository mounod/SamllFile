num =int(37131220080329000)
while ( num < 37131220080329998):
    xishu = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2]
    qiumo = [1, 0, 'X', 9, 8, 7, 6, 5, 4, 3, 2]
    sum = 0
    num =str(num)
    for i in range(17):
        sum += int(num[i])*int(xishu[i])
    yu = sum%11
    yanzheng = qiumo[yu]
    #print("验证码为：%s"%yanzheng)
    print("身份证号码为：%s%s"%(str(num),str(yanzheng)))
    num = int(num)
    num = num + 2