from ConfigHelper import Config

config = Config()
config.setConfig("Version", "0.0.1")
config.setConfig("isTemporary", 0)
config.setConfig("isUserMode", 1)

print(config.isTemporary) # 0
print(config.Version) # 0.0.1

print(config.toJSON())
"""
{
        "Version": "0.0.1",
        "isTemporary": 0,
        "isUserMode": 1
}
"""

class Test:
    def __init__(self):
        self.name = "Donggun LEE"
        self.age = 24
    
    def __str__(self):
        return "name : {}, age : {}".format(self.name, self.age)

test = Test()
print(test) # name : Donggun LEE, age : 24
config.setConfig("name", "LEE Donggun")
config.toClass(test)
print(test) # name : LEE Donggun, age : 24
try:
    print(test.Version)
except Exception as e:
    print(e) # 'Test' object has no attribute 'Version'

print(config.Version) # 0.0.1

print(config.toDict()['Version']) # 0.0.1

config.toFile("d:/a/b/c/d/e/f/config.json")
config2 = Config("d:/a/b/c/d/e/f/config.json")
print(config2)
"""
{
        "Version": "0.0.1",
        "isTemporary": 0,
        "isUserMode": 1,
        "name": "LEE Donggun"
}
"""