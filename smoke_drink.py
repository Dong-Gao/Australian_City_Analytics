
import json

def get_words():
    words = []
    file = open('smoke.txt', 'r', encoding='utf-8')
    while 1:
        line = file.readline().strip('\n')
        words.append(line)
        if not line:
            break
    return words
def attribute(tweet):
    score=0
    negative=['hate','no more','disgusting','awful','selfish','idiot','quit smoking','no smoking','no-smoking','No-Smoking','anti-smoking',
              'non-smoking','Non-Smoking','boozer','alcoholic','drunkard','wino','secondhand smoke','second-hand smoke','chainsmoker','heavey smoker',
              'chain smoker','pollution','stupid','garbage','rubbish',':,(', ":'(", ':\"(', ':((','TT',':(','escape','fuck','piss','stop','die','death',
              'hell','violence','fight','domestic violence','caught','police','sue','security','abuse','bustup','brawl','addictive','addicted']
    for n in negative:
        if n in tweet:
            score=score-1
    return score
def find(tweet, words, smokeResult):
    text = tweet['text']
    find = 0
    a=0
    for t in words:
        if t!='':
            if t in text:
                find = find + 1
            else:
                find=find
    if find > 0:
        #score = sentiment_analysis.sentiment_score(text)['compound']
        score=attribute(text)
        try:
            loc = tweet['location']
            #print(loc)
            for l in smokeResult:
                if l == loc:
                    if score >= 0:
                        smokeResult[l]['positive'] = smokeResult[l]['positive'] + 1
                    else:
                        smokeResult[l]['negative'] = smokeResult[l]['negative'] + 1
            return smokeResult
        except:
            a=a
def smoke_Drink_per(tweet,smokeResult):
    words=get_words()
    find(tweet,words,smokeResult)
    return smokeResult

def smoke_Drink_cloud(tweets,smokeResult):
    words=get_words()
    for tweet in tweets:
        find(tweet,words,smokeResult)
    return smokeResult

def smoke_Drink(smokeResult):
    words = get_words()
    filesource = open('status1.json', 'r', encoding='utf-8')
    for i in filesource:
        tweet = json.loads(i)
        #print(tweet)
        #print(tweet['location'])
        #for tweet in tweets:
        find(tweet, words, smokeResult)

    return smokeResult
def print_results(result):
    with open('output.txt', "w") as text_file:
        for each_result in result:
            print("City name: {} \n positive: {} \nnegative: {}.\n".format(
                each_result, result[each_result]['positive'],result[each_result]['negative']),
                  file=text_file)
