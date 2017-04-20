# tweet format should be dict
# list format should be dict


def beer_brand(tweet_text, beer_list):
    if "Snow" in tweet_text:
        beer_list["Snow"] = beer_list["Snow"] + 1
    if "Tsingtao" in tweet_text:
        beer_list["Tsingtao"] = beer_list["Tsingtao"] + 1
    if "Bud Light" in tweet_text:
        beer_list["Bud Light"] = beer_list["Bud Light"] + 1
    if "Budweiser" in tweet_text:
        beer_list["Budweiser"] = beer_list["Budweiser"] + 1
    if "Skol" in tweet_text:
        beer_list["Skol"] = beer_list["Skol"] + 1
    if "Yanjing" in tweet_text:
        beer_list["Yanjing"] = beer_list["Yanjing"] + 1
    if "Heineken" in tweet_text:
        beer_list["Heineken"] = beer_list["Heineken"] + 1
    if "Harbin" in tweet_text:
        beer_list["Harbin"] = beer_list["Harbin"] + 1
    if "Brahma" in tweet_text:
        beer_list["Brahma"] = beer_list["Brahma"] + 1
    if "Coors Light" in tweet_text:
        beer_list["Coors Light"] = beer_list["Coors Light"] + 1
    if "Victoria Bitter" in tweet_text or "VB" in tweet_text:
        beer_list["Victoria Bitter"] = beer_list["Victoria Bitter"] + 1
    if " XXXX Gold" in tweet_text:
        beer_list[" XXXX Gold"] = beer_list[" XXXX Gold"] + 1
    if "Carlton Premium Dry" in tweet_text:
        beer_list["Carlton Premium Dry"] = beer_list["Carlton Premium Dry"] + 1
    if "Carlton Draught" in tweet_text:
        beer_list["Carlton Draught"] = beer_list["Carlton Draught"] + 1
    if "Corona Extra" in tweet_text:
        beer_list["Corona Extra"] = beer_list["Corona Extra"] + 1
    if "Toohey’s New " in tweet_text:
        beer_list["Toohey’s New "] = beer_list["Toohey’s New "] + 1
    if "Toohey’s Extra Dry" in tweet_text:
        beer_list["Toohey’s Extra Dry"] = beer_list["Toohey’s Extra Dry"] + 1
    if "Carlton Mid Strength" in tweet_text:
        beer_list["Carlton Mid Strength"] = beer_list["Carlton Mid Strength"] + 1
    if "Crown Lager" in tweet_text:
        beer_list["Crown Lager"] = beer_list["Crown Lager"] + 1
    if "Oettinger" in tweet_text:
        beer_list["Oettinger"] = beer_list["Oettinger"] + 1
    return beer_list

# def beer_brand(tweet, beer_list):
#     if "Snow" in tweet["text"]:
#         beer_list["Snow"] = beer_list["Snow"] + 1
#     if "Tsingtao" in tweet["text"]:
#         beer_list["Tsingtao"] = beer_list["Tsingtao"] + 1
#     if "Bud Light" in tweet["text"]:
#         beer_list["Bud Light"] = beer_list["Bud Light"] + 1
#     if "Budweiser" in tweet["text"]:
#         beer_list["Budweiser"] = beer_list["Budweiser"] + 1
#     if "Skol" in tweet["text"]:
#         beer_list["Skol"] = beer_list["Skol"] + 1
#     if "Yanjing" in tweet["text"]:
#         beer_list["Yanjing"] = beer_list["Yanjing"] + 1
#     if "Heineken" in tweet["text"]:
#         beer_list["Heineken"] = beer_list["Heineken"] + 1
#     if "Harbin" in tweet["text"]:
#         beer_list["Harbin"] = beer_list["Harbin"] + 1
#     if "Brahma" in tweet["text"]:
#         beer_list["Brahma"] = beer_list["Brahma"] + 1
#     if "Coors Light" in tweet["text"]:
#         beer_list["Coors Light"] = beer_list["Coors Light"] + 1
#     if "Victoria Bitter" in tweet["text"] or "VB" in tweet["text"]:
#         beer_list["Victoria Bitter"] = beer_list["Victoria Bitter"] + 1
#     if " XXXX Gold" in tweet["text"]:
#         beer_list[" XXXX Gold"] = beer_list[" XXXX Gold"] + 1
#     if "Carlton Premium Dry" in tweet["text"]:
#         beer_list["Carlton Premium Dry"] = beer_list["Carlton Premium Dry"] + 1
#     if "Carlton Draught" in tweet["text"]:
#         beer_list["Carlton Draught"] = beer_list["Carlton Draught"] + 1
#     if "Corona Extra" in tweet["text"]:
#         beer_list["Corona Extra"] = beer_list["Corona Extra"] + 1
#     if "Toohey’s New " in tweet["text"]:
#         beer_list["Toohey’s New "] = beer_list["Toohey’s New "] + 1
#     if "Toohey’s Extra Dry" in tweet["text"]:
#         beer_list["Toohey’s Extra Dry"] = beer_list["Toohey’s Extra Dry"] + 1
#     if "Carlton Mid Strength" in tweet["text"]:
#         beer_list["Carlton Mid Strength"] = beer_list["Carlton Mid Strength"] + 1
#     if "Crown Lager" in tweet["text"]:
#         beer_list["Crown Lager"] = beer_list["Crown Lager"] + 1
#     if "Oettinger" in tweet["text"]:
#         beer_list["Oettinger"] = beer_list["Oettinger"] + 1
#     return beer_list