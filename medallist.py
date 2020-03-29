class Medal:
    def __init__(self,country,gold,silver,bronze):
        self.country = country
        self.gold = gold
        self.silver = silver
        self.bronze = bronze

    def newget(self,newgold=0,newsilver=0,newbronze=0):
        self.gold += newgold
        self.silver += newsilver
        self.bronze += newbronze

    def count(self):
        self.totalmedal= self.gold+self.silver+self.bronze
        return ('%s,%d,%d,%d,%d'%(self.country,self.gold,self.silver,self.bronze,self.totalmedal))



usa = Medal('usa',2,3,4)
usa.newget(5,4,3)
usa.count()


china = Medal('China',3,5,7)
usa.newget(5,8,1)
china.count()


uk = Medal('uk',4,1,2)
uk.newget(1,4,2)
uk.count()

usmd = usa.count()
chinamd = china.count()
ukmd = uk.count()

l = [usmd.split(','),chinamd.split(','),ukmd.split(',')]

print('金牌榜序：\n')
print('国家   金牌  银牌  铜牌  总奖牌数')
gdrk = sorted(l,key = lambda x:x[1],reverse=True)
for m in gdrk:
    m.append('\n')
    m = '   '.join(m)
    print(m)

print('奖牌榜序：\n')
print('国家   金牌  银牌  铜牌  总奖牌数')
mdrk = sorted(l,key = lambda x:x[-1],reverse=True)
for m in mdrk:
    m.append('\n')
    m = '   '.join(m)
    print(m)
