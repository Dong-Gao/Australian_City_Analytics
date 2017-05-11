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

def read_result():
    result = {'Darwin': {'match': 0, 'total': 0}, 'Adelaide': {'match': 0, 'total': 0},
                  'Brisbane': {'match': 0, 'total': 0}, 'Perth': {'match': 0, 'total': 0},
                  'Canberra': {'match': 0, 'total': 0}, 'Melbourne': {'match': 0, 'total': 0},
                  'Sydney': {'match': 0, 'total': 0}, 'Hobart': {'match': 0, 'total': 0}}
    return result


#this function read a text file of keywords, and return a list of key word
def read_keywords():
    keywords_list=[]
    with open('keywords.txt') as keywords_file:
        for each_keyword in keywords_file:
            keywords_list.append(each_keyword.rstrip('\n'))
    return keywords_list

#this function write the final result into text file
def print_results(result):
    with open('output.txt', "w") as text_file:
        for each_result in result:
            print("City name: {} \n match: {} \ntotal: {}.\n".format(
                each_result, result[each_result]['match'],result[each_result]['total']),
                  file=text_file)

#for each tweet, add 1 to total amount,
#if any of the keyword list is in the tweet content,
#the tweet is identified as related tweet. And 1 is added
#to the amount of related tweets.
def tweet_culture(tweet, words, result):
    count=0
    text=tweet['text']
    loc = tweet['location']
    result[loc]['total']= 1 + result[loc]['total']
    for w in words:
        if w in text:
            count=count+1
    if count>0:
        for l in result:
            if l==loc:
                result[l]['match']= 1 + result[l]['match']
    return result

#this function is used for analyzing single tweet
def culture_per(tweet,result):
    keywords=read_keywords()
    tweet_culture(tweet,keywords,result)
    return result
# this function is used for analyzing multi-tweet,
#and write the final result into text file
def culture_file():
    a=0
    result=read_result()
    words=read_keywords()
    filesource = open('status1.json', 'r', encoding='utf-8')
    for i in filesource:
        try:

            tweet = json.loads(i)
            tweet_culture(tweet, words, result)
        except:
            a=a
    print(result)
    print_results(result)
culture_file()
