import re
import SentimentAnalysis
import couchdb

server = couchdb.Server()
text = server['text']
smokeResult={'negative':0, 'positive':0}
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
def smokeAndDrink(text,smokeResult):
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
            smokeResult['positive']= smokeResult['positive'] + 1
        else:
            smokeResult['negative']= smokeResult['negative'] + 1
    return smokeResult
smokeAndDrink(text,smokeResult)
print(smokeResult)
