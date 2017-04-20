German = ["Mercedes-Benz", "Audi", "Volkswagen", "BMW", "Opel", "Porsche"]
Italian = ["Fiat", "Lancia", "Alfa Romeo", "Lamborghini", "Maserati", "Ferrari"]
French = ["Citroen", "Renault", "Bugatti", "Alpine", "Peugeot"]
British = ["McLaren", "Aston Martin", "Vauxhall", "Bentley", "Rolls-Royce", "Land Rover", "Mini"]
American = ["Chrysler", "Dodge", "Jeep", "Chevrolet", "Buick", "GMC", "Cadillac", "Lincoln", "Ford"]
Japanese = ["Honda", "Toyota", "Suzuki", "Lexus", "Infiniti", "Mazda", "Mitsubishi", "Nissan"]
Korean = ["Hyundai", "Kia", "Daewoo"]
Chinese = ["Geely", "Chery", "Hongqi", "Brilliance", "BYD"]
Australian = ["Honden"]


# tweet format should be dict
# list format should be dict
def vehicle_manufacturer_country(tweet_text, country_list):
    for brand in German:
        if brand in tweet_text:
            country_list["German"] = country_list["German"] + 1
    for brand in Italian:
        if brand in tweet_text:
            country_list["Italian"] = country_list["Italian"] + 1
    for brand in French:
        if brand in tweet_text:
            country_list["French"] = country_list["French"] + 1
    for brand in British:
        if brand in tweet_text:
            country_list["British"] = country_list["British"] + 1
    for brand in American:
        if brand in tweet_text:
            country_list["American"] = country_list["American"] + 1
    for brand in Japanese:
        if brand in tweet_text:
            country_list["Japanese"] = country_list["Japanese"] + 1
    for brand in Korean:
        if brand in tweet_text:
            country_list["Korean"] = country_list["Korean"] + 1
    for brand in Chinese:
        if brand in tweet_text:
            country_list["Chinese"] = country_list["Chinese"] + 1
    for brand in Australian:
        if brand in tweet_text:
            country_list["Australian"] = country_list["Australian"] + 1
    return country_list
