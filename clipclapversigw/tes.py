import json
c = json.dumps({"code":"OK","data":{"upgrade":True,"evolution":False,"bubbles":[{"id":"5ed79390bb16ec7169a2546d","userId":"8423877","type":"PEARL","from":None},{"id":"5ed79390bb16ec7b34a2546e","userId":"8423877","type":"PEARL","from":None},{"id":"5ed79390bb16ec1fbca2546f","userId":"8423877","type":"PEARL","from":None},{"id":"5ed79390bb16ecdb77a25470","userId":"8423877","type":"PEARL","from":None}],"freeFoodCount":12,"cost":1,"currency":"FREE","fish":{"id":"5ed7936f8c3ff981230c893e","userId":"8423877","name":"Clownfish","key":"xcy","level":2,"bodyFactor":0.66,"price":9,"exp":0,"remainFood":3,"sold":False,"feedCount":2,"specialEffect":"SHINING","weight":404,"status":"FEEDABLE","upgradeExp":2,"feedingTime":33521,"race":"xsyx","currency":"GOLD","giftFish":False,"nextFeedingTime":0}}})
a = json.dumps({"code":"OK","data":{"upgrade":False,"evolution":False,"bubbles":[],"freeFoodCount":2,"cost":1,"currency":"FREE","fish":{"id":"5ed5e330c7dc38ea088e22d9","userId":"7930164","name":"Tropical fish","key":"rdy","level":3,"bodyFactor":0.7260000000000001,"price":23,"exp":2,"remainFood":2,"sold":False,"feedCount":8,"specialEffect":"SHINING","weight":315,"status":"FEEDABLE","upgradeExp":3,"feedingTime":122256028,"race":"gsyx","currency":"GOLD","giftFish":False,"nextFeedingTime":0}}})
b = json.loads(c)
bubles = b['data']['bubbles']
if bubles:
	for bb in bubles:
		print(bb)
else:print('tidak ada bubles')