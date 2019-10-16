# coding:utf-8

from os import system
import unity_tools

tasks = []

tasks.append(unity_tools.svn_update)
tasks.append(lambda : unity_tools.execute_unity("Editor.EditorTest.TestJson"))
tasks.append(unity_tools.commitAssetBundles)

for i, t in enumerate(tasks):
    while t() != 0:
        input(f"task {i} execute failed, press anykey to retry!")

input("done!")