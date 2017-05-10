import matplotlib.pyplot as plt
import numpy as np

final_result ={'Melbourne':{'0-6': {'total': 346756.8215000196, 'amount': 1574572, 'positive': 792449, 'negative': 220545, 'neutral': 561578}, '6-12': {'total': 298451.1661001414, 'amount': 1381525, 'positive': 689611, 'negative': 206124, 'neutral': 485790}, '12-18': {'total': 71436.3012999878, 'amount': 363493, 'positive': 174054, 'negative': 59317, 'neutral': 130122}, '18-24': {'total': 174975.5080000411, 'amount': 808130, 'positive': 406476, 'negative': 118388, 'neutral': 283266}}, 'Sydney':{'0-6': {'total': 375024.6058999546, 'amount': 1748133, 'positive': 869462, 'negative': 249105, 'neutral': 629566}, '6-12': {'total': 319744.58200011676, 'amount': 1495411, 'positive': 742243, 'negative': 223810, 'neutral': 529358}, '12-18': {'total': 74866.51659998334, 'amount': 389189, 'positive': 184730, 'negative': 64246, 'neutral': 140213}, '18-24': {'total': 213088.59800011534, 'amount': 1006727, 'positive': 499899, 'negative': 148049, 'neutral': 358779}},'Perth':{'0-6': {'total': 78684.2003999896, 'amount': 349810, 'positive': 176825, 'negative': 47625, 'neutral': 125360}, '6-12': {'total': 74327.33239999131, 'amount': 323544, 'positive': 164008, 'negative': 43503, 'neutral': 116033}, '12-18': {'total': 37833.34969999946, 'amount': 161640, 'positive': 82048, 'negative': 22217, 'neutral': 57375}, '18-24': {'total': 21034.343000000474, 'amount': 95954, 'positive': 47932, 'negative': 13768, 'neutral': 34254}}, 'Darwin':{'0-6': {'total': 7927.801400000074, 'amount': 38644, 'positive': 18774, 'negative': 5668, 'neutral': 14202}, '6-12': {'total': 6491.911599999957, 'amount': 30911, 'positive': 15298, 'negative': 4784, 'neutral': 10829}, '12-18': {'total': 1818.3056999999953, 'amount': 8699, 'positive': 4287, 'negative': 1385, 'neutral': 3027}, '18-24': {'total': 3205.3958999999427, 'amount': 16125, 'positive': 7849, 'negative': 2518, 'neutral': 5758}}, 'Canberra':{'0-6': {'total': 42714.38309999754, 'amount': 211296, 'positive': 103841, 'negative': 32104, 'neutral': 75351}, '6-12': {'total': 35648.08140000032, 'amount': 166599, 'positive': 83385, 'negative': 25429, 'neutral': 57785}, '12-18': {'total': 6942.710900000083, 'amount': 35595, 'positive': 17083, 'negative': 5958, 'neutral': 12554}, '18-24': {'total': 23284.322600000614, 'amount': 116461, 'positive': 57357, 'negative': 18517, 'neutral': 40587}}, 'Hobart':{'0-6': {'total': 13724.713999999762, 'amount': 67363, 'positive': 33060, 'negative': 10201, 'neutral': 24102}, '6-12': {'total': 11632.782999999901, 'amount': 54913, 'positive': 27052, 'negative': 8237, 'neutral': 19624}, '12-18': {'total': 2305.593499999988, 'amount': 11640, 'positive': 5622, 'negative': 1929, 'neutral': 4089}, '18-24': {'total': 7544.852100000141, 'amount': 36245, 'positive': 17807, 'negative': 5400, 'neutral': 13038}},
'Adelaide':{'0-6': {'total': 72679.42059998855, 'amount': 311953, 'positive': 160102, 'negative': 41503, 'neutral': 110348}, '6-12': {'total': 63338.03149999169, 'amount': 272502, 'positive': 139254, 'negative': 37791, 'neutral': 95457}, '12-18': {'total': 16985.714599999446, 'amount': 79853, 'positive': 39253, 'negative': 12360, 'neutral': 28240}, '18-24': {'total': 31718.935800001585, 'amount': 138770, 'positive': 71045, 'negative': 19481, 'neutral': 48244}}, 'Brisbane':{'0-6': {'total': 160448.1419000175, 'amount': 724118, 'positive': 363879, 'negative': 99958, 'neutral': 260281}, '6-12': {'total': 138502.80579998263, 'amount': 631846, 'positive': 315964, 'negative': 92254, 'neutral': 223628}, '12-18': {'total': 31654.718800001647, 'amount': 159947, 'positive': 76345, 'negative': 25469, 'neutral': 58133}, '18-24': {'total': 88248.61559998107, 'amount': 399073, 'positive': 201220, 'negative': 56976, 'neutral': 140877}}}

#print("Total tweets: 13210681")
scoreResult = {'Melbourne': {'0-6': 0.2202229059706508, '6-12': 0.21603023188153772, '12-18': 0.1965273094667237, '18-24': 0.2165190105552833}, 'Sydney': {'0-6': 0.2145286462185398, '6-12': 0.21381719273170838, '12-18': 0.19236544866371696, '18-24': 0.21166472936567246}, 'Perth': {'0-6': 0.22493410823015236, '6-12': 0.22972866874363707, '12-18': 0.23405932751793776, '18-24': 0.21921277903996159}, 'Darwin': {'0-6': 0.20514960666597853, '6-12': 0.21001946232732543, '12-18': 0.2090246809978153, '18-24': 0.19878424186046156}, 'Canberra': {'0-6': 0.20215424380962035, '6-12': 0.2139753623971352, '12-18': 0.1950473633937374, '18-24': 0.19993236018925317}, 'Hobart': {'0-6': 0.2037426183513169, '6-12': 0.21184023819496114, '12-18': 0.19807504295532544, '18-24': 0.20816256311215728}, 'Adelaide': {'0-6': 0.23298195753843862, '6-12': 0.2324314372004304, '12-18': 0.21271229133532174, '18-24': 0.2285719953880636}, 'Brisbane': {'0-6': 0.22157734222877695, '6-12': 0.21920342266942044, '12-18': 0.197907549375741, '18-24': 0.2211340170845461}}

cities = ['MEL', 'SYD', 'PER', 'DRW', 'CBR', 'HBA', 'ADL', 'BNE']
time = ['0-6','6-12','12-18','18-24']

#Drawing a bar chart of average sentiment score for each city
avgScore = []
for city in final_result:
    totals = final_result[city]['0-6']['total']+final_result[city]['6-12']['total']+final_result[city]['12-18']['total']+final_result[city]['18-24']['total']
    amounts = final_result[city]['0-6']['amount']+final_result[city]['6-12']['amount']+final_result[city]['12-18']['amount']+final_result[city]['18-24']['amount']
    avg = totals/amounts
    avgScore.append(avg)
    print(city)
    print(avg)
x=np.arange(8)+1
y=np.array(list(avgScore))
plt.bar(x, y, width = 0.5, tick_label=cities)
plt.xlabel('City')
plt.ylabel('Score')
plt.title('Average Sentiment Score')
for a,b in zip(x, y):
    plt.text(a, b+0.0025, '%.3f' % b, ha='center', va='bottom',fontsize=8)
plt.ylim(0, 0.30)
#plt.legend()
#plt.plot(x, y, label='First Line')
plt.show()
plt.savefig("avg.png")


#Drawing a bar chart of positive/negative percentage for each city
pos = []
neg = []
neu = []

for city in final_result:
    amounts = final_result[city]['0-6']['amount'] + final_result[city]['6-12']['amount'] + final_result[city]['12-18']['amount'] + final_result[city]['18-24']['amount']
    pos_num = final_result[city]['0-6']['positive'] + final_result[city]['6-12']['positive'] + final_result[city]['12-18']['positive'] + final_result[city]['18-24']['positive']
    neg_num = final_result[city]['0-6']['negative'] + final_result[city]['6-12']['negative'] + final_result[city]['12-18']['negative'] + final_result[city]['18-24']['negative']
    neu_num = final_result[city]['0-6']['neutral'] + final_result[city]['6-12']['neutral'] + final_result[city]['12-18']['neutral'] + final_result[city]['18-24']['neutral']
    postive = pos_num/amounts
    negative = neg_num/amounts
    neutral = neu_num/amounts
    pos.append(postive)
    neg.append(negative)
    neu.append(neutral)

x=np.arange(8)+1
y1=np.array(list(pos))
y2=np.array(list(neg))
y3=np.array(list(neu))
plt.bar(x, y1, width = 0.5, tick_label=cities, label = 'positive')
plt.bar(x, y2, width = 0.5, bottom=y1, tick_label=cities, label = 'negative')
plt.bar(x, y3, width = 0.5, bottom=y1+y2, tick_label=cities, label = 'neutral')
plt.xlabel('City')
plt.ylabel('Percentage')
plt.title('Sentiment Percentage Statistic')
for a,b in zip(x, y1):
    plt.text(a, 0.3, '%.3f' % b, ha='center', va='bottom',fontsize=8)
for a,b in zip(x, y2):
    plt.text(a, 0.55, '%.3f' % b, ha='center', va='bottom',fontsize=8)
for a,b in zip(x, y3):
    plt.text(a, 0.8, '%.3f' % b, ha='center', va='bottom',fontsize=8)
plt.ylim(0, 1.15)
plt.yticks(np.linspace(0, 1, 11, endpoint=True))

plt.legend(loc=9, ncol=3, bbox_to_anchor=(0.5,0.98))
plt.show()
plt.savefig("percentage.png")

#Drawing a line chart of Time-Happiness statistics for each city and the average of all cities
fig, ax = plt.subplots(nrows=3, ncols=3)
time_score = []
t1,t2,t3,t4 = 0,0,0,0
a1,a2,a3,a4 = 0,0,0,0
for city in final_result:
    t1 += final_result[city]['0-6']['total']
    t2 += final_result[city]['6-12']['total']
    t3 += final_result[city]['12-18']['total']
    t4 += final_result[city]['18-24']['total']
    a1 += final_result[city]['0-6']['amount']
    a2 += final_result[city]['6-12']['amount']
    a3 += final_result[city]['12-18']['amount']
    a4 += final_result[city]['18-24']['amount']
time_score.append([t1/a1, t2/a2, t3/a3, t4/a4])

for city in scoreResult:
    temp = []
    temp.append(scoreResult[city]['0-6'])
    temp.append(scoreResult[city]['6-12'])
    temp.append(scoreResult[city]['12-18'])
    temp.append(scoreResult[city]['18-24'])
    time_score.append(temp)

plt.suptitle("Time Score Statistic")
plt.subplot(3, 3, 1)
x=np.arange(4)+1
y1 = time_score[0]
plt.plot(x, y1,marker='x')
plt.xlabel('Time',fontsize=8)
plt.ylabel('Score',fontsize=8)
plt.title('All Cities',fontsize=8)
plt.xticks(x, time,fontsize=8)
plt.ylim(0.19,0.24)
plt.yticks(np.linspace(0.19,0.24, 6, endpoint=True),fontsize=8)

plt.subplot(3, 3, 2)
y2 = time_score[1]
plt.plot(x, y2)
plt.xlabel('Time',fontsize=8)
plt.ylabel('Score',fontsize=8)
plt.title('MEL',fontsize=8)
plt.xticks(x, time,fontsize=8)
plt.ylim(0.19,0.24)
plt.yticks(np.linspace(0.19,0.24, 6, endpoint=True),fontsize=8)

plt.subplot(3, 3, 3)
y3 = time_score[2]
plt.plot(x, y3)
plt.xlabel('Time',fontsize=8)
plt.ylabel('Score',fontsize=8)
plt.title('SYD',fontsize=8)
plt.xticks(x, time,fontsize=8)
plt.ylim(0.19,0.24)
plt.yticks(np.linspace(0.19,0.24, 6, endpoint=True),fontsize=8)

plt.subplot(3, 3, 4)
y4 = time_score[3]
plt.plot(x, y4)
plt.xlabel('Time',fontsize=8)
plt.ylabel('Score',fontsize=8)
plt.title('PER',fontsize=8)
plt.xticks(x, time,fontsize=8)
plt.ylim(0.19,0.24)
plt.yticks(np.linspace(0.19,0.24, 6, endpoint=True),fontsize=8)

plt.subplot(3, 3, 5)
y5 = time_score[4]
plt.plot(x, y5)
plt.xlabel('Time',fontsize=8)
plt.ylabel('Score',fontsize=8)
plt.title('DRW',fontsize=8)
plt.xticks(x, time,fontsize=8)
plt.ylim(0.19,0.24)
plt.yticks(np.linspace(0.19,0.24, 6, endpoint=True),fontsize=8)

plt.subplot(3, 3, 6)
y6 = time_score[5]
plt.plot(x, y6)
plt.xlabel('Time',fontsize=8)
plt.ylabel('Score',fontsize=8)
plt.title('CBR',fontsize=8)
plt.xticks(x, time,fontsize=8)
plt.ylim(0.19,0.24)
plt.yticks(np.linspace(0.19,0.24, 6, endpoint=True),fontsize=8)

plt.subplot(3, 3, 7)
y7 = time_score[6]
plt.plot(x, y7)
plt.xlabel('Time',fontsize=8)
plt.ylabel('Score',fontsize=8)
plt.title('HBA',fontsize=8)
plt.xticks(x, time,fontsize=8)
plt.ylim(0.19,0.24)
plt.yticks(np.linspace(0.19,0.24, 6, endpoint=True),fontsize=8)

plt.subplot(3, 3, 8)
y8 = time_score[7]
plt.plot(x, y8)
plt.xlabel('Time',fontsize=8)
plt.ylabel('Score',fontsize=8)
plt.title('ADL',fontsize=8)
plt.xticks(x, time,fontsize=8)
plt.ylim(0.19,0.24)
plt.yticks(np.linspace(0.19,0.24, 6, endpoint=True),fontsize=8)

plt.subplot(3, 3, 9)
y9 = time_score[8]
plt.plot(x, y9)
plt.xlabel('Time',fontsize=8)
plt.ylabel('Score',fontsize=8)
plt.title('BNE',fontsize=8)
plt.xticks(x, time,fontsize=8)
plt.ylim(0.19,0.24)
plt.yticks(np.linspace(0.19,0.24, 6, endpoint=True),fontsize=8)

fig.tight_layout()
plt.show()
plt.savefig("time_happiness.png")


