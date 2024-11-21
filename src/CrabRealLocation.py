import requests

link ="https://api-zero.livere.com/v1/comments/list?callback=jQuery112407916776725405603_1732201378464&limit=10&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&code=&_=1732201378466"
headers={
    "User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Mobile Safari/537.36"
}

r=requests.get(link,headers=headers)
print(r.text)

#使用json库解析数据
import json
json_string=r.text
json_string=json_string[json_string.find('{'):-2]
json_data=json.loads(json_string)
commit_list=json_data['results']['parents']

for eachone in commit_list:
    print(eachone['content'])