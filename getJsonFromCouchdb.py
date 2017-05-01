import json

# use curl first to get all docs
# curl -X GET sourcead:iamfine@115.146.93.79:5984/twitter/_all_docs?include_docs\=true >
# ./statusdoc.json

# curl may not work in computers otherwise the NeCTAR
f = open('statusdoc.json','r',encoding='utf8')
jsdoc = json.loads(f.read())
f.close()

js = []
for row in jsdoc['rows']:
    js.extend(row['doc']['status'])
print(len(js))

jsstr = json.dumps(js)
f = open('status.json','w',encoding='utf8')
f.write(jsstr)
f.close()
a = 1
