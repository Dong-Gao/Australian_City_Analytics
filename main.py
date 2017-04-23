import couchdb
import vehicle
import beer
import re
import SentimentAnalysis
server = couchdb.Server('地址')
db=server['库名']
emotion={'Melbourne':{'0-6':0,'6-12':0,'12-18':0,'18-24':0},
          'Sydney':{'0-6':0,'6-12':0,'12-18':0,'18-24':0},
          'Peth':{'0-6':0,'6-12':0,'12-18':0,'18-24':0},
          'Darwin':{'0-6':0,'6-12':0,'12-18':0,'18-24':0},
          'Canberra':{'0-6':0,'6-12':0,'12-18':0,'18-24':0},
          'Hobart':{'0-6':0,'6-12':0,'12-18':0,'18-24':0},
          'Adelaide':{'0-6':0,'6-12':0,'12-18':0,'18-24':0},
          'Brisbane':{'0-6':0,'6-12':0,'12-18':0,'18-24':0}}
for tweet in db:
