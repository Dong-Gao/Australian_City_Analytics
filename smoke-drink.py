import re
import SentimentAnalysis
import couchdb

tweet = couchdb.Server()
#text = server['text']
#loc = server['location']
smokeResult={'Melbourne':0,'Sydney':0,'Peth':0,'Darwin':0,'Canberra':0,'Hobart':0,'Adelaide':0,'Brisbane':0}
def get_train():
    train=[]
    file=open('smoke.txt', 'r', encoding='utf-8')
    while 1:
        line=file.readline().strip('\n')
        train.append(line)
        if not line:
            break
    return  train
def score2dic(score):
    if score>=0:
        smokeResult['positive']= smokeResult['positive'] + 1
    else:
        smokeResult['negative']= smokeResult['negative'] + 1
def smokeAndDrink(tweet,smokeResult):
    text=server['text']
    loc=server['location']
    find = 0
    trains=get_train()
    for t in trains:
        if t in text:
            find=find+1
        else:
            find=find
    if find>0:
        score=SentimentAnalysis.senti_analy(input)
        if score>=0:
            for l in smokeResult:
                if l==loc:
                    smokeResult[l]=smokeResult[l]+1
                    break
    return smokeResult
smokeAndDrink(text,smokeResult)
print(smokeResult)
