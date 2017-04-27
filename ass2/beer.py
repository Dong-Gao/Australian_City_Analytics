import couchdb
def test_data():
    test=[{'location':'Melbourne','text':'beer BMW , Tsingtao, happy! cigar'},{'location':'Melbourne','text':'pint Ford sorry!'},{'location':'Peth','text':'Who has fire lighter? VW with Asahi :)! cigar'},{'location':'Canberra','text':'Holden,new car cider! so cheerful!'}]
    return test

def beer_data():
    beer={'Melbourne':{"Snow": 0, "Tsingtao": 0, "Bud Light": 0, "Budweiser": 0, "Skol": 0, "Yanjing": 0, "Heineken": 0, "Harbin": 0,
         "Brahma": 0, "Coors Light": 0, "Victoria Bitter": 0, " XXXX Gold": 0, " Carlton Premium Dry ": 0,
         "Carlton Draught": 0, "Corona Extra": 0, "Toohey’s New": 0, "Toohey’s Extra Dry": 0,
         "Carlton Mid Strength": 0, "Crown Lager": 0, "Oettinger": 0, "Asahi":0,"Mountain Goat":0,"cider":0},
      'Sydney':{"Snow": 0, "Tsingtao": 0, "Bud Light": 0, "Budweiser": 0, "Skol": 0, "Yanjing": 0, "Heineken": 0, "Harbin": 0,
         "Brahma": 0, "Coors Light": 0, "Victoria Bitter": 0, " XXXX Gold": 0, " Carlton Premium Dry ": 0,
         "Carlton Draught": 0, "Corona Extra": 0, "Toohey’s New": 0, "Toohey’s Extra Dry": 0,
         "Carlton Mid Strength": 0, "Crown Lager": 0, "Oettinger": 0, "Asahi":0,"Mountain Goat":0,"cider":0},
      'Peth':{"Snow": 0, "Tsingtao": 0, "Bud Light": 0, "Budweiser": 0, "Skol": 0, "Yanjing": 0, "Heineken": 0, "Harbin": 0,
         "Brahma": 0, "Coors Light": 0, "Victoria Bitter": 0, " XXXX Gold": 0, " Carlton Premium Dry ": 0,
         "Carlton Draught": 0, "Corona Extra": 0, "Toohey’s New": 0, "Toohey’s Extra Dry": 0,
         "Carlton Mid Strength": 0, "Crown Lager": 0, "Oettinger": 0, "Asahi":0,"Mountain Goat":0,"cider":0},
      'Darwin':{"Snow": 0, "Tsingtao": 0, "Bud Light": 0, "Budweiser": 0, "Skol": 0, "Yanjing": 0, "Heineken": 0, "Harbin": 0,
         "Brahma": 0, "Coors Light": 0, "Victoria Bitter": 0, " XXXX Gold": 0, " Carlton Premium Dry ": 0,
         "Carlton Draught": 0, "Corona Extra": 0, "Toohey’s New": 0, "Toohey’s Extra Dry": 0,
         "Carlton Mid Strength": 0, "Crown Lager": 0, "Oettinger": 0, "Asahi":0,"Mountain Goat":0,"cider":0},
      'Canberra':{"Snow": 0, "Tsingtao": 0, "Bud Light": 0, "Budweiser": 0, "Skol": 0, "Yanjing": 0, "Heineken": 0, "Harbin": 0,
         "Brahma": 0, "Coors Light": 0, "Victoria Bitter": 0, " XXXX Gold": 0, " Carlton Premium Dry ": 0,
         "Carlton Draught": 0, "Corona Extra": 0, "Toohey’s New": 0, "Toohey’s Extra Dry": 0,
         "Carlton Mid Strength": 0, "Crown Lager": 0, "Oettinger": 0, "Asahi":0,"Mountain Goat":0,"cider":0},
      'Hobart':{"Snow": 0, "Tsingtao": 0, "Bud Light": 0, "Budweiser": 0, "Skol": 0, "Yanjing": 0, "Heineken": 0, "Harbin": 0,
         "Brahma": 0, "Coors Light": 0, "Victoria Bitter": 0, " XXXX Gold": 0, " Carlton Premium Dry ": 0,
         "Carlton Draught": 0, "Corona Extra": 0, "Toohey’s New": 0, "Toohey’s Extra Dry": 0,
         "Carlton Mid Strength": 0, "Crown Lager": 0, "Oettinger": 0, "Asahi":0,"Mountain Goat":0,"cider":0},
      'Adelaide':{"Snow": 0, "Tsingtao": 0, "Bud Light": 0, "Budweiser": 0, "Skol": 0, "Yanjing": 0, "Heineken": 0, "Harbin": 0,
         "Brahma": 0, "Coors Light": 0, "Victoria Bitter": 0, " XXXX Gold": 0, " Carlton Premium Dry ": 0,
         "Carlton Draught": 0, "Corona Extra": 0, "Toohey’s New": 0, "Toohey’s Extra Dry": 0,
         "Carlton Mid Strength": 0, "Crown Lager": 0, "Oettinger": 0, "Asahi":0,"Mountain Goat":0,"cider":0},
      'Brisbane':{"Snow": 0, "Tsingtao": 0, "Bud Light": 0, "Budweiser": 0, "Skol": 0, "Yanjing": 0, "Heineken": 0, "Harbin": 0,
         "Brahma": 0, "Coors Light": 0, "Victoria Bitter": 0, " XXXX Gold": 0, " Carlton Premium Dry ": 0,
         "Carlton Draught": 0, "Corona Extra": 0, "Toohey’s New": 0, "Toohey’s Extra Dry": 0,
         "Carlton Mid Strength": 0, "Crown Lager": 0, "Oettinger": 0, "Asahi":0,"Mountain Goat":0,"cider":0}}
    return beer

def beer_brand(tweet, beer_list):
    tweet_text=tweet['text']
    loc=tweet['location']
    for l in beer_list:
        if l==loc:
            if "Snow" in tweet_text:
                beer_list[l]["Snow"] = beer_list[l]["Snow"] + 1
            if "Tsingtao" in tweet_text:
                beer_list[l]["Tsingtao"] = beer_list[l]["Tsingtao"] + 1
            if "Bud Light" in tweet_text:
                beer_list[l]["Bud Light"] = beer_list[l]["Bud Light"] + 1
            if "Budweiser" in tweet_text:
                beer_list[l]["Budweiser"] = beer_list[l]["Budweiser"] + 1
            if "Skol" in tweet_text:
                beer_list[l]["Skol"] = beer_list[l]["Skol"] + 1
            if "Yanjing" in tweet_text:
                beer_list[l]["Yanjing"] = beer_list[l]["Yanjing"] + 1
            if "Heineken" in tweet_text:
                beer_list[l]["Heineken"] = beer_list[l]["Heineken"] + 1
            if "Harbin" in tweet_text:
                beer_list[l]["Harbin"] = beer_list[l]["Harbin"] + 1
            if "Brahma" in tweet_text:
                beer_list[l]["Brahma"] = beer_list[l]["Brahma"] + 1
            if "Coors Light" in tweet_text:
                beer_list[l]["Coors Light"] = beer_list[l]["Coors Light"] + 1
            if "Victoria Bitter" in tweet_text or "VB" in tweet_text:
                beer_list[l]["Victoria Bitter"] = beer_list[l]["Victoria Bitter"] + 1
            if " XXXX Gold" in tweet_text:
                beer_list[l][" XXXX Gold"] = beer_list[l][" XXXX Gold"] + 1
            if "Carlton Premium Dry" in tweet_text:
                beer_list[l]["Carlton Premium Dry"] = beer_list[l]["Carlton Premium Dry"] + 1
            if "Carlton Draught" in tweet_text:
                beer_list[l]["Carlton Draught"] = beer_list[l]["Carlton Draught"] + 1
            if "Corona Extra" in tweet_text:
                beer_list[l]["Corona Extra"] = beer_list[l]["Corona Extra"] + 1
            if "Toohey’s New " in tweet_text:
                beer_list[l]["Toohey’s New "] = beer_list[l]["Toohey’s New "] + 1
            if "Toohey’s Extra Dry" in tweet_text:
                beer_list[l]["Toohey’s Extra Dry"] = beer_list[l]["Toohey’s Extra Dry"] + 1
            if "Carlton Mid Strength" in tweet_text:
                beer_list[l]["Carlton Mid Strength"] = beer_list[l]["Carlton Mid Strength"] + 1
            if "Crown Lager" in tweet_text:
                beer_list[l]["Crown Lager"] = beer_list[l]["Crown Lager"] + 1
            if "Oettinger" in tweet_text:
                beer_list[l]["Oettinger"] = beer_list[l]["Oettinger"] + 1
            if "Asahi" in tweet_text:
                beer_list[l]["Asahi"] = beer_list[l]["Asahi"] + 1
            if "Mountain Goat" in tweet_text:
                beer_list[l]["Mountain Goat"] = beer_list[l]["Mountain Goat"] + 1
            if "cider" in tweet_text:
                beer_list[l]["cider"] = beer_list[l]["cider"] + 1
    return beer_list

def beer_exe(beerResult):
    beer_list=beer_data()
    server = couchdb.Server('placeholer')
    db=server['placeholer']
    ##用户名 sourcead
    ##密码 iamfine
    for tweet in db:
        beer_brand(tweet,beer_list)
    #test=test_data()
    #for i in range(0,len(test)):
    #    beer_brand(test[i],beer_list)
    for i in beer_list:
        count = 0
        for j in beer_list[i]:
            if beer_list[i][j]==0:
                count=count+1
        if count==23:
            beerResult[i] = 'N/A'
        else:
            beerResult[i] = max(beer_list[i].items(), key=lambda x: x[1])[0]
    return beerResult
