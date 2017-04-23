import re
import SentimentAnalysis
import couchdb



def get_words():
    words=[]
    file=open('smoke.txt', 'r', encoding='utf-8')
    while 1:
        line=file.readline().strip('\n')
        words.append(line)
        if not line:
            break
    return  words
def score2dic(score):
    if score>=0:
        smokeResult['positive']= smokeResult['positive'] + 1
    else:
        smokeResult['negative']= smokeResult['negative'] + 1
def find(tweet,words,smokeResult):
    
    text=tweet['text']
    loc=tweet['location']
    find = 0
    for t in words:
        if t in text:
            find=find+1
        else:
            find=find
    if find>0:
        score=SentimentAnalysis.sentiment_score(text)
        
        for l in smokeResult:
            if l==loc:
                if score>=0:
                    smokeResult[l]['positive']=smokeResult[l]['positive']+1
                else if score<0:
                    smokeResult[l]['negative']=smokeResult[l]['negative']+1
    return smokeResult
def smoke_Drink(smokeResult):
    words=get_words()
    server = couchdb.Server('placeholer')
    db=server['placeholer']
    for tweet in db:
        find(tweet,words,smokeResult)
    return smokeResult
    
