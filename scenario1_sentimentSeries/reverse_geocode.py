import urllib, json
#from nltk.sentiment.vader import SentimentIntensityAnalyzer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import time

start = time.clock()
coor_range = {}
filesource = open('suburbData.json', 'r', encoding='utf-8')
file = open('melbourneSuburb', 'a', encoding='utf-8')
analyzer = SentimentIntensityAnalyzer()
count=0
suburbs = []
for line in filesource:
    tweet = json.loads(line)
    if tweet['location'] == 'Perth':
        lat = tweet['coordinates']['coordinates'][1]
        lon = tweet['coordinates']['coordinates'][0]
        url = "http://nominatim.openstreetmap.org/reverse?format=json&lat=" + str(lat) + "&lon=" + str(lon) + "&zoom=18&addressdetails=1"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        count += 1
        try:
            suburb = data['address']['suburb']
        except:
            print()
        if suburb == '':
            print("No Suburb Returned!")
        else:
            score = analyzer.polarity_scores(tweet['text'])
            #Add the sentiment score and corresponding suburb attributes into tweets.
            tweet['suburb'] = suburb
            tweet['score'] = score['compound']
            coor_range[suburb] = data['boundingbox']
            #print(coor_range)
            new = json.dumps(tweet, ensure_ascii=False)
            file.write(new)
            file.write('\n')
            if suburb not in suburbs:
                suburbs.append(suburb)
                print(suburb)
            if count % 100 == 0:
                print(count)

end = time.clock()
print(end-start)