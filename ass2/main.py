
import vehicle
import beer
import sentiment_analysis
import smoke_drink

emotionResult={'Melbourne':{'0-6':0,'6-12':0,'12-18':0,'18-24':0},
          'Sydney':{'0-6':0,'6-12':0,'12-18':0,'18-24':0},
          'Peth':{'0-6':0,'6-12':0,'12-18':0,'18-24':0},
          'Darwin':{'0-6':0,'6-12':0,'12-18':0,'18-24':0},
          'Canberra':{'0-6':0,'6-12':0,'12-18':0,'18-24':0},
          'Hobart':{'0-6':0,'6-12':0,'12-18':0,'18-24':0},
          'Adelaide':{'0-6':0,'6-12':0,'12-18':0,'18-24':0},
          'Brisbane':{'0-6':0,'6-12':0,'12-18':0,'18-24':0}}
smokeResult={'Melbourne':{'positive':0,'negative':0,'tolerant':0},'Sydney':{'positive':0,'negative':0,'tolerant':0},
             'Peth':{'positive':0,'negative':0,'tolerant':0},'Darwin':{'positive':0,'negative':0,'tolerant':0},
             'Canberra':{'positive':0,'negative':0,'tolerant':0},'Hobart':{'positive':0,'negative':0,'tolerant':0},
             'Adelaide':{'positive':0,'negative':0,'tolerant':0},'Brisbane':{'positive':0,'negative':0,'tolerant':0}}
vehicleResult={'Melbourne':'N/A','Sydney':'N/A','Peth':'N/A','Darwin':'N/A','Canberra':'N/A','Hobart':'N/A','Adelaide':'N/A','Brisbane':'N/A'}
beerResult={'Melbourne':'N/A','Sydney':'N/A','Peth':'N/A','Darwin':'N/A','Canberra':'N/A','Hobart':'N/A','Adelaide':'N/A','Brisbane':'N/A'}

sentiment_analysis.sentiment_analysis(emotionResult)
smoke_drink.smoke_Drink(smokeResult)
vehicle.vehicle_exe(vehicleResult)
beer.beer_exe(beerResult)
print(beerResult)
print(vehicleResult)
#print(smokeResult)
print(emotionResult)