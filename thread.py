import threading
import time
import requests

def makerequest(name):
    while True:
        r = requests.get("https://ail-ohm-accp.apps.ap-3a.mendixcloud.com/p/login")
        print("Response code from thread {}:{}".format(name,str(r.status_code)))
if __name__ == "__main__":
    threads = 4
    while threads >= 1:
        print("thread starting from {}".format(threads))
        t = threading.Thread(target=makerequest,args=(threads,))
        threads-=1
        t.start()
        
    