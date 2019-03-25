import os
import sys

cmd_file_name = sys.argv[1]

with open("{}.txt".format(cmd_file_name), "r") as f:
    cmd = f.readline()

    print(cmd)

    count = 1000
    for i in range(count):
        os.system(cmd)
        print("{}/{}".format(i, count))

    print("Done!")


