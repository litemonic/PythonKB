myDict = {1:"a",2:"b",3:"c",4:"d"}
keys = list(myDict.keys())
i = 0
while i <= len(myDict):
    key = keys[i]
    if key % 2 == 0:
        del myDict[key]
    i+=1
print(myDict)