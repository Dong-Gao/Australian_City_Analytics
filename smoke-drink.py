import re
import SentimentAnalysis
import couchdb

tweet = couchdb.Server('#######')
db=couch['######']


smokeResult={'Melbourne':{'positive':0,'negative':0},'Sydney':{'positive':0,'negative':0},
             'Peth':{'positive':0,'negative':0},'Darwin':{'positive':0,'negative':0},
             'Canberra':{'positive':0,'negative':0},'Hobart':{'positive':0,'negative':0},
             'Adelaide':{'positive':0,'negative':0},'Brisbane':{'positive':0,'negative':0}}
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
def find(tweet,smokeResult):
    text=server['text']
    loc=server['location']
    find = 0
    for t in trains:
        if t in text:
            find=find+1
        else:
            find=find
    if find>0:
        score=SentimentAnalysis.senti_analy(input)
        
        for l in smokeResult:
            if l==loc:
                if score>=0:
                    smokeResult[l]['positive']=smokeResult[l]['positive']+1
                else if score<0:
                    smokeResult[l]['negative']=smokeResult[l]['negative']+1
    return smokeResult
#########################  MAIN  ###############################################
def execute():
    trains=get_train()
    for tweet in db:
        find(tweet,smokeResult)
    print(smokeResult)
