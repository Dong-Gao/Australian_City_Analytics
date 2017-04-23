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
smokeResult={'Melbourne':{'positive':0,'negative':0},'Sydney':{'positive':0,'negative':0},
             'Peth':{'positive':0,'negative':0},'Darwin':{'positive':0,'negative':0},
             'Canberra':{'positive':0,'negative':0},'Hobart':{'positive':0,'negative':0},
             'Adelaide':{'positive':0,'negative':0},'Brisbane':{'positive':0,'negative':0}}
vehicle={'Melbourne':{"German": 0, "Italian": 0, "French": 0, "British": 0, 
                      "American": 0, "Japanese": 0, "Korean": 0, "Chinese": 0, "Australian": 0},
          'Sydney':{"German": 0, "Italian": 0, "French": 0, "British": 0, 
                      "American": 0, "Japanese": 0, "Korean": 0, "Chinese": 0, "Australian": 0},
          'Peth':{"German": 0, "Italian": 0, "French": 0, "British": 0, 
                      "American": 0, "Japanese": 0, "Korean": 0, "Chinese": 0, "Australian": 0},
          'Darwin':{"German": 0, "Italian": 0, "French": 0, "British": 0, 
                      "American": 0, "Japanese": 0, "Korean": 0, "Chinese": 0, "Australian": 0},
          'Canberra':{"German": 0, "Italian": 0, "French": 0, "British": 0, 
                      "American": 0, "Japanese": 0, "Korean": 0, "Chinese": 0, "Australian": 0},
          'Hobart':{"German": 0, "Italian": 0, "French": 0, "British": 0, 
                      "American": 0, "Japanese": 0, "Korean": 0, "Chinese": 0, "Australian": 0},
          'Adelaide':{"German": 0, "Italian": 0, "French": 0, "British": 0, 
                      "American": 0, "Japanese": 0, "Korean": 0, "Chinese": 0, "Australian": 0},
          'Brisbane':{"German": 0, "Italian": 0, "French": 0, "British": 0, 
                      "American": 0, "Japanese": 0, "Korean": 0, "Chinese": 0, "Australian": 0}}
beer={'Melbourne':{"Snow": 0, "Tsingtao": 0, "Bud Light": 0, "Budweiser": 0, "Skol": 0, "Yanjing": 0, "Heineken": 0, "Harbin": 0,
                     "Brahma": 0, "Coors Light": 0, "Victoria Bitter": 0, " XXXX Gold": 0, " Carlton Premium Dry ": 0,
                     "Carlton Draught": 0, "Corona Extra": 0, "Toohey’s New": 0, "Toohey’s Extra Dry": 0,
                    "Carlton Mid Strength": 0, "Crown Lager": 0, "Oettinger": 0},
          'Sydney':{"Snow": 0, "Tsingtao": 0, "Bud Light": 0, "Budweiser": 0, "Skol": 0, "Yanjing": 0, "Heineken": 0, "Harbin": 0,
                    "Brahma": 0, "Coors Light": 0, "Victoria Bitter": 0, " XXXX Gold": 0, " Carlton Premium Dry ": 0,
                    "Carlton Draught": 0, "Corona Extra": 0, "Toohey’s New": 0, "Toohey’s Extra Dry": 0,
                    "Carlton Mid Strength": 0, "Crown Lager": 0, "Oettinger": 0},
          'Peth':{"Snow": 0, "Tsingtao": 0, "Bud Light": 0, "Budweiser": 0, "Skol": 0, "Yanjing": 0, "Heineken": 0, "Harbin": 0,
                    "Brahma": 0, "Coors Light": 0, "Victoria Bitter": 0, " XXXX Gold": 0, " Carlton Premium Dry ": 0,
                    "Carlton Draught": 0, "Corona Extra": 0, "Toohey’s New": 0, "Toohey’s Extra Dry": 0,
                    "Carlton Mid Strength": 0, "Crown Lager": 0, "Oettinger": 0},
          'Darwin':{"Snow": 0, "Tsingtao": 0, "Bud Light": 0, "Budweiser": 0, "Skol": 0, "Yanjing": 0, "Heineken": 0, "Harbin": 0,
                    "Brahma": 0, "Coors Light": 0, "Victoria Bitter": 0, " XXXX Gold": 0, " Carlton Premium Dry ": 0,
                    "Carlton Draught": 0, "Corona Extra": 0, "Toohey’s New": 0, "Toohey’s Extra Dry": 0,
                    "Carlton Mid Strength": 0, "Crown Lager": 0, "Oettinger": 0},
          'Canberra':{"Snow": 0, "Tsingtao": 0, "Bud Light": 0, "Budweiser": 0, "Skol": 0, "Yanjing": 0, "Heineken": 0, "Harbin": 0,
                    "Brahma": 0, "Coors Light": 0, "Victoria Bitter": 0, " XXXX Gold": 0, " Carlton Premium Dry ": 0,
                    "Carlton Draught": 0, "Corona Extra": 0, "Toohey’s New": 0, "Toohey’s Extra Dry": 0,
                    "Carlton Mid Strength": 0, "Crown Lager": 0, "Oettinger": 0},
          'Hobart':{"Snow": 0, "Tsingtao": 0, "Bud Light": 0, "Budweiser": 0, "Skol": 0, "Yanjing": 0, "Heineken": 0, "Harbin": 0,
                    "Brahma": 0, "Coors Light": 0, "Victoria Bitter": 0, " XXXX Gold": 0, " Carlton Premium Dry ": 0,
                    "Carlton Draught": 0, "Corona Extra": 0, "Toohey’s New": 0, "Toohey’s Extra Dry": 0,
                    "Carlton Mid Strength": 0, "Crown Lager": 0, "Oettinger": 0},
          'Adelaide':{"Snow": 0, "Tsingtao": 0, "Bud Light": 0, "Budweiser": 0, "Skol": 0, "Yanjing": 0, "Heineken": 0, "Harbin": 0,
                    "Brahma": 0, "Coors Light": 0, "Victoria Bitter": 0, " XXXX Gold": 0, " Carlton Premium Dry ": 0,
                    "Carlton Draught": 0, "Corona Extra": 0, "Toohey’s New": 0, "Toohey’s Extra Dry": 0,
                    "Carlton Mid Strength": 0, "Crown Lager": 0, "Oettinger": 0},
          'Brisbane':{"Snow": 0, "Tsingtao": 0, "Bud Light": 0, "Budweiser": 0, "Skol": 0, "Yanjing": 0, "Heineken": 0, "Harbin": 0,
                    "Brahma": 0, "Coors Light": 0, "Victoria Bitter": 0, " XXXX Gold": 0, " Carlton Premium Dry ": 0,
                    "Carlton Draught": 0, "Corona Extra": 0, "Toohey’s New": 0, "Toohey’s Extra Dry": 0,
                    "Carlton Mid Strength": 0, "Crown Lager": 0, "Oettinger": 0}}





emotionResult={'Melbourne':{'0-6':0,'6-12':0,'12-18':0,'18-24':0},
          'Sydney':{'0-6':0,'6-12':0,'12-18':0,'18-24':0},
          'Peth':{'0-6':0,'6-12':0,'12-18':0,'18-24':0},
          'Darwin':{'0-6':0,'6-12':0,'12-18':0,'18-24':0},
          'Canberra':{'0-6':0,'6-12':0,'12-18':0,'18-24':0},
          'Hobart':{'0-6':0,'6-12':0,'12-18':0,'18-24':0},
          'Adelaide':{'0-6':0,'6-12':0,'12-18':0,'18-24':0},
          'Brisbane':{'0-6':0,'6-12':0,'12-18':0,'18-24':0}}
def emotion(tweet,emotion):
    for i in emotionResult:
        emotionResult[i]['0-6']=emotionScore[i]['0-6']['total']/emotionScore[i]['0-6']['amount']
        emotionResult[i]['6-12'] = emotionScore[i]['6-12']['total'] / emotionScore[i]['6-12']['amount']
        emotionResult[i]['12-18'] = emotionScore[i]['12-18']['total'] / emotionScore[i]['12-18']['amount']
        emotionResult[i]['12-18'] = emotionScore[i]['0-6']['total'] / emotionScore[i]['12-18']['amount']
    return  emotionResult
          

          
          
          
          


          
      
