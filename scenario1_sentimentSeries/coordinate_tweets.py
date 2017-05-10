import json
#This function is for finding the tweets with coordinates and store them.
def tweet_coor():
     filesource = open('status.json', 'r', encoding='utf-8')
     file = open('corrdinateData.json', 'a', encoding='utf-8')
     count = 0
     for line in filesource:
         tweet = json.loads(line)
         try:
             tweet['location']
         except:
             # print(tweet)
             continue
         if tweet['location'] == '':
             continue
         if tweet['coordinates'] != None:
             # print(tweet)
             str = json.dumps(tweet, ensure_ascii=False)
             file.write(str)
             file.write('\n')
             count += 1
     filesource.close()
     file.close()
     print(count)


 #Find the tweets having coordinates which is within the range of these 8 cities.
def coor_city():
    coordinates = {'Melbourne': (144.9631, -37.8136), 'Sydney': (151.2093, -33.8688), 'Perth': (115.8605, -31.9505),
                   'Darwin': (130.8456, -12.4634), 'Canberra': (149.1300, -35.2809), 'Hobart': (147.3272, -42.8821),
                   'Adelaide': (138.6007, -34.9285), 'Brisbane': (153.0251, -27.4698)}
    filesource = open('corrdinateData.json', 'r', encoding='utf-8')
    file = open('suburbData.json', 'a', encoding='utf-8')
    count = 0
    for line in filesource:
        tweet = json.loads(line)
        try:
            if tweet['location'] == '':
                x = tweet['coordinates']['coordinates'][0]
                y = tweet['coordinates']['coordinates'][1]
                for i in coordinates:
                    if -1.2 < x - coordinates[i][0] < 1.2:
                        if -1.2 < y - coordinates[i][1] < 1.2:
                            count += 1
                            # tweet['location'] = i
                            str = json.dumps(tweet, ensure_ascii=False)
                            # file.write(str)
                            # file.write('\n')
                            break
                continue
        except:
            # print(tweet)
            temp = count
            x = tweet['coordinates']['coordinates'][0]
            y = tweet['coordinates']['coordinates'][1]
            for i in coordinates:
                if -1.2 < x - coordinates[i][0] < 1.2:
                    if -1.2 < y - coordinates[i][1] < 1.2:
                        count += 1
                        tweet['location'] = i
                        str = json.dumps(tweet, ensure_ascii=False)
                        # file.write(str)
                        # file.write('\n')
                        break
                        # if temp == count:
                        # print(tweet)
            continue
        count += 1
        str = json.dumps(tweet, ensure_ascii=False)
        file.write(str)
        file.write('\n')
    filesource.close()
    file.close()
    print(count)
