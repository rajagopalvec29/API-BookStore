import requests
from Utilities.resources import *
from TestCases.PayLoads import *


posturl = getConfig()['API']['endpoint']+ ApiResources.addbook
query = 'select * from Books'
print(posturl)
print(DBAddBookData(query))
res = requests.post(posturl,json =  DBAddBookData(query) )
# res = requests.post(posturl,json = Addbook('fgr45656') )
json_res = res.json()
fileid= json_res['ID']
print(json_res)
print("Status code : ",res.status_code)
print("Order ID :", fileid)


print("DELETE RESQUEST")
delurl = getConfig()['API']['endpoint']+ApiResources.deletebook
res1 = requests.post(delurl,json={'ID':fileid})
print("Status code : ",res1.status_code)
print(res1.json())