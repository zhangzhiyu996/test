#tf_idf值越高代表在本篇文章中的独特性
import math
dic = {}
dct = {}
dd = {}
def tf(t, d):
    if t in dd[d]:
        return float(dd[d][t]) / dic[t]
    else:
        return 0
def idf(t):
    num = 0
    for i in range(0, 300):
        if t in dd[i]:
            num += 1
    return math.log(300.0 / num)
def Euclid_d(d1, d2):
    ans = 0.0
    for i in dic:
        ans += (dct[d1][i] - dct[d2][i]) * (dct[d1][i] - dct[d2][i])
    return math.sqrt(ans)
def Cosine_s(d1, d2):
    ans1 = 0.0
    ans2 = 0.0
    ans3 = 0.0
    for i in dic:
        ans1 += dct[d1][i] * dct[d2][i]
        ans2 += dct[d1][i] * dct[d1][i]
        ans3 += dct[d2][i] * dct[d2][i]
    return abs(ans1) / math.sqrt(ans2) / math.sqrt(ans3) 
a = [',', '.', '?', '!', '@', ':', '&', '(', ')', '"', "'", ';', ' ']
for i in range(0, 300):
    u = "/home/zzy/redcross/hw1/hw1/nyt_corp0/nyt_corp0/" + str(i)
    f = open(u)
    r = f.read()
    ls = r.split()
    lst = []
    for j in ls:
        for k in a:
            j = j.strip(k)
        lst.extend([j])
    di = {}
    for item in lst:
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
        if item in di:
            di[item] += 1
        else:
            di[item] = 1
    dd[i] = di
print(len(dic))
id = {}
for i in dic:
    id[i] = idf(i)
for i in range(0, 300):
    dct[i] = {}
    for j in dic:
        dct[i][j] = float(tf(j, i)) * id[j]
mi = Euclid_d(31, 0)
min = 0
for i in range(1, 300):
    if(mi > Euclid_d(31, i) and i != 31):
        min = i
        mi = Euclid_d(31, i)
print(min, mi)
ma = Cosine_s(31, 0)
max = 0
for i in range(1, 300):
    if(ma < Cosine_s(31, i) and i != 31):
        max = i
        ma = Cosine_s(31, i)
print(max, ma)
