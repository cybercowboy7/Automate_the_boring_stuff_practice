import json

with open("test.json") as data:
    json_data = data.read() # Takes the raw JSON file and turns it into a string

json_dictionary = json.loads(json_data) # Takes the string and uses the load string json method to
                                        # convert the string to a dictionary

print(json_dictionary)


json_dictionary["Router"]["hostname"] = "KraftRouter"   #Changes the value of the hostname key to "KraftRouter"

print(json_dictionary)

with open("test.json", "w") as data:        # Open the json file in write mode
    json.dump(json_dictionary, data, indent=4)      # Dumps contents of the json_dictionary into the data file

with open("test.json") as data:
    json_data = data.read()
    json_dictionary2 = json.loads(json_data)

print(json_dictionary2)