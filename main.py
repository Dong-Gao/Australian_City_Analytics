# Cluster and Cloud Computing
# Group Project
# Team 16
#
# Kaile Wei: 812381
# Nanjiang Li: 741524
# Hongzhen Xie: 773383
# Dong Gao: 795622
# Chuang Ying: 844566

import couchdb
import json
import queue
import sys
import time
import tweepy
import scenario3_alcoholTobacco.smoke_drink
import scenario1_sentimentSeries.sentiment_analysis
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import scenario2_culturalIntegration.culture as Culture
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy.streaming import StreamListener

analyzer = SentimentIntensityAnalyzer()

couchIP = 'sourcead:iamfine@115.146.93.79' # IP of master couchdb
#couchIP = 'localhost'
threadRank = 1
threadCount = 4
dbName = 'twitter'
dbNameSource = 'source'
dbNameResult = 'result'
docNameSource = 'sourcelist'
docNameSmokeResult = 'smokeResult'
docNameEmotionResult = 'emotionResult'
docNameCulture = 'culture'

accounts = [] # for fetching status
accountPos = 0 # current account fetching
unfetchedUserQueueCapacity = 100
peopleMaxCount = 25000 # Max amount of people fetching
statusMaxCount = 200 # Max amount of statuses of one person
friendMaxCount = 20 # Max amount of friends of one person to be added to queue
databasetime = 0 # for timing
tweettime = 0

# initialize the queue
unfetchedUser = queue.Queue(maxsize = unfetchedUserQueueCapacity)

# for scenario
smokeResult = {'_id' : docNameSmokeResult,
    'Melbourne': {'positive': 0, 'negative': 0, 'rate': 0,'female_rate':0.4937},
    'Sydney': {'positive': 0, 'negative': 0, 'rate': 0,'female_rate':0.4941},
    'Perth': {'positive': 0, 'negative': 0, 'rate': 0,'female_rate':0.4851},
    'Darwin': {'positive': 0, 'negative': 0, 'rate': 0,'female_rate':0.4533},
    'Canberra': {'positive': 0, 'negative': 0, 'rate': 0,'female_rate':0.4926},
    'Hobart': {'positive': 0, 'negative': 0, 'rate': 0,'female_rate':0.4834},
    'Adelaide': {'positive': 0, 'negative': 0, 'rate': 0,'female_rate':0.4908},
    'Brisbane': {'positive': 0, 'negative': 0, 'rate': 0,'female_rate':0.4944}}
emotionResult = {'_id' : docNameEmotionResult,
    'Melbourne':{'0-6':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0}},
    'Sydney':{'0-6':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0}},
    'Perth':{'0-6':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0}},
    'Darwin':{'0-6':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0}},
    'Canberra':{'0-6':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0}},
    'Hobart':{'0-6':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0}},
    'Adelaide':{'0-6':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0}},
    'Brisbane':{'0-6':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'6-12':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'12-18':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0},'18-24':{'total':0,'amount':0,'score':0,'positive':0, 'negative':0, 'neutral':0}}}
culture = {'_id' : docNameCulture,
    'Darwin': {'match': 0, 'total': 0}, 'Adelaide': {'match': 0, 'total': 0},
    'Brisbane': {'match': 0, 'total': 0}, 'Perth': {'match': 0, 'total': 0},
    'Canberra': {'match': 0, 'total': 0}, 'Melbourne': {'match': 0, 'total': 0},
    'Sydney': {'match': 0, 'total': 0},'Hobart': {'match': 0, 'total': 0}}

# account setting
# yingchuang
accounts.append({
'consumer_key' : '4eEm0v4afh2MH9juRASmR3xd0',
'consumer_secret' : 'ek5x4au3LBo25iBcwKf9lzJMViz1KCoYApbPIYstHZgWJHHFHY',
'access_token' : '853442542074908672-A3pnyKH3xVGC65s5lvtZnIPMymGL4kb',
'access_secret' : 'UgORHfIhuvCYAH11nwejwupfN92Lu9GKpyBbSc6HAOttT'})

accounts.append({
'consumer_key' : 'Ahm52ivjZ9aLxdF8mGGhhKhKU',
'consumer_secret' : 'eyGbe8yBHendsSOxyoZ99Z0ohMl1NDuJtUG3rL39Ic3V50hkFF',
'access_token' : '853442542074908672-7t6ztvCOsHqClazlbxFKe2p1YTFIfAB',
'access_secret' : '50FpJK7S5Cdabmm6kQr0ikWWe3FY83y3sRZrB8tX265XO'})

accounts.append({
'consumer_key' : '0QblwtahftHzpUY6JNBKJlYxH',
'consumer_secret' : 'mC7ZnBBKSNipAlmwQ2johuhugx0m3wZCnO2yChjZxxkLn7oDUQ',
'access_token' : '853442542074908672-glcGvuSrkTZmkoppCnbjd9ULLFjourF',
'access_secret' : 'JheGGn1NTR2JwDNVc2lKW64cNfsGOOvAqJ63aU458SVBk'})

accounts.append({
'consumer_key' : 'xe9mVovHE49pll0BedCxckxoj',
'consumer_secret' : 'Buy7Y5eBjbypLveoqEXEj9exCpDspWUCI9hag9Z8Iigd7YAsOJ',
'access_token' : '853442542074908672-BOEyHjWAQFu2IuvJKOGy22qdK32o4Q1',
'access_secret' : 'rufPkPAeJXf1p1xuCSowZGspLFU0AMoQ45q4CyjXWz6PF'})

accounts.append({
'consumer_key' : 'NhmAGuRvOhen2EXoReEvFPhn9',
'consumer_secret' : 'q2ZrUQrdInVAHKr2ClVBqv3RfCIB2jO4A2HLm5QifwYmIcoXEu',
'access_token' : '853442542074908672-nAf6QrTJjHasdmXqtghe7FoIz54dRCk',
'access_secret' : 'DGckFXikMtxjmGM16pGCp2pgXGvz7O6hDw0Fe7fRzglXA'})

# arthur
accounts.append({
'consumer_key' : '7NW9RyZLWnXE7jbbgC7Q5ErJw',
'consumer_secret' : 'Vmkp7ZrAVTVob0Cxr2lGMFokjNKvKLTWQtrVbWmf8FaP9E48Jx',
'access_token' : '4444601909-kdjeiUNVq4eIFpkXUGuRPJUAoQImceVIcPzBAgK',
'access_secret' : 'A7lOd2DZ38SnpUcXNQvd8QT7m16B0Ckm8xuyw55qFrIO9'})

accounts.append({
'consumer_key' : 'e4Fv8KAwQ5L5A5NZxqMANJuuz',
'consumer_secret' : 'b3kQg69dKxVcpYMaeaSvkQSaWxLZoFsIp4cQnzU033daWCAUgt',
'access_token' : '854235761587048449-467HV6EMSqsuHbSmrvRICZHoMPuTJUT',
'access_secret' : 'UzX374xOJJBD10Rzm5nBqXw949f4eGUDEt6V7fKRbGdpZ'})

accounts.append({
'consumer_key' : 'dQtpEQrxmlfRiQczGwG8nXMbp',
'consumer_secret' : 'RGNlbrkPRzFA9XQB3tCKtDbUeAh3tGOTkdXKq17pjTzXjVEqDa',
'access_token' : '4444601909-rEsfeP8bDq7aKWyeJP4GWuk3HiQXwCdzKudLG3s',
'access_secret' : 'QPYnCZejVtbPP3bGBibNZzeaOOSsXloiIeP2Qo4DKOJWH'})

accounts.append({
'consumer_key' : 'bcypBvJdToHd3tN1LieuDfPJu',
'consumer_secret' : 'rogOKksgJU46NeXB5Cdmy40TJBZyVZkVtFxkkTZyXPBosvkjSd',
'access_token' : '4444601909-peSS6eUsgXxNUDdZxm1HQ0Reg9OnqQyqiGIazhV',
'access_secret' : '4KNmPFXSO0tM10FFDiRmJ0ZXecRGND2hKuROd0A25ba4K'})

accounts.append({
'consumer_key' : '7xdxfkr5gEKSsmF0DX6hRYL16',
'consumer_secret' : 'Gxrl8LH8bgKhroexnYQvpD4ZqHJhBT6TZHIDaj9H4jViz4vwIi',
'access_token' : '4444601909-0VwZQd6nFZuPpbThO71EwHm9eHSmnlH0RvLLksg',
'access_secret' : 'NtHCGjj7AXJDSPEfIZsYrtjvByCf7ogvpm9zqNUbaZbJL'})

accounts.append({
'consumer_key' : '7NW9RyZLWnXE7jbbgC7Q5ErJw',
'consumer_secret' : 'Vmkp7ZrAVTVob0Cxr2lGMFokjNKvKLTWQtrVbWmf8FaP9E48Jx',
'access_token' : '4444601909-kdjeiUNVq4eIFpkXUGuRPJUAoQImceVIcPzBAgK',
'access_secret' : 'A7lOd2DZ38SnpUcXNQvd8QT7m16B0Ckm8xuyw55qFrIO9'})

accounts.append({
'consumer_key' : 'rEC4hwWzesBL4RWbFzxrhFakG',
'consumer_secret' : 'nXCP3qKW9D1DmHjqvk4hovDXA5oyH6uy7yP3M24LmbgWKb50dv',
'access_token' : '4444601909-wx1dYmwFIUUN5Z0ti2IyglyZZNocgOfPXKnNG7W',
'access_secret' : 'aCjI2ExAC0FggfgzI6BtsjAz3zL0M8edHC8piOsjGxC5P'})

accounts.append({
'consumer_key' : 'V51Fzvh89TNDwNmnkHUOLuoYg',
'consumer_secret' : 'zkQ0UrSsox0sfWJStdUH763HYzLufg73YpHX28ZwrOLoxpVwVc',
'access_token' : '4444601909-Cconi2L2ZTkI0h1LO6D3czBZtVGdLqgHV6Ofjm9',
'access_secret' : 'dLGpzyYVWkYHxj7Dt5OCtxsiHwQpEVK1wZB8o1SmG6V3t'})

accounts.append({
'consumer_key' : 'ozCn4SrkepajOW6AIL06PvjGs',
'consumer_secret' : 'CeC0Jj7axyOStyoruT6cyR1HidIc4NQRKeWeecgDZuTbF1KM3E',
'access_token' : '4444601909-nM7OCTy2lprrlQvh9OeHY6YVQjXxfoIFBkBsFcb',
'access_secret' : 'batdpIYlIAYhyiAUjUF35BMT9QcdlR6lzmG5fYPIuJJBX'})

# kwei
accounts.append({
'consumer_key' : 'B8PeDuAVGycIPn73ceE0vLo1e',
'consumer_secret' : 'daF1UjcwavAnoFiHnNxAmyuJevG2JU9GlEYoTkRLsWiKqWb6fY',
'access_token' : '2575592904-JWrYORjYN0JPX85Q2Cbo5lYTjOpNfiNiT3fQ6Dq',
'access_secret' : '6eaZYdPSXIDA9Sr9TEvTFp0OR4aCFlDjupKPxb99TSAeY'})

accounts.append({
'consumer_key' : '48YW6WZRjyPtMGwR6VX7lBieE',
'consumer_secret' : 'wVes0R25aoNEiLcdfwTlPngZCFaF4AE7eeQpWflZtbJpo3k3eA',
'access_token' : '854237152212688896-CsaNyvQ0eIkfrDuz5TOZVCzdFpv6Peo',
'access_secret' : '6BhuokvlK1LvRH7BLCS7ZkPG2lql5TPV8SXojfeVkRc0i'})

accounts.append({
'consumer_key' : 'BISq0gnPO5sKPmSGIDDX8CoNi',
'consumer_secret' : 'wqwZPU7Eq1YBxSTGagFoy5OHcuYyoJ7cs6Wrg7yz0C8gvki6kU',
'access_token' : '854237152212688896-sjbpQYfsArfzvCKTmSqxjt5d5Lj4Ui4',
'access_secret' : '7AP93iXzTNPlJdtccQLkCb047SPXdJhJ2mIr3gwR0KkUK'})

accounts.append({
'consumer_key' : '0hDkVWYVtI3FbPBO0eabByMJr',
'consumer_secret' : 'IM4IBDHosLw1GrG5rX0pVQy9vv3wxwZdGS630lD7YPpVCZ21n2',
'access_token' : '854237152212688896-lGvQMrSPKA3I8daYWR4q20TCNi5oEah',
'access_secret' : 'UwJ2GjZjAlJmcuHhSk32WPo35RTTk8DCqhG7A3jiudUqj'})

accounts.append({
'consumer_key' : 'ZMcJlgB2POlzVbqQVgwBfMes5',
'consumer_secret' : 'tL3Ch94uEORN7dZrrWEoKZdjVPiMYscE0Am5a1MqUyskFmXTwD',
'access_token' : '2575592904-DFVFcTEZ7bB4qVCAanC32jiGJtU5LP02eOuESFK',
'access_secret' : '0HsSuWz3MpKMqWYxSod77WVW5WXX10Trq13z5Nry348bN'})

accounts.append({
'consumer_key' : '2c56wTHKAS21gA4UAZzkkwzqZ',
'consumer_secret' : 'fxAfJHIBqHGwL0f42zlzUEtJUmsxyHAD8MQ7gEqYqaau7KZyxJ',
'access_token' : '2575592904-mQN46mJwpSMj9CW5jakd79c5T34x7DjBApSf4W5',
'access_secret' : 'bYFLbECe6EjNvKM6xm4BEzA6IZk00HZ5XtaFwJ4GxfhGp'})

accounts.append({
'consumer_key' : 'QVpJC7lLXt0VqSRiB4oWOxLux',
'consumer_secret' : 'r0rQgZku1qtZtdXV1z4luOh2yiWNPWGxhdfxhl0RPyqkASCJxc',
'access_token' : '2575592904-rjouP5t0EJ1iu7vFM3kU5DBKLAZHA94YzSvtau6',
'access_secret' : 'gql0ekQiHWx5rQmurJKFp9EiNrvl6MJ7mF04rqFBwGGYx'})

# amyxie1994
accounts.append({
'consumer_key' : 'gbqEmrklOoqFEpvEFfYFmufqF',
'consumer_secret' : 'QgzOCavAiPh1wWrSAPBvj7ZZQyMJ9KxUp4Qz8SSh1WzgblQ7oE',
'access_token' : '853486226443194368-M6NEQ1DGRZX8eUUKmaXj9CsY3vv7gLA',
'access_secret' : '8qxOum5J3Uuc4kbpnoNykBoDQcHSzTF4xW9JRWhZwIbdh'})

# nanjiangl
accounts.append({
'consumer_key' : 'pXWJNLIVTT8NNmO5X2x7nQf2P',
'consumer_secret' : 'RETU3DeIbqq111XWBByJppmOOZHDNnMsb4ergE2ZQZlUDVeFCY',
'access_token' : '851662491927040000-df4TR9seEcvDWGva4OcNjMrPAC0z0ik',
'access_secret' : '0zCj63JPIcx28g1UcquZKv3vnTGXHJFaO60sPgOQgbmHY'})

accounts.append({
'consumer_key' : 'oqUpEOmJwT63m2ifD45EwWgOJ',
'consumer_secret' : 'Qd3hcSkzAATYZQpv9z5AjvOkOIqdN6fvOU1JNlGB1BsgJ0j3zp',
'access_token' : '851662491927040000-7gLy5OGe00h8evy5jKKBSNOanAVZeFn',
'access_secret' : 'd5BjxJ5EnYZG02bBpPmwpB2fF7ZuWoUzH96xmhoVef6JX'})

accounts.append({
'consumer_key' : 'D1CUDFJ8aLZ9D8VGy6vcleYfP',
'consumer_secret' : '12TndZwTsN5YReB2YJx0xIPmSvUlr7HbdBbWasrqZwA8Bks76z',
'access_token' : '851662491927040000-RLTayq8a5pzT0zz337skagbe36osxbd',
'access_secret' : 'eZ2pcRvumBQ5eO9E96VFM3XLLacf0dVwJEeBrJdSpLykR'})

accounts.append({
'consumer_key' : 'Z54Zw9U1v5HwE63UJgio1C2Eh',
'consumer_secret' : 'HebEb4OereuW3VKTSByShOIV10N8hgadyrMXc3KSywJDoCGv1V',
'access_token' : '851662491927040000-VNCzPjxMMU3wSxEC1CbshQJVkh1ie8Q',
'access_secret' : 'hmtQPook0vBXQzzpgmaAvcWqzyRtXQhctaVgk61YBboIP'})

accounts.append({
'consumer_key' : 'g5pLp0KLQ5hgRcR3fxTxQsd5p',
'consumer_secret' : 'RtgxcATM7I5ELmEnLycjI1JUBI6GY7BQF6xP2BIPY5YkvfSU40',
'access_token' : '854862643948957696-iRKez7j7mjH32YNqiKi36eotm2U2qEv',
'access_secret' : 'cGdFdOwrVHOKP37GGzqaD6SuElsb7D7Fa1nXYkGpH9DcK'})

accounts.append({
'consumer_key' : 'ybqdx2QUlaXGfuPtvq5xDum5s',
'consumer_secret' : 'XCmegsIkx5DhFEsfdukpwVLTcvCeObG6PVx073pYGFAiN5tvwd',
'access_token' : '854862643948957696-sJezdcXBvXLTqBM3V7ltJ7EX99v76Ve',
'access_secret' : 'ATo8pboqahtHE3AnGqeDd9bOGLoXtiQEcjpAawdORB4AV'})

accounts.append({
'consumer_key' : 'RbMGm2WJE1P7eQQJkYJwO8RuR',
'consumer_secret' : 'o2AwpUtXCM8mUDNmYTitCPBuqmXtkeWm7PANE1W2PN1Rmc0aaB',
'access_token' : '854862643948957696-N44ZODQraL0fpFFGCuP0wgDLKIcARCk',
'access_secret' : 'JfSi4XZ5fo0ZlxDfwuxs4cSDQnlaZQ0yS4VYOWEvHaFqc'})

accounts.append({
'consumer_key' : 'z0OFMGNhUeNyr3BLJUzP9nQ6t',
'consumer_secret' : 'D5rxzXStJZVo8UxNCu707lljqwjytsJTr4ZEIAEgYEZMcrU5Rh',
'access_token' : '854891237358186496-Ul8AHeMDRgyjrKXSdt4PD40Kkku693s',
'access_secret' : 'kWO9T8BZQBKMlrFUaXC2lDa8jD3f8dU7RNlXoxrpNoZ9Y'})

accounts.append({
'consumer_key' : '7rF55CFf3JWQNk5iEsBLIDqzM',
'consumer_secret' : 'EwdO46xaOrWXkh4raX0prEAWzBCHKOB2JDqhrALcvSrIFSJQRy',
'access_token' : '854891237358186496-7WkKebZtQbitwSHRw3nZYEoxjzgVE0O',
'access_secret' : 'nY9gniL3jUSv5YQUv5l4Sy8MS0Iufyj8UJqKkCoAjnNds'})

accounts.append({
'consumer_key' : 'ZppJmYBBlRz0H50G3UIk2cfy2',
'consumer_secret' : 'GX0rDbhcgsXb6qlvAnWIjLung3G8ELPfzdhrs4kU2EJiNMuX58',
'access_token' : '854891237358186496-ti1HW24Xk49vG2S8xvmES8oGvI8xBQR',
'access_secret' : 'A3f1AYO4vYOgfaSywTtGgksZybBhdtXA1QMbmB5DQfmvt'})

# add accounts to apis
apis = []
for account in accounts:
    auth = OAuthHandler(account['consumer_key'], account['consumer_secret'])
    auth.set_access_token(account['access_token'], account['access_secret'])
    apis.append(tweepy.API(auth))
print("Accounts added")

# connect to couchdb
# database for tweets
couch = couchdb.Server('http://' + couchIP + ':5984')
db = None
try:
    db = couch[dbName]
except couchdb.http.ResourceNotFound:
    try:
        couch.create(dbName)
        db = couch[dbName]
    except couchdb.http.PreconditionFailed:
        pass

# database for results
dbResult = None
try:
    dbResult = couch[dbNameResult]
except couchdb.http.ResourceNotFound:
    try:
        couch.create(dbNameResult)
        dbResult = couch[dbNameResult]
    except couchdb.http.PreconditionFailed:
        pass

try:
    docSmokeResult = dbResult[docNameSmokeResult]
except:
    doc_id, doc_rev = dbResult.save(smokeResult)
    pass
try:
    docEmotionResult = dbResult[docNameEmotionResult]
except:
    doc_id, doc_rev = dbResult.save(emotionResult)
    pass
try:
    docCulture = dbResult[docNameCulture]
except:
    doc_id, doc_rev = dbResult.save(culture)
    pass

def city(str):
    citylist = ['Canberra','Sydney','Melbourne','Brisbane','Perth','Darwin','Adelaide','Hobart']
    for c in citylist:
        if c in str:
            return c
    return ''
def location(friend):
    locationString = friend.location
    if locationString != '' and locationString is not None:
        local = city(locationString)
        if local != '':
            return local
    locationString = friend.time_zone
    if locationString != '' and locationString is not None:
        local = city(locationString)
        if local != '':
            return local
    try:
        locationString = friend.status.place
        if locationString != '' and locationString is not None:
            local = city(locationString.name)
            if local != '':
                return local
    except Exception:
        pass
    return ''

# class for Streaming API
class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        try:
            db[status.user.screen_name]
            print(friend.screen_name, "re")
        except couchdb.http.ResourceNotFound:
            tweet_temp = {"time":status.created_at.hour,'location':location(status.user),'text':status.text,'coordinates':status._json['coordinates']}
            db.save(tweet_temp)
        except Exception as e:
            print(e,sys._getframe().f_lineno)

try:
    # get source and rank
    dbSource = couch[dbNameSource]
    while True:
        try:
            docSource = dbSource[docNameSource]
            threadRank = docSource['count']
            startIndex = int(threadRank / threadCount * len(docSource['name']))
            endIndex = int((threadRank + 1) / threadCount * len(docSource['name']))
            for i in range(startIndex,endIndex):
                unfetchedUser.put(docSource['name'][i])
            docSource['count'] += 1
            a = dbSource.save(docSource)
            accountPos += int(threadRank * (len(accounts) / threadCount + 1))
            break
        except couchdb.http.ResourceConflict as e:
            print(e, sys._getframe().f_lineno)

    # start crawling
    # half crawling by REST API
    if threadRank % 2 == 0:
        starttime = time.time()
        userCount = 0
        for i in range(peopleMaxCount):
            screenName = unfetchedUser.get()
            print(screenName, unfetchedUser.qsize())

            # fetch friends
            while True:
                try:
                    # get users in a low frequency
                    if unfetchedUserQueueCapacity - unfetchedUser.qsize() < 20:
                        break
                    friendCount = min(unfetchedUserQueueCapacity - unfetchedUser.qsize(),friendMaxCount)
                    for friend in tweepy.Cursor(apis[accountPos].friends, screen_name = screenName).items(friendCount):
                        # judge conditions
                        if friend.lang != 'en' or friend.followers_count < 5 or friend.statuses_count < 10:
                            continue
                        local = location(friend)
                        if local == '':
                            continue
                        try:
                            db[friend.screen_name] # judge if existing
                            print(friend.screen_name, "re")
                        except couchdb.http.ResourceNotFound:
                            unfetchedUser.put(friend.screen_name)
                        except Exception as e:
                            print(e,sys._getframe().f_lineno)
                    break
                except tweepy.error.RateLimitError as e:
                    accountPos = accountPos + 1
                    accountPos = accountPos % len(accounts)
                    time.sleep(5)
                    print(e,accountPos,'friend',sys._getframe().f_lineno)
                except tweepy.error.TweepError as e:
                    if e.response is None:
                        raise e
                    # error rate limit exceeded
                    elif e.api_code == 326:
                        accountPos = accountPos + 1
                        accountPos = accountPos % len(accounts)
                        time.sleep(5)
                        print(e,accountPos,'friend e.api_code 326',sys._getframe().f_lineno)
                    # error Bad request or URI not found
                    elif e.response.status_code in set([401, 404]): ##############
                        print(e,"status_code 401 404",sys._getframe().f_lineno)
                        break
                    else:
                        print(e,'friend',sys._getframe().f_lineno)
                        break
            # crawling tweets
            while True:
                try:
                    statusJsons = []
                    id = None
                    for i in range(2):
                        tweets = None
                        if id == None:
                            tweets = tweepy.Cursor(apis[accountPos].user_timeline, screen_name = screenName, include_rts = False).items(statusMaxCount)
                        else:
                            tweets = tweepy.Cursor(apis[accountPos].user_timeline, screen_name = screenName, include_rts = False,max_id = id - 1).items(statusMaxCount)
                        for status in tweets:
                            # save tweets into a list temporarily
                            tweet_temp = {"time":status.created_at.hour,'location':location(status.user),'text':status.text,'coordinates':status._json['coordinates']}
                            try:
                                smoke_drink.smoke_Drink_per(tweet_temp,smokeResult)
                            except Exception as e:
                                print(e,sys._getframe().f_lineno)
                            try:
                                sentiment_analysis.sentiment_analy(analyzer, tweet_temp,emotionResult)
                            except Exception as e:
                                print(e,sys._getframe().f_lineno)
                            try:
                                Culture.culture_per(tweet_temp,culture)
                            except Exception as e:
                                print(e,sys._getframe().f_lineno)
                            statusJsons.append(tweet_temp)
                            id = status.id
                    if len(statusJsons) > 0:
                        if screenName[0] == '_': # delete underscore in 1st place of name
                            print(screenName)
                            screenName = screenName[1:]
                            print(screenName)
                        saveDict = {'_id':screenName,'status':statusJsons}
                        try:
                            db.save(saveDict) # save to database
                        except Exception as e:
                            print(e,sys._getframe().f_lineno)
                    break
                # error too many requests
                except tweepy.error.RateLimitError as e:
                    accountPos = accountPos + 1
                    accountPos = accountPos % len(accounts)
                    time.sleep(5)
                    print(e,accountPos,'status',sys._getframe().f_lineno)
                except tweepy.error.TweepError as e:
                    if e.response is None:
                        print(e,"None",sys._getframe().f_lineno)
                    # error rate limit exceeded
                    elif e.response.status_code in set([326,429]):
                        accountPos = accountPos + 1
                        accountPos = accountPos % len(accounts)
                        time.sleep(5)
                        print(e,sys._getframe().f_lineno)
                    else:
                        print(e,sys._getframe().f_lineno)
                        break
            print(time.time() - starttime,i)
            userCount += 1
            if userCount % 5 == 0:
                dbResult.save(smokeResult)
                dbResult.save(emotionResult)
                dbResult.save(culture)
                pass
        while not unfetchedUser.empty():
            print(unfetchedUser.get())
    # half crawling by Streaming API
    else:
        tweetStream = Stream(api.auth,MyStreamListener())
        tweetStream.filter(track=['smoke','smoker','smokers','smoking','smokie','cigar','ciggie','ciggy','fag','durry','tobacco','tobaccos',
                              'cigarette','cigarette case','King Street','Bond Street','free choice','Choice Signature','JPS RYO',
                              'Champion blue','Marlboro','Winfield','Longbeach','Peter Jackson','Horizon','Holiday','Alpine','Dunhill',
                              'Escort','ashtray','lighter','lighters','match','Easy','JPS','B&H','PJ','Rothmans','P/Stuyv','alcohol',
                              'atubby','slab','drunk','drink','drank','bar','barburger','muso','bottle-o','bottle','pint','jar','wine',
                              'ale','beer','spirits','whiskey','brandy','champagne','tequila','rum','sake','liquor','shochu',
                              'anti-smoking','non-smoking','smoking zone','smoking area','quit smoking','alcoholic','alcoholism',
                              'bacchant','sottish','dipsopathy','alcoholics','drunkenness','intoxication','temulentia','temulence',
                              'zonked','abstinence','Chinese','China','China Town','Peking Opera','Kunfu','cheongsam','Beijing',
                              'Shanghai','Hangzhou','Xi\'an','Sichuan','Chengdu','Guangzhou','Nanjing','Suzhou','Tibet','Tianjing',
                              'Xiamen','Jinan','Pudong','Taiyuan','Sanya','Hainan','Kunming','Great Wall','Forbidden City',
                              'Potala Palace','Terracotta Warriors and Horses','Huangshan','Taishan','Wutaishan','Yellow River',
                              'Yangtze','Taiji','Hot pot','Dim sum','General Tsao\'s Chicken','Orange Chicken','Fortune Cookie',
                              'Gong Bao Chicken','Mapo tofu','Dumplings','Won ton Soup','Peking Duck','Chow Mein','Hand Pulled Noodles',
                              'Tsing Tao','Snow','Maotai','Yanjing','Yuxi','Shenzhou','Gaokao','Panda','nihao','NIHAO','RMB','Mahjong',
                              'Yin and Yang','Feng shui','Journey to the West','Dream of Red Mansions','Three Kingdoms','Confucius',
                              'Lao Tzu','Sun Tzu','Qin Shihuang','Emperor Wu','Sun Yat-sen','Chiang Kai-shek','Mao Zedong','Zhou Enlai',
                              'Deng Xiaoping','Xi Jinping','Bruce Lee','Yao Ming','People\'s Republic of China',
                              'The Chinese Communist Party','PRC','Spring Festival','Ching Ming Festival','Lantern Festival',
                              'Mid-Autumn Festival','Erhu','Guzheng','Hulusi','Tsinghua University','Beijing University',
                              'Fudan University','Zhejiang University','People\'s University','Nanjing University','Alibaba',
                              'Union Pay','Huili','Taobao','Lenovo','Haier','Hisense','Huawei','BYD','DJI','OPPO','Xiaomi','VIVO','WeChat'])
except Exception as e:
    f = open('cluster.out','w',encoding='utf8')
    while not unfetchedUser.empty():
        str = unfetchedUser.get()
        f.write(str)
        print(str)
    print(e,sys._getframe().f_lineno)
