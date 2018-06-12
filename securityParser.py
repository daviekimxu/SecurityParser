import xml.etree.ElementTree as ET
tree = ET.parse('security.xml')
root = tree.getroot()

with open("log.txt", "w") as file:
    file.write("username violation\n")
    users = root.find("users")
    for user_element in users.iter("user"):

        userString = user_element.find("username").text
        passwordString = user_element.find("password").text
        propValueString = user_element.findall(".//propValue")

        if userString.startswith("AM6J"):
            print (userString)

            file.write(userString + "\n")

        if passwordString != (None):
            if passwordString.startswith("AM6J"):
                print (userString + " " + passwordString)

                file.write(userString + " " + passwordString + "\n")


        for k in propValueString:
            if k.text.startswith("AM6J"):
                print (userString + " " + k.text)

                file.write(userString + " " + k.text + "\n")
