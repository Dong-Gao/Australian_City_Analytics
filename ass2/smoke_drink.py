import re
import sentiment_analysis
import couchdb

def test_data():
    test=[{'location':'Melbourne','text':'beer BMW happy! cigar'},{'location':'Melbourne','text':'pint Ford sorry!'},{'location':'Peth','text':'Who has fire lighter? VW :)! cigar'},{'location':'Canberra','text':'Holden,new car! so cheerful!'}]
    return test
def get_words():
    words = []
    file = open('smoke.txt', 'r', encoding='utf-8')
    while 1:
        line = file.readline().strip('\n')
        words.append(line)
        if not line:
            break
    return words

def find(tweet, words, smokeResult):
    text = tweet['text']
    loc = tweet['location']
    find = 0
    for t in words:
        if t in text:
            find = find + 1
        else:
            find = find
    if find > 0:
        #score = sentiment_analysis.sentiment_score(text)['compound']
        score=0
        for l in smokeResult:
            if l == loc:
                if score > 0:
                    smokeResult[l]['positive'] = smokeResult[l]['positive'] + 1
                elif score == 0:
                    smokeResult[l]['tolerant'] = smokeResult[l]['tolerant'] + 1
                else:
                    smokeResult[l]['negative'] = smokeResult[l]['negative'] + 1
    return smokeResult


def smoke_Drink(smokeResult):
    words = get_words()
    #server = couchdb.Server('placeholer')
    #db = server['placeholer']
    #for tweet in db:
    #    find(tweet, words, smokeResult)
    test=test_data()
    for i in range(0,len(test)):
        find(test[i],words,smokeResult)
    return smokeResult