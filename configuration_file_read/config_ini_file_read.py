import configparser

config = configparser.ConfigParser()
print(config.read('config.ini'))
print(config.sections())

for section in config.sections():
    print(section)

print(config.get('mysql','host'))
print(config.get('mysql','passwd'))

print(config.get('other','preprocessing_queue'))
print(config.get('other','use_anonymous'))
