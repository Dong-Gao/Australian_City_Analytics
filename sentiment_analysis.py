#The input is a tweet and dictionary, and the output is a dictionary.
import re
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Hashtags
hash_regex = re.compile(r"#(\w+)")
def hash_repl(match):
    return '__HASH_'+match.group(1).upper()

# Handels
hndl_regex = re.compile(r"@(\w+)")
def hndl_repl(match):
    return '__HNDL'#_'+match.group(1).upper()

# URLs
url_regex = re.compile(r"(http|https|ftp)://[a-zA-Z0-9\./]+")

# Spliting by word boundaries
word_bound_regex = re.compile(r"\W+")

# Repeating words like happyyyyy
rpt_regex = re.compile(r"(.)\1{1,}", re.IGNORECASE)
def rpt_repl(match):
    return match.group(1)+match.group(1)

# Emoticons
emoticons = \
    [
        ('SMILE', [':-)',':)','(:','(-:',';o)',':o)',':-3',':3',':->',':>','8-)','8)',':c)',':^)','=)']),
        ('LAUGH', [':-D',':D', 'X-D', 'x-D', 'XD', 'xD', '=D', '8-D', '8D', '=3', 'B^D', ":'‑)", ":')"]),
        ('LOVE', ['<3', ':\*', ]),
        ('GRIN', [';-)', ';)', ';-D', ';D', '(;', '(-;','\*-)','\*)',';‑]',';]',';^)',':‑,']),
        ('FRUSTRATE', [':o(','>:o(',':-(', ':(', '):', ')-:', ':c',':‑<','>:(']),
        ('CRY', [':,(', ":'(", ':\"(', ':((']),
    ]


emojis = \
    [
        ('SMILE',['\\xF0\\x9F\\x98\\x81', '\\xF0\\x9F\\x98\\x82', '\\xF0\\x9F\\x98\\x83','\\xF0\\x9F\\x98\\x84', '\\xF0\\x9F\\x98\\x86', '\\xF0\\x9F\\x98\\x8A', '\\xF0\\x9F\\x98\\x8B','\\xF0\\x9F\\x98\\x8C', '\\xF0\\x9F\\x98\\x8D','\\xF0\\x9F\\x98\\x80','\\xF0\\x9F\\x98\\x87','\\xF0\\x9F\\x98\\x87','\\xF0\\x9F\\x98\\x9B','\\xF0\\x9F\\x98\\xB8','\\xF0\\x9F\\x98\\xB9','\\xF0\\x9F\\x98\\xBA', '\\xF0\\x9F\\x98\\x80','\\xF0\\x9F\\x98\\x87','\\xF0\\x9F\\x98\\x8E']),
        ('LAUGH', ['\\xF0\\x9F\\x98\\x9C', '\\xF0\\x9F\\x98\\x9D', '\\xF0\\x9F\\x98\\x9B']),
        ('LOVE', ['\\xF0\\x9F\\x98\\x98', '\\xF0\\x9F\\x98\\x9A', '\\xF0\\x9F\\x98\\x97','\\xF0\\x9F\\x98\\x99', '\\xF0\\x9F\\x98\\xBB','\\xF0\\x9F\\x98\\xBD','\\xF0\\x9F\\x98\\x97','\\xF0\\x9F\\x98\\x99']),
        ('GRIN', ['\\xF0\\x9F\\x98\\x89']),
        ('FRUSTRATE', ['\\xF0\\x9F\\x98\\x94', '\\xF0\\x9F\\x98\\x96', '\\xF0\\x9F\\x98\\x9E', '\\xF0\\x9F\\x98\\xA0', '\\xF0\\x9F\\x98\\xA1', '\\xF0\\x9F\\x98\\xA3', '\\xF0\\x9F\\x98\\xA8', '\\xF0\\x9F\\x98\\xA9', '\\xF0\\x9F\\x98\\xAB','\\xF0\\x9F\\x98\\xB0', '\\xF0\\x9F\\x98\\x9F','\\xF0\\x9F\\x98\\xA7']),
        ('CRY', ['\\xF0\\x9F\\x98\\xA2', '\\xF0\\x9F\\x98\\xAD', '\\xF0\\x9F\\x98\\xB9', '\\xF0\\x9F\\x98\\xBF']),
    ]


# Punctuations, this part is already achieved by nltk.
punctuations = \
    [
        ('__PUNC_EXCL',['!']),
        ('__PUNC_QUES',['?']),
        ('__PUNC_ELLP',['...', '…', ]),
    ]

#Printing functions for info
def print_config(cfg):
    for (x, arr) in cfg:
        print(x, '\t', end='')
        for a in arr:
            print(a, '\t', end='')
        print('')

def print_emoticons():
    print_config(emoticons)

def print_punctuations():
    print_config(punctuations)

#For emoticon regexes
def escape_paren(arr):
    return [text.replace(')', '[)}\]]').replace('(', '[({\[]') for text in arr]

def regex_union(arr):
    return '(' + '|'.join(arr) + ')'

emoticons_regex = [(repl, re.compile(regex_union(escape_paren(regx)))) for (repl, regx) in emoticons]



#For emoji regexes
emojis_regex = [(repl, re.compile(regex_union(regx))) for (repl, regx) in emojis]


#For punctuation replacement
def punctuations_repl(match):
    text = match.group(0)
    repl = []
    for (key, parr) in punctuations :
        for punc in parr :
            if punc in text:
                repl.append(key)
    if len(repl) > 0 :
        return ' '+' '.join(repl)+' '
    else :
        return ' '

def process_hashtags(text):
    return re.sub(hash_regex, hash_repl, text)

def process_handles(text):
    return re.sub(hndl_regex, hndl_repl, text )

def process_urls(text):
    return re.sub(url_regex, '', text )

def process_emoticons(text):
    for (repl, regx) in emoticons_regex :
        text = re.sub(regx, ' '+repl+' ', text)
    return text

def process_emojis(text):
    for (repl, regx) in emojis_regex :
        text = re.sub(regx, ' '+repl+' ', text)
    return text

def process_punctuations(text):
    return re.sub( word_bound_regex , punctuations_repl, text )

def process_repeatings(text):
    return re.sub(rpt_regex, rpt_repl, text)[:-1]

#This function can count the number of query occured in a tweet.
def process_query_term(text, query):
    query_regex = "|".join([ re.escape(q) for q in query])
    return re.sub(query_regex, '__QUER', text, flags=re.IGNORECASE )

def count_handles(text):
    return len(re.findall(hndl_regex, text) )
def count_hashtags(text):
    return len(re.findall(hash_regex, text) )
def count_urls(text):
    return len(re.findall(url_regex, text) )
def count_emoticons(text):
    count = 0
    for (repl, regx) in emoticons_regex :
        count += len(re.findall(regx, text) )
    return count
def count_emojis(text):
    count = 0
    for (repl, regx) in emojis_regex :
        count += len(re.findall(regx, text) )
    return count

def sentiment_analysis(tweet_text, sentiment_list):
    tweet_text = process_urls(tweet_text)
    tweet_text = process_emoticons(tweet_text)
    tweet_text = process_emojis(tweet_text)
    tweet_text = tweet_text.replace('\'','')
    tweet_text = process_repeatings(tweet_text)
    score = SentimentIntensityAnalyzer().polarity_scores(tweet_text)
    if score['compound'] == 0:
        sentiment_list['neutral'] += 1
    elif score['compound'] > 0:
        sentiment_list['positive'] += 1
        sentiment_list['postive_count'] += score['compound']
    else:
        sentiment_list['negative'] += 1
        sentiment_list['negative_count'] += score['compound']
    return sentiment_list

#The below part is used to test!
tweets = ["I am happy! #Today! @helloworld, :)", "\xF0\x9F\x98\x81","I am not happy.","Today is :).", "I am really >:o(."]


for tweet_text in tweets:
    tweet_text = process_urls(tweet_text)
    tweet_text = process_emoticons(tweet_text)
    tweet_text = process_emojis(tweet_text)
    tweet_text = tweet_text.replace('\'','')
    tweet_text = process_repeatings(tweet_text)
    score = SentimentIntensityAnalyzer().polarity_scores(tweet_text)
    print(score)