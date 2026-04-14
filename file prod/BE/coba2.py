import json
nametoadd  = "du"

with open('namedb.json','r') as namedb:
    
    namedb_dict = json.load(namedb)
    if nametoadd not in namedb_dict:
        namedb_dict[nametoadd] = 1
    else:
        print("has already added")

with open('namedb.json','w') as namedb:
    json.dump(namedb_dict,namedb)