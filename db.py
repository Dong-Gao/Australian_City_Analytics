import couchdb
import vehicle
import beer

list1 = {"German": 0, "Italian": 0, "French": 0, "British": 0, "American": 0, "Japanese": 0, "Korean": 0, "Chinese": 0,
         "Australian": 0}
list2 = {"Snow": 0, "Tsingtao": 0, "Bud Light": 0, "Budweiser": 0, "Skol": 0, "Yanjing": 0, "Heineken": 0, "Harbin": 0,
         "Brahma": 0, "Coors Light": 0, "Victoria Bitter": 0, " XXXX Gold": 0, " Carlton Premium Dry ": 0,
         "Carlton Draught": 0, "Corona Extra": 0, "Toohey’s New": 0, "Toohey’s Extra Dry": 0,
         "Carlton Mid Strength": 0, "Crown Lager": 0, "Oettinger": 0}
server = couchdb.Server()
db = server['test']
for tweet in db:
    content = db[tweet]["text"]
    vehicle.vehicle_manufacturer_country(content, list1)
for tweet in db:
    content = db[tweet]["text"]
    beer.beer_brand(content, list2)
print(list1)
print(list2)
print(max(list1, key=list1.get))
