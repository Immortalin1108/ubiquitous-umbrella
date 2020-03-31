import requests

#读取记录
def record():
    global scores,game_times,min_times,total_times
    f = open('user_records.txt','r+')
    lines = f.readlines()
    f.close()
    scores = {}
    for l in lines:
        s = l.split()
        scores[s[0]] = s[1:]
    score = scores.get(name)
    #print(score)
    if score is None:
        score = [0,0,0]

    game_times = int(score[0])
    min_times = int(score[1])
    total_times = int(score[2])

    if game_times > 0:
        avg_times = total_times / game_times
    else:
        avg_times = 0

    print('%s，你已经玩了%d次，最少%d轮猜出答案，平均%.2f轮猜出答案'%(name,game_times,min_times,avg_times))

#猜数字
def guess():
    global scores,game_times, min_times, total_times
    times = 0
    # 从网络上获取正确答案
    url = "https://python666.cn/cls/number/guess/"
    num = requests.get(url)
    num = int(num.text)
    print('猜猜我想的是几？')
    while True:
        times += 1
        ans = int(input())
        if ans > num:
            print(ans,'太大了')
        elif ans < num:
            print(ans,'太小了')
        else:
            print('你猜对了')
            break

    if game_times == 0 or times < min_times:
        min_times = times
    total_times += times
    game_times += 1

    scores[name] = [str(game_times),str(min_times),str(total_times)]
    result = ''
    for n in scores:
        line = n + ' ' +' '.join(scores[n])+'\n'
        result += line

    f = open('user_records.txt','w')
    f.write(result)
    f.close()


#输入玩家名字
name  = input('请输入你的名字：')
a = True
while a:
    record()
    guess()
    y = input('是否想要再玩一局？（输入“y”继续，否则退出）')
    if y != 'y':
        a = False
