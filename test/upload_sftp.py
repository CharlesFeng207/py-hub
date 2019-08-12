# coding:utf8

import json
import os
import pysftp
import sys

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

srv = pysftp.Connection(host=config["host"], username=config["username"], password=config["password"], cnopts=cnopts)
srv.put(localpath, remotepath)
srv.close()