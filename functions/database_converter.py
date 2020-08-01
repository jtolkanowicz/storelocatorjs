import json

#----------------------------------------------------------------------
if __name__ == "__main__":
    #file name location, file name default
    #if file name location exists use it, if not use default
    databaseFile = 'database.json'

    with open(databaseFile, 'r') as file:
        locations = json.load(file)

        locationsMap = dict()
        for location in locations:
            if location["category"] in locationsMap:
                locationsMap[location["category"]].append(location)
            else:
                locationsMap[location["category"]] = list()
                locationsMap[location["category"]].append(location)

    with open('location_map.json', 'x') as file:
        json.dump(locationsMap, file, indent=4)