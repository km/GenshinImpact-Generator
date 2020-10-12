import json
import requests

def createAcc(username, password):
    success = False
    payload = "is_crypto=false&not_login=0&username="+username+"&password="+password
    headers = {'Content-Type':'application/x-www-form-urlencoded'}
    req = requests.session()
    req.headers.update(headers)
    req1 = req.post("https://webapi-os.account.mihoyo.com/Api/regist_by_account", data=payload)
    try:
      if(json.loads(req1.text)["data"]['msg'] == "Success"):
       success = True
    except:
        print("error")
    return success    
ignlist = open("igns.txt","r").readlines()
password = input("Type password: ")
output = open('output.txt', 'w')
created = []
for x in ignlist:
    status = createAcc(x.replace("\n",""), password)
    account = x.replace("\n","") + ":" + password
    if status == True:
        print(account)
        output.write(account+"\n")
