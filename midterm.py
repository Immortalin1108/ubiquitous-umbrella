with open('report.txt',encoding='utf8') as f:
    scores = f.readlines()
    rpt = []
    for l in scores:
        if l:
            l = l.strip()
            rpt.append(l)
#print(rpt)

lists=[]
for i in rpt:
    i = i.split(' ')
    lists.append(i)
#print(lists)
lists[0].append('总成绩')
lists[0].append('平均分')
lists[0].insert(0,'名次')
#print(lists)
y = len(lists)
for i in range(1,y):
    l = lists[i]
#   print(l)
    s= 0
    for j in range(1,10):
        s+= int(l[j])
        avg=s/9
    avg = format(avg,'.2f')
    avg = str(avg)
    lists[i].append(str(s))
    lists[i].append(avg)
#print(lists)
scores=[]
scores=lists[1:]
#print(scores)

rk=sorted(scores,key=lambda x: x[-1],reverse=True)
#print(rk)

mavg=[]
mavg.append('平均')
for i in range(1,12):
    s = 0
    a = 0
    for lst in rk:
        s += float(lst[i])
        a = s/len(rk)
        a = format(a,'.2f')
        a = str(a)
    mavg.append(a)
rk.insert(0,mavg)
#print(rk)

n = 0
for l in rk:
    l.insert(0,str(n))
    n +=1
#print(rk)

for l in rk[1:]:
    for i in range(2,11):
        if int(l[i]) < 60:
            l[i] = '不及格'
#print(rk)

rk.insert(0,lists[0])

f=open('results.txt','w')
for l in rk:
    l.append('\n')
    m = '   '.join(l)
    f.write(m)
f.close()