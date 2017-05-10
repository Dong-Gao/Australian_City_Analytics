import re
import json
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import twython

# Find and process Hashtags
hash_regex = re.compile(r"#(\w+)")
def hash_repl(match):
    return '__HASH_'+match.group(1).upper()

# Find and process Handels
hndl_regex = re.compile(r"@(\w+)")
def hndl_repl(match):
    return '__HNDL'#_'+match.group(1).upper()

# Find URLs
url_regex = re.compile(r"(http|https|ftp)://[a-zA-Z0-9\./]+")

# Find Repeating characters like happyyyyy
rpt_regex = re.compile(r"(.)\1{1,}(.)\2{1,}", re.IGNORECASE)
def rpt_repl(match):
    process = match.group(1) + match.group(1) + match.group(2)
    return process

# Build emoticon dictionary
emoticons = \
    [
        (' SMILE ', [':-)',':)','(:','(-:',';o)',':o)',':-3',':3',':->',':>','8-)','8)',':c)',':^)','=)']),
        (' LAUGH ', [':-D',':D', 'X-D', 'x-D', 'XD', 'xD', '=D', '8-D', '8D', '=3', 'B^D', ":'‑)", ":')"]),
        (' LOVE ', ['<3', ':\*', ]),
        (' GRIN ', [';-)', ';)', ';-D', ';D', '(;', '(-;','\*-)','\*)',';‑]',';]',';^)',':‑,']),
        (' FRUSTRATE ', [':o(','>:o(',':-(', ':(', '):', ')-:', ':c',':‑<','>:(']),
        (' CRY ', [':,(', ":'(", ':\"(', ':((']),
    ]

'''
emojis = \
    [
        (' SMILE ',['\\xF0\\x9F\\x98\\x81', '\\xF0\\x9F\\x98\\x82', '\\xF0\\x9F\\x98\\x83','\\xF0\\x9F\\x98\\x84', '\\xF0\\x9F\\x98\\x86', '\\xF0\\x9F\\x98\\x8A', '\\xF0\\x9F\\x98\\x8B','\\xF0\\x9F\\x98\\x8C', '\\xF0\\x9F\\x98\\x8D','\\xF0\\x9F\\x98\\x80','\\xF0\\x9F\\x98\\x87','\\xF0\\x9F\\x98\\x87','\\xF0\\x9F\\x98\\x9B','\\xF0\\x9F\\x98\\xB8','\\xF0\\x9F\\x98\\xB9','\\xF0\\x9F\\x98\\xBA', '\\xF0\\x9F\\x98\\x80','\\xF0\\x9F\\x98\\x87','\\xF0\\x9F\\x98\\x8E']),
        (' LAUGH', ['\\xF0\\x9F\\x98\\x9C', '\\xF0\\x9F\\x98\\x9D', '\\xF0\\x9F\\x98\\x9B']),
        (' LOVE ', ['\\xF0\\x9F\\x98\\x98', '\\xF0\\x9F\\x98\\x9A', '\\xF0\\x9F\\x98\\x97','\\xF0\\x9F\\x98\\x99', '\\xF0\\x9F\\x98\\xBB','\\xF0\\x9F\\x98\\xBD','\\xF0\\x9F\\x98\\x97','\\xF0\\x9F\\x98\\x99']),
        (' GRIN ', ['\\xF0\\x9F\\x98\\x89']),
        (' FRUSTRATE ', ['\\xF0\\x9F\\x98\\x94', '\\xF0\\x9F\\x98\\x96', '\\xF0\\x9F\\x98\\x9E', '\\xF0\\x9F\\x98\\xA0', '\\xF0\\x9F\\x98\\xA1', '\\xF0\\x9F\\x98\\xA3', '\\xF0\\x9F\\x98\\xA8', '\\xF0\\x9F\\x98\\xA9', '\\xF0\\x9F\\x98\\xAB','\\xF0\\x9F\\x98\\xB0', '\\xF0\\x9F\\x98\\x9F','\\xF0\\x9F\\x98\\xA7']),
        (' CRY ', ['\\xF0\\x9F\\x98\\xA2', '\\xF0\\x9F\\x98\\xAD', '\\xF0\\x9F\\x98\\xB9', '\\xF0\\x9F\\x98\\xBF']),
    ]
'''
#Build emoji dictionary
emojis = \
    [
        (' SMILE ',['😁', '😂', '😹', '😃','😄', '😆', '😊', '😋','😌', '😍','😀','😇','😛','😸','😹','😺','😎']),
        (' LAUGH', ['😜', '😝', '😛']),
        (' LOVE ', ['😘', '😚', '😗', '😙', '😻', '😽','😗','😙']),
        (' GRIN ', ['😉']),
        (' FRUSTRATE ', ['😔', '😖', '😞', '😠', '😡', '😣', '😨', '😩', '😫','😰', '😟','😧']),
        (' CRY ', ['😢', '😭', '😿']),
    ]

# Find punctuations, this part is achieved by vaderSentiment.
punctuations = \
    [
        ('__PUNC_EXCL',['!']),
        ('__PUNC_QUES',['?']),
        ('__PUNC_ELLP',['...']),
    ]

#For emoticon regex
def escape_paren(arr):
    return [text.replace(')', '[)}\]]').replace('(', '[({\[]') for text in arr]

def regex_union(arr):
    return '(' + '|'.join(arr) + ')'

emoticons_regex = [(repl, re.compile(regex_union(escape_paren(regx)))) for (repl, regx) in emoticons]


#For emoji regex
emojis_regex = [(repl, re.compile(regex_union(regx))) for (repl, regx) in emojis]


def process_hashtags(text):
    return re.sub(hash_regex, hash_repl, text)

def process_handles(text):
    return re.sub(hndl_regex, hndl_repl, text)

def process_urls(text):
    return re.sub(url_regex, '', text)

def process_emoticons(text):
    for (repl, regx) in emoticons_regex :
        text = re.sub(regx, ' '+repl+' ', text)
    return text

def process_emojis(text):
    for (repl, regx) in emojis_regex :
        text = re.sub(regx, ' '+repl+' ', text)
    return text

def process_repeatings(text):
    return re.sub(rpt_regex, rpt_repl, text)

#This function can count the number of query occured in a tweet.
def process_query_term(text, query):
    query_regex = "|".join([ re.escape(q) for q in query])
    return re.sub(query_regex, '__QUER', text, flags=re.IGNORECASE)

def count_handles(text):
    return len(re.findall(hndl_regex, text))
def count_hashtags(text):
    return len(re.findall(hash_regex, text))
def count_urls(text):
    return len(re.findall(url_regex, text))
def count_emoticons(text):
    count = 0
    for (repl, regx) in emoticons_regex :
        count += len(re.findall(regx, text))
    return count
def count_emojis(text):
    count = 0
    for (repl, regx) in emojis_regex :
        count += len(re.findall(regx, text))
    return count

def emotion_list():
    emotion_score={'Melbourne':{'0-6':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0}},
          'Sydney':{'0-6':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0}},
          'Perth':{'0-6':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0}},
          'Darwin':{'0-6':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0}},
          'Canberra':{'0-6':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0}},
          'Hobart':{'0-6':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0}},
          'Adelaide':{'0-6':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0}},
          'Brisbane':{'0-6':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0}}}
    return emotion_score

#This function is used to pre-process tweet and return its sentiment value.
def sentiment_score(analyzer, tweet_text):
    tweet_text = process_urls(tweet_text)
    tweet_text = process_emoticons(tweet_text)
    tweet_text = process_emojis(tweet_text)
    tweet_text = tweet_text.replace('\'', '')
    tweet_text = process_repeatings(tweet_text)
    score = analyzer.polarity_scores(tweet_text)
    return score

#This function is used to calculate statictisc of a tweet, and return a dictionary.
def sentiment_statistic(analyzer, tweet_text, sentiment_list):
    #score = sentiment_score(analyzer, tweet_text['text'].encode('utf-8').decode('unicode_escape'))
    score = sentiment_score(analyzer, tweet_text['text'])
    city = tweet_text['location']
    if 0 <= tweet_text['time'] < 6:
        sentiment_list[city]['0-6']['total'] += score['compound']
        sentiment_list[city]['0-6']['amount'] += 1
        if score['compound'] > 0:
            sentiment_list[city]['0-6']['positive'] += 1
        elif score['compound'] < 0:
            sentiment_list[city]['0-6']['negative'] += 1
        else:
            sentiment_list[city]['0-6']['neutral'] += 1
    elif 6 <= tweet_text['time'] < 12:
        sentiment_list[city]['6-12']['total'] += score['compound']
        sentiment_list[city]['6-12']['amount'] += 1
        if score['compound'] > 0:
            sentiment_list[city]['6-12']['positive'] += 1
        elif score['compound'] < 0:
            sentiment_list[city]['6-12']['negative'] += 1
        else:
            sentiment_list[city]['6-12']['neutral'] += 1
    elif 12 <= tweet_text['time'] < 18:
        sentiment_list[city]['12-18']['total'] += score['compound']
        sentiment_list[city]['12-18']['amount'] += 1
        if score['compound'] > 0:
            sentiment_list[city]['12-18']['positive'] += 1
        elif score['compound'] < 0:
            sentiment_list[city]['12-18']['negative'] += 1
        else:
            sentiment_list[city]['12-18']['neutral'] += 1
    elif 18 <= tweet_text['time'] < 24:
        sentiment_list[city]['18-24']['total'] += score['compound']
        sentiment_list[city]['18-24']['amount'] += 1
        if score['compound'] > 0:
            sentiment_list[city]['18-24']['positive'] += 1
        elif score['compound'] < 0:
            sentiment_list[city]['18-24']['negative'] += 1
        else:
            sentiment_list[city]['18-24']['neutral'] += 1
    return sentiment_list

#This function is used to process each tweet has been stored in the couchdb, and update the statistics each time.
def sentiment_analy(analyzer, tweet, emotionResult):
    emotion_data = {'Melbourne':{'0-6':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0}},
          'Sydney':{'0-6':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0}},
          'Perth':{'0-6':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0}},
          'Darwin':{'0-6':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0}},
          'Canberra':{'0-6':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0}},
          'Hobart':{'0-6':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0}},
          'Adelaide':{'0-6':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0}},
          'Brisbane':{'0-6':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0, 'amount':0, 'positive':0, 'negative':0, 'neutral':0}}}
    try:
        tweet['location']
    except:
        return
    if tweet['location'] == '':
        return
    emotion_data = sentiment_statistic(analyzer, tweet, emotion_data)
    for i in emotionResult:
        if i == '_id' or i =='_rev':
            continue
        #Statistics of tweets from 0am to 6am
        emotionResult[i]['0-6']['total'] += emotion_data[i]['0-6']['total']
        emotionResult[i]['0-6']['amount'] += emotion_data[i]['0-6']['amount']
        emotionResult[i]['0-6']['positive'] += emotion_data[i]['0-6']['positive']
        emotionResult[i]['0-6']['negative'] += emotion_data[i]['0-6']['negative']
        emotionResult[i]['0-6']['neutral'] += emotion_data[i]['0-6']['neutral']
        if emotionResult[i]['0-6']['amount'] == 0:
            emotionResult[i]['0-6']['score'] = 'N/A'
        else:
            emotionResult[i]['0-6']['score'] = emotionResult[i]['0-6']['total'] / emotionResult[i]['0-6']['amount']
        # Statistics of tweets from 6am to 12pm
        emotionResult[i]['6-12']['total'] += emotion_data[i]['6-12']['total']
        emotionResult[i]['6-12']['amount'] += emotion_data[i]['6-12']['amount']
        emotionResult[i]['6-12']['positive'] += emotion_data[i]['6-12']['positive']
        emotionResult[i]['6-12']['negative'] += emotion_data[i]['6-12']['negative']
        emotionResult[i]['6-12']['neutral'] += emotion_data[i]['6-12']['neutral']
        if emotionResult[i]['6-12']['amount'] == 0:
            emotionResult[i]['6-12']['score'] = 'N/A'
        else:
            emotionResult[i]['6-12']['score'] = emotionResult[i]['6-12']['total'] / emotionResult[i]['6-12']['amount']
        # Statistics of tweets from 12pm to 6pm
        emotionResult[i]['12-18']['total'] += emotion_data[i]['12-18']['total']
        emotionResult[i]['12-18']['amount'] += emotion_data[i]['12-18']['amount']
        emotionResult[i]['12-18']['positive'] += emotion_data[i]['12-18']['positive']
        emotionResult[i]['12-18']['negative'] += emotion_data[i]['12-18']['negative']
        emotionResult[i]['12-18']['neutral'] += emotion_data[i]['12-18']['neutral']
        if emotionResult[i]['12-18']['amount'] == 0:
            emotionResult[i]['12-18']['score'] = 'N/A'
        else:
            emotionResult[i]['12-18']['score'] = emotionResult[i]['12-18']['total'] / emotionResult[i]['12-18'][
                'amount']
        # Statistics of tweets from 6pm to 12am
        emotionResult[i]['18-24']['total'] += emotion_data[i]['18-24']['total']
        emotionResult[i]['18-24']['amount'] += emotion_data[i]['18-24']['amount']
        emotionResult[i]['18-24']['positive'] += emotion_data[i]['18-24']['positive']
        emotionResult[i]['18-24']['negative'] += emotion_data[i]['18-24']['negative']
        emotionResult[i]['18-24']['neutral'] += emotion_data[i]['18-24']['neutral']
        if emotionResult[i]['18-24']['amount'] == 0:
            emotionResult[i]['18-24']['score'] = 'N/A'
        else:
            emotionResult[i]['18-24']['score'] = emotionResult[i]['18-24']['total'] / emotionResult[i]['18-24'][
                'amount']
    return emotionResult

#This function is used for multi-tweet analysis, used a json file as the input, and return the statistics as the output.
def sentiment_all(emotionResult):
    emotion_data = emotion_list()
    filesource = open('status.json', 'r', encoding='utf-8')
    analyzer = SentimentIntensityAnalyzer()
    count = 0
    for line in filesource:
        tweet = json.loads(line)
        count += 1
        if count % 100000 == 0:
            print(emotion_data)
        try:
            tweet['location']
        except:
            #print(tweet)
            continue
        if tweet['location'] == '':
            continue
        sentiment_statistic(analyzer, tweet, emotion_data)
    for i in emotionResult:
        emotionResult[i]['0-6'] = emotion_data[i]['0-6']['total'] / emotion_data[i]['0-6']['amount']
        emotionResult[i]['6-12'] = emotion_data[i]['6-12']['total'] / emotion_data[i]['6-12']['amount']
        emotionResult[i]['12-18'] = emotion_data[i]['12-18']['total'] / emotion_data[i]['12-18']['amount']
        emotionResult[i]['18-24'] = emotion_data[i]['18-24']['total'] / emotion_data[i]['18-24']['amount']
        print(i)
        print(emotion_data[i])
    amount = 0
    for i in emotion_data:
        amount += emotion_data[i]['0-6']['amount'] + emotion_data[i]['6-12']['amount']+emotion_data[i]['12-18']['amount']+emotion_data[i]['18-24']['amount']
    print("Total tweets:", amount)
    return emotionResult
