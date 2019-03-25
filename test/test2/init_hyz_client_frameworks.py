# coding:utf8

import sys
from os import path
import os

print("sys.path:", sys.path)

tasks = [("GPCommon", "http://192.168.0.9/FengChao/GPCommon.git", "master"),
         ("GPAssetContainer", "http://192.168.0.9/FengChao/GPAssetContainer.git", "master"),
         ("GPVersionFlow", "http://192.168.0.9/FengChao/GPVersionFlow.git", "master"),
         ("GPQuickBuild", "http://192.168.0.9/FengChao/GPQuickBuild.git", "master"),
         ("GPDebugConsole", "http://192.168.0.9/FengChao/GPDebugConsole.git", "master")]

t = sys.path[0]
startFolder = t

while not path.exists(path.join(t, ".git")):
    p = path.dirname(t)
    if t == p:
        input("没找到git项目")
        quit(-1)
    t = p

print(t)

os.chdir(t)

for task in tasks:
    prefix = path.relpath(path.join(startFolder, task[0]), start=t)
    if path.exists(prefix):
        print(prefix + " 已经存在，忽略")
    else:
        r = 0
        prefix = prefix.replace("\\", "/")
        cmd = "git subtree add --prefix={} {} {}".format(prefix, task[1], task[2])
        print(cmd)
        r = os.system(cmd)
        if r != 0:
            input(task[0] + " 拉取失败")
            quit(-1)

input("成功!")
