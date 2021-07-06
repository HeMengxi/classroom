s="语文:80,数学:82,英语:90,物理:85,化学:88,美术:80"
list=s.split(',')  #对字符串s进行切片，以列表形式表示
Score_list=[] #构造分数空列表，只记录分数
total=0
for x in list:
    # 运用切片，将各科分数加入分数列表
    Score_list.append(x[3:])
# 遍历分数列表，分数求和
for x in Score_list:
    y=int(x)
    total=total+y
print("总分：",total)
#求平均分 ，保留一位小数
avg=total/6
print("平均分：","%3.1f"%avg)

