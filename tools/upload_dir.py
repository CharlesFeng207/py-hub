# coding:utf8

import json
import os
import pysftp
import sys

progressDict = {}
progressEveryPercent = 10

for i in range(0, 101):
    if i % progressEveryPercent == 0:
        progressDict[str(i)] = ""


def printProgressDecimal(x, y):
    if int(100*(int(x)/int(y))) % progressEveryPercent == 0 and progressDict[str(int(100*(int(x)/int(y))))] == "":
        print("{}% ({} Transfered(B)/ {} Total File Size(B))".format(str("%.2f" %
                                                                         (100*(int(x)/int(y)))), x, y))
        progressDict[str(int(100*(int(x)/int(y))))] = "1"


with open(os.path.join(sys.path[0], "upload_dir.json"), 'r') as f:
    config = json.load(f)

print(config)

localdir = config["localdir"]
if not os.path.isdir(localdir):
    raise Exception(f"{localdir} is not dir!")

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None
srv = pysftp.Connection(host=config["host"], port=config["port"], username=config["username"],
                        password=config["password"], cnopts=cnopts)

os.chdir(localdir)
files = os.listdir(localdir)
for i, filename in enumerate(files):
    if filename.endswith(".part"):
        continue
    remotepath = config["remotedir"] + "/" + filename
    print("process {}, {} / {}".format(filename, i+1, len(files)))
    print(f"{filename} -> {remotepath} ...")
    srv.put(filename, remotepath, callback=printProgressDecimal)
    os.remove(filename)
    print(f"{filename} deleted!")

srv.close()