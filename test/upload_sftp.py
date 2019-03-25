#coding:utf8

import pysftp, sys

print(sys.argv)

host = sys.argv[1]
fromPath = sys.argv[2]
toPath = sys.argv[3]
password = sys.argv[4]

cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

srv = pysftp.Connection(host=host, username="root", password=password, cnopts=cnopts)
srv.put(fromPath, toPath)
srv.close()
