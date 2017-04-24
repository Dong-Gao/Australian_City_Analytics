import couchdb
def test_data():
    test=[{'location':'Melbourne','text':'beer BMW happy! cigar'},{'location':'Melbourne','text':'pint Ford sorry!'},{'location':'Peth','text':'Who has fire lighter? VW Mustang Ford:)! cigar'},{'location':'Hobart','text':'Holden,Ford,new car! so cheerful!'}]
    return test
def country_list_data():
    country_list={'Melbourne':{"German": 0, "Italian": 0, "French": 0, "British": 0,
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
    return country_list
# tweet format should be dict
# list format should be dict
def vehicle_manufacturer_country(tweet,country_list):
    German = ["Mercedes-Benz", "Audi","A6","A8","TT", "Volkswagen","VW","Benz", "BMW", "Opel", "Porsche"]
    Italian = ["Fiat", "Lancia", "Alfa Romeo", "Lamborghini", "Maserati", "Ferrari"]
    French = ["Citroen", "Renault", "Bugatti", "Alpine", "Peugeot","3008","4008","5008"]
    British = ["McLaren", "Aston Martin", "Vauxhall", "Bentley", "Rolls-Royce","RR", "Land Rover","Range Rover","Cooper" "Mini"]
    American = ["Chrysler", "Dodge", "Jeep", "Cherokee","Mustang","Chevrolet", "Buick", "GMC", "Cadillac", "Lincoln", "Ford"]
    Japanese = ["Honda", "Civic","Toyota","Prado" ,"Suzuki", "Lexus", "Infiniti", "Atenza","Axela","MX-5","Mazda", "Mitsubishi", "Nissan","GTR"]
    Korean = ["Hyundai", "Kia", "Daewoo"]
    Chinese = ["Geely", "Chery", "Hongqi", "Brilliance", "BYD"]
    Australian = ["Holden"]

    tweet_text=tweet['text']
    loc=tweet['location']
    for l in country_list:
        if l==loc:
            for brand in German:
                if brand in tweet_text:
                    country_list[l]["German"] = country_list[l]["German"] + 1
            for brand in Italian:
                if brand in tweet_text:
                    country_list[l]["Italian"] = country_list[l]["Italian"] + 1
            for brand in French:
                if brand in tweet_text:
                    country_list[l]["French"] = country_list[l]["French"] + 1
            for brand in British:
                if brand in tweet_text:
                    country_list[l]["British"] = country_list[l]["British"] + 1
            for brand in American:
                if brand in tweet_text:
                    country_list[l]["American"] = country_list[l]["American"] + 1
            for brand in Japanese:
                if brand in tweet_text:
                    country_list[l]["Japanese"] = country_list[l]["Japanese"] + 1
            for brand in Korean:
                if brand in tweet_text:
                    country_list[l]["Korean"] = country_list[l]["Korean"] + 1
            for brand in Chinese:
                if brand in tweet_text:
                    country_list[l]["Chinese"] = country_list[l]["Chinese"] + 1
            for brand in Australian:
                if brand in tweet_text:
                    country_list[l]["Australian"] = country_list[l]["Australian"] + 1
    return country_list

def vehicle_exe(vehicle):
    country_list=country_list_data()
    #server = couchdb.Server('placeholer')
    #db=server['placeholer']
    #for tweet in db:
    #    vehicle_manufacturer_country(tweet,country_list)
    test=test_data()
    for i in range(0,len(test)):
        vehicle_manufacturer_country(test[i],country_list)
    for i in country_list:
        count = 0
        for j in country_list[i]:
            if country_list[i][j]==0:
                count=count+1
        if count==9:
            vehicle[i] = 'N/A'
        else:
            vehicle[i] = max(country_list[i].items(), key=lambda x: x[1])[0]
    return vehicle