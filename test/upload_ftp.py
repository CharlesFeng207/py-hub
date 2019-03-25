# coding:utf8

import ftplib
import sys

fromPath = sys.argv[1]
toPath = sys.argv[2]

session = ftplib.FTP('192.168.0.200','Anonymous')
session.debugging = True
session.encoding = "gbk"

file = open(fromPath,'rb')
# file to send

session.storbinary('STOR {}'.format(toPath), file)     # send the file
file.close()                                    # close file and FTP
session.quit()