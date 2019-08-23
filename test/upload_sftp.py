# coding:utf8

import json
import os
import pysftp
import sys

progressDict={}
progressEveryPercent=10

for i in range(0,101):
    if i%progressEveryPercent==0:
        progressDict[str(i)]=""

def printProgressDecimal(x,y):
    if int(100*(int(x)/int(y))) % progressEveryPercent ==0 and progressDict[str(int(100*(int(x)/int(y))))]=="":
        print("{}% ({} Transfered(B)/ {} Total File Size(B))".format(str("%.2f" %(100*(int(x)/int(y)))),x,y))
        progressDict[str(int(100*(int(x)/int(y))))]="1"

with open(os.path.join(sys.path[0], "upload_sftp.json"), 'r') as f:
    config = json.load(f)

print(config)

localpath = sys.argv[1]

"""remotepath: the destination path on the SFTP server. 
Note that the filename should be included.
Only specifying a directory may result in an error."""
remotepath = sys.argv[2]

print(localpath)
print(remotepath)

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

srv = pysftp.Connection(host=config["host"], port=config["port"], username=config["username"],
                        password=config["password"], cnopts=cnopts)
srv.put(localpath, remotepath, callback=printProgressDecimal)
srv.close()
