# The default encoding format is utf-8.
import re

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

# Repeating words like hurrrryyyyyy
rpt_regex = re.compile(r"(.)\1{1,}", re.IGNORECASE)
def rpt_repl(match):
    return match.group(1)+match.group(1)

# Emoticons
emoticons = \
    [
        ('__EMOT_SMILEY', [':-)',':)','(:','(-:',';o)',':o)',':-3',':3',':->',':>','8-)','8)',':c)',':^)','=)']),
        ('__EMOT_LAUGH', [':-D',':D', 'X-D', 'x-D', 'XD', 'xD', '=D', '8-D', '8D', '=3', 'B^D', ":'‑)", ":')"]),
        ('__EMOT_LOVE', ['<3', ':\*', ]),
        ('__EMOT_WINK', [';-)', ';)', ';-D', ';D', '(;', '(-;','\*-)','\*)',';‑]',';]',';^)',':‑,']),
        ('__EMOT_FROWN', [':o(','>:o(',':-(', ':(', '):', ')-:', ':c',':‑<','>:(']),
        ('__EMOT_CRY', [':,(', ":'(", ':\"(', ':((']),
    ]


emojis = \
    [
        ('__EMOJI_SMILEY',['\\xF0\\x9F\\x98\\x81', '\\xF0\\x9F\\x98\\x82', '\\xF0\\x9F\\x98\\x83','\\xF0\\x9F\\x98\\x84', '\\xF0\\x9F\\x98\\x86', '\\xF0\\x9F\\x98\\x8A', '\\xF0\\x9F\\x98\\x8B','\\xF0\\x9F\\x98\\x8C', '\\xF0\\x9F\\x98\\x8D','\\xF0\\x9F\\x98\\x80','\\xF0\\x9F\\x98\\x87','\\xF0\\x9F\\x98\\x87','\\xF0\\x9F\\x98\\x9B','\\xF0\\x9F\\x98\\xB8','\\xF0\\x9F\\x98\\xB9','\\xF0\\x9F\\x98\\xBA', '\\xF0\\x9F\\x98\\x80','\\xF0\\x9F\\x98\\x87','\\xF0\\x9F\\x98\\x8E']),
        ('__EMOJI_LAUGH', ['\\xF0\\x9F\\x98\\x9C', '\\xF0\\x9F\\x98\\x9D', '\\xF0\\x9F\\x98\\x9B']),
        ('__EMOJI_LOVE', ['\\xF0\\x9F\\x98\\x98', '\\xF0\\x9F\\x98\\x9A', '\\xF0\\x9F\\x98\\x97','\\xF0\\x9F\\x98\\x99', '\\xF0\\x9F\\x98\\xBB','\\xF0\\x9F\\x98\\xBD','\\xF0\\x9F\\x98\\x97','\\xF0\\x9F\\x98\\x99']),
        ('__EMOJI_WINK', ['\\xF0\\x9F\\x98\\x89']),
        ('__EMOJI_FROWN', ['\\xF0\\x9F\\x98\\x94', '\\xF0\\x9F\\x98\\x96', '\\xF0\\x9F\\x98\\x9E', '\\xF0\\x9F\\x98\\xA0', '\\xF0\\x9F\\x98\\xA1', '\\xF0\\x9F\\x98\\xA3', '\\xF0\\x9F\\x98\\xA8', '\\xF0\\x9F\\x98\\xA9', '\\xF0\\x9F\\x98\\xAB','\\xF0\\x9F\\x98\\xB0', '\\xF0\\x9F\\x98\\x9F','\\xF0\\x9F\\x98\\xA7']),
        ('__EMOJI_CRY', ['\\xF0\\x9F\\x98\\xA2', '\\xF0\\x9F\\x98\\xAD', '\\xF0\\x9F\\x98\\xB9', '\\xF0\\x9F\\x98\\xBF']),
    ]


# Punctuations
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

def processHashtags(text):
    return re.sub(hash_regex, hash_repl, text)

def processHandles(text):
    return re.sub(hndl_regex, hndl_repl, text )

def processUrls(text):
    return re.sub(url_regex, ' __URL ', text )

def processEmoticons(text):
    for (repl, regx) in emoticons_regex :
        text = re.sub(regx, ' '+repl+' ', text)
    return text

def processEmojis(text):
    for (repl, regx) in emojis_regex :
        text = re.sub(regx, ' '+repl+' ', text)
    return text

def processPunctuations(text):
    return re.sub( word_bound_regex , punctuations_repl, text )

def processRepeatings(text):
    return re.sub( rpt_regex, rpt_repl, text )

def processQueryTerm(text, query):
    query_regex = "|".join([ re.escape(q) for q in query])
    return re.sub( query_regex, '__QUER', text, flags=re.IGNORECASE )

def countHandles(text):
    return len(re.findall(hndl_regex, text) )
def countHashtags(text):
    return len(re.findall(hash_regex, text) )
def countUrls(text):
    return len(re.findall(url_regex, text) )
def countEmoticons(text):
    count = 0
    for (repl, regx) in emoticons_regex :
        count += len(re.findall(regx, text) )
    return count

def countEmojis(text):
    count = 0
    for (repl, regx) in emojis_regex :
        count += len(re.findall(regx, text) )
    return count

def processAll(text):
    text = re.sub( hash_regex, hash_repl, text )
    text = re.sub( hndl_regex, hndl_repl, text )
    text = re.sub( url_regex, ' __URL ', text )

    for (repl, regx) in emoticons_regex :
        text = re.sub(regx, ' '+repl+' ', text)
    for (repl, regx) in emojis_regex :
        text = re.sub(regx, ' ' + repl + ' ', text)

    text = text.replace('\'','')
    text = re.sub( word_bound_regex , punctuations_repl, text )
    text = re.sub( rpt_regex, rpt_repl, text )

    return text

twitter = ["I am happy! #Today! @helloworld, :), \xF0\x9F\x98\x81","I am not happy.","Today is :)."]

a = processAll(twitter[0])
print(a)