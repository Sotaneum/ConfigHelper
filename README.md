# ConfigMaster
Can use it to save or recall preferences from Python.
 - Copyright (c) 2019 Lee Dong-gun
 - Homepage : http://infolab.kunsan.ac.kr
 - How to install
  - pip install "http://duration.digimoon.net/pip/configmaster.whl"

 - Functions
 ```python
    config = ConfigMaster(data:dict)
    config = ConfigMaster(path:str) # URL is not supported.

    # Returns the values.
    def getConfig(key:str):
        return Value

    # Modify or add new values. 
    def setConfig(key:str, value:object):
        return None

    # Put a value in Class.
    def toClass(cls:object):
        return Object

    # Return as "Dictionary".
    def toDict():
        return Dictionary

    # Return as "JSON".
    def toJSON():
        return String(=JSON)

    # Return as "File".
    def toFile(path:string):
        return file
 ```

 - How to use

```python
from ConfigMaster import Config
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
```