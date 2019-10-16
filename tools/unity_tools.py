# coding:utf-8

import os
import sys
import json

with open(os.path.join(sys.path[0], "unity_tools.json"), 'r') as f:
    config = json.load(f)

print(config)




def print_and_run(cmd):
    print(cmd)
    return os.system(cmd)


def execute_unity(executeMethod):
    cmd = r"{0} -batchmode -nographics -projectPath {1} -executeMethod {2} -quit -logFile run_unity.log".format(
        config["unityPath"], config["projectPath"], executeMethod)
    return print_and_run(cmd)


def svn_update():
    cmd = r"svn update {0} --username {1} --password {2} --accept tc".format(
        config["projectPath"], config["svn_username"], config["svn_password"])
    return print_and_run(cmd)


def commitAssetBundles():
    print_and_run(r"svn add {0}\*".format(config["assetBundlesPath"]))
    return print_and_run(r"svn commit -m \"AssetBundles\" {0} --username {1} --password {2}".
                         format(config["assetBundlesPath"], config["svn_username"], config["svn_password"]))


if __name__ == "__main__":
    # print(svn_update())
    # print(commitAssetBundles())
    # print(execute_unity("Editor.EditorTest.TestJson"))
    pass
