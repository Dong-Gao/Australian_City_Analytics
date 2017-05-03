import json
import time

def read_result():
    result = [['darwin', 0, 0], ['adelaide', 0, 0], ['bribane', 0, 0], ['perth', 0, 0], ['canberra', 0, 0],
            ['melbourne', 0, 0], ['sydney', 0, 0], ['adelaide', 0, 0]]
    return result

def read_keywords():
    keywords_list=[]
    with open('keywords.txt') as keywords_file:
        for each_keyword in keywords_file:
            keywords_list.append(each_keyword.rstrip('\n'))
    return keywords_list


def read_file(keywords_list,result):
    filesource = open('status1.json', 'r', encoding='utf-8')
    for i in filesource:
        tweet = json.loads(i)
        classify(keywords_list,tweet,result)

def tweet_culture(keywords_list,tweet,result):
    classify(keywords_list,tweet,result)

def classify(keywords_list,each_tweet,result):
    a=0
    try:
        if each_tweet['location'] == 'Darwin':
            if_contain_keywords(keywords_list,each_tweet["text"], result[0])
        elif each_tweet['location'] == 'Adelaide':
            if_contain_keywords(keywords_list,each_tweet["text"], result[1])
        elif each_tweet['location'] == 'Brisbane':
            if_contain_keywords(keywords_list,each_tweet["text"], result[2])
        elif each_tweet['location'] == 'Perth':
            if_contain_keywords(keywords_list,each_tweet["text"], result[3])
        elif each_tweet['location'] == 'Canberra':
            if_contain_keywords(keywords_list,each_tweet["text"], result[4])
        elif each_tweet['location'] == 'Melbourne':
            if_contain_keywords(keywords_list,each_tweet["text"], result[5])
        elif each_tweet['location'] == 'Sydney':
            if_contain_keywords(keywords_list,each_tweet["text"], result[6])
        elif each_tweet['location'] == 'Hobart':
            if_contain_keywords(keywords_list,each_tweet["text"], result[7])
    except:
        a=a


def if_contain_keywords(keywords_list,tweet_text, result_list):
    result_list[2] = result_list[2] + 1
    for word in keywords_list:
        if word in tweet_text:
            result_list[1] = result_list[1] + 1;
            break
    return result_list


def print_results(result):
    with open('jeff.txt', "w") as text_file:
        for each_result in result:
            if each_result[2] ==0:
                rate =0
            else:
                rate = each_result[1]/ each_result[2]
            rate=round(rate,8)
            print("City name: {}. Rate of tweets: {} \nNumber of tweets contains keywords: {}.\nNumber of total tweets: {}\n".format(
                each_result[0], rate,each_result[1], each_result[2]),
                  file=text_file)

def culture_per(tweet,result):
    keywords_list=read_keywords()
    tweet_culture(keywords_list, tweet, result)
def culture_main(result):
    t1=time.process_time()
    words=read_keywords()
    read_file(words,result)
    print(result)
    t2=time.process_time()
    print(t2-t1)
    print_results(result)
