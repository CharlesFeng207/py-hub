#!/usr/local/bin/python3

import sys
import os

a = " ".join(sys.argv[1:])
cmd = f"youtube-dl {a} --proxy socks5://127.0.0.1:1080 --write-auto-sub --sub-lang en --convert-subs srt"
# print(cmd)
os.system(cmd)
