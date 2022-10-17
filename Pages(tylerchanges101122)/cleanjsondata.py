import json
import datetime



def cleanjson():
    try:
        jsonpath = r"/home/infinitysystem/Desktop/AssayProfiles.json"

        obj  = json.load(open(jsonpath))

        def check_if_more_than_seven_days(x):
            d = datetime.datetime.strptime(x, "%Y-%m-%d") # Add .date() if hour doesn't matter

            now = datetime.datetime.now()                 # Add .date() if hour doesn't matter

            return (now - d).days > 7



        def recursive_items(dictionary):
            for key, value in dictionary.items():
                if type(value) is dict:
                    yield from recursive_items(value)
                else:
                    yield (key, value)

        toRemove = []
        for key in obj.keys():
            dict = obj[key]
            for key2, value2 in recursive_items(dict):
                if key2 == 'enddate' and value2 != '---':
                    lastconnection = datetime.datetime.strptime(value2, "%Y-%m-%d").strftime("%Y-%m-%d")
                    if check_if_more_than_seven_days(lastconnection):
                        print("Found")
                        print(value2)
                        toRemove.append(key)
        print(toRemove)
        for x in toRemove:
            obj.pop(x)
        open(jsonpath, "w").write(
            json.dumps(obj, sort_keys=True, indent=4, separators=(',', ': '))
        )
    except:
        print('clean json data function failed')






    #if check_if_more_than_seven_days("2018-04-18"):
    #   print('Do something')  # This will not print

    #if check_if_more_than_seven_days("2018-04-14"): 
    #   print('Do something')  # This will print

    

