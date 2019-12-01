# coding:utf8

import sys
from os import path
import os

print("sys.path:", sys.path)

tasks = [("GPCommon", "http://192.168.0.9/FengChao/GPCommon.git", "master"),
         ("GPAssetContainer", "http://192.168.0.9/FengChao/GPAssetContainer.git", "master"),
         ("GPVersionFlow", "http://192.168.0.9/FengChao/GPVersionFlow.git", "master"),
         ("GPQuickBuild", "http://192.168.0.9/FengChao/GPQuickBuild.git", "master"),
         ("GPDebugConsole", "http://192.168.0.9/FengChao/GPDebugConsole.git", "master"),
		 ("GPPlatform ", "http://192.168.0.9/FengChao/GPPlatform.git", "master")]

t = sys.path[0]

for task in tasks:
	os.chdir(path.join(t, task[0]))
	r = os.system("git pull")

input("成功!")