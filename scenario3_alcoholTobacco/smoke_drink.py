# Cluster and Cloud Computing
# Group Project
# Team 16
#
# Kaile Wei: 812381
# Nanjiang Li: 741524
# Hongzhen Xie: 773383
# Dong Gao: 795622
# Chuang Ying: 844566

import json

def get_result():
    result = {'Melbourne': {'positive': 0, 'negative': 0, 'rate': 0,'female_rate':0.4937},
                   'Sydney': {'positive': 0, 'negative': 0, 'rate': 0,'female_rate':0.4941},
                   'Perth': {'positive': 0, 'negative': 0, 'rate': 0,'female_rate':0.4851},
                   'Darwin': {'positive': 0, 'negative': 0, 'rate': 0,'female_rate':0.4533},
                   'Canberra': {'positive': 0, 'negative': 0, 'rate': 0,'female_rate':0.4926},
                   'Hobart': {'positive': 0, 'negative': 0, 'rate': 0,'female_rate':0.4834},
                   'Adelaide': {'positive': 0, 'negative': 0, 'rate': 0,'female_rate':0.4908},
                   'Brisbane': {'positive': 0, 'negative': 0, 'rate': 0,'female_rate':0.4944}}
    return result

#read text file of smoking and alcohol words, and return the list of words
def get_words():
    words = []
    file = open('smoke.txt', 'r', encoding='utf-8')
    while 1:
        line = file.readline().strip('\n')
        words.append(line)
        if not line:
            break
    return words

#for each tweet, if any words of the negative word list, the tweet is assigned with a negative score,
#else with a score of 0.
def attribute(tweet):
    score=0
    negative=['hate','no more','disgusting','awful','selfish','idiot','quit smoking','no smoking','no-smoking','No-Smoking','anti-smoking',
              'non-smoking','Non-Smoking','boozer','alcoholic','drunkard','wino','secondhand smoke','second-hand smoke','chainsmoker','heavey smoker',
              'chain smoker','pollution','stupid','garbage','rubbish',':,(', ":'(", ':\"(', ':((','TT',':(',':o(','>:o(',':-(',  '):', ')-:', ':c',':-<','>:(',
              'escape','fuck','piss','stop','die','death','quit','ban','prohibit','enjoin','can\'t breath','choke','choking','cancer','liver','inflammation',
              'cirrhosis','hepatocirrhosis','hemoptysis','haemoptysis','vomit','vomiting','nausea','naupathia','stupid','fool','donkey',
              'hell','violence','fight','domestic violence','caught','police','sue','security','abuse','bustup','brawl','addictive','addicted']
    for n in negative:
        if n in tweet:
            score=score-1
    return score

#for each tweet, if any of words list is in the tweet content, the tweet is identified as related tweet
#use attritube() function to score the tweet
#if the score is negative, the tweet is identified negative, else positive
def matchTweet(tweet, words, result):
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
        score=attribute(text)
        loc = tweet['location']
        for l in result:
            if l == loc:
                if score >= 0:
                    result[l]['positive'] = result[l]['positive'] + 1
                else:
                    result[l]['negative'] = result[l]['negative'] + 1
                result[l]['rate']=round(result[l]['negative']/(result[l]['negative']+result[l]['positive']),4)
        return result

#this function is used for single tweet analysis
def smoke_Drink_per(tweet, result):
    words=get_words()
    matchTweet(tweet, words, result)
    return result
#write the final result into text file
def print_results(result):
    with open('output.txt', "w") as text_file:
        for each_result in result:
            print("City name: {} \n positive: {} \nnegative: {}.\nnegative-rate: {}.\n".format(
                each_result, result[each_result]['positive'],result[each_result]['negative'],result[each_result]['rate']),
                  file=text_file)
#this function is used for multi-tweet analysis, used a json file as resource
#the final result are wrote into text file using print_result() function
def smoke_Drink_file():
    a=0
    result=get_result()
    words = get_words()
    filesource = open('status1.json', 'r', encoding='utf-8')
    for i in filesource:
        try:
            tweet = json.loads(i)
            matchTweet(tweet, words, result)
        except:
            a=a
    for i in result:
        result[i]['rate']=round(result[i]['negative'] / (result[i]['negative'] + result[i]['positive']), 4)
    print(result)
    print_results(result)
    return result
