# coding:utf8

import json
import os
import pysftp
import sys
from time import sleep


def run():
    print("run...")
    srv = None
    os.chdir(localdir)
    files = os.listdir(localdir)
    for filename in files:
        if filename == "url.txt" or any(map(lambda x: filename.endswith(x), [".vtt", ".ytdl", ".m4a", ".part", ".DS_Store"])):
            continue

        if len(filename.split(".")) >= 3:
            if filename.split(".")[-2].startswith("f") or filename.split(".")[-2] == "temp":
                print(f"{filename} skiped")
                continue

        if not srv:
            cnopts = pysftp.CnOpts()
            cnopts.hostkeys = None
            srv = pysftp.Connection(host=config["host"], port=config["port"], username=config["username"],
                                    password=config["password"], cnopts=cnopts)

        remotepath = config["remotedir"] + "/" + filename
        print(f"process {filename}")
        print(f"{filename} -> {remotepath} ...")
        srv.put(filename, remotepath, callback=printProgressDecimal)
        os.remove(filename)
        print(f"{filename} deleted!")
        pass
    if srv:
        srv.close()
        srv = None


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


config_path = None


for i, a in enumerate(sys.argv):
    if a == "-c":
        config_path = sys.argv[i + 1]
        break
    pass


if not config_path:
    config_path = os.path.join(sys.path[0], "upload_dir.json")
    pass

with open(config_path, 'r') as f:
    config = json.load(f)

print(config)

localdir = config["localdir"]
if not os.path.isdir(localdir):
    raise Exception(f"{localdir} is not dir!")

if any(map(lambda x: x == "-t", sys.argv)):
    while True:
        run()
        sleep(5)
        pass
else:
    run()
    pass
