import configparser

def update_config(value):
    config = configparser.ConfigParser()
    config.read('config.ini')
    config["KEYS"]["API_KEY"] = value
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

key = input("Enter your api key : ")
update_config(key)
print("api key saved...")
