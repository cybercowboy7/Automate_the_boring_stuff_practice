import xmltodict as xd

with open("xml_test") as file:
    xml_data = file.read()      # reads the xml file contents into xml_data

xml_dict = xd.parse(xml_data)       # parses the xml file into a dictionary that python can work with

print(xml_dict)

xml_dict["interface"]["ipv4"]["address"]["ip"] = "192.168.55.3"     # changes the value of the child key "ip"

print(xd.unparse(xml_dict))     # unparses the file and prints the edited key

with open("xml_test", "w") as file:
    file.write(xd.unparse(xml_dict, pretty=True))       # writes our previous changes to the file

with open("xml_test") as file:
    xml_data2 = file.read()     # Opens file so we can view the new changes in the print command

print(xml_data2)