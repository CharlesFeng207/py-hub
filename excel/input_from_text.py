# coding:utf-8
import sys

if __name__ == "__main__":
    path_src = sys.argv[1]
    print(path_src)
    with open(path_src, "r", encoding='utf-8') as f:
        s = f.read()
        outList = s.split("\n\n\n\n\n\n")
        print(len(outList))

    print("done!")




