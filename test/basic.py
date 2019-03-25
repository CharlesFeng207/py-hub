import sys
import platform
import locale

print("__name__:", __name__)
print("sys.argv:", sys.argv)
print("sys.path:", sys.path)
print("platform.platform()", platform.platform())
print("sys.getdefaultencoding ", sys.getdefaultencoding(), locale.getdefaultlocale())

s = '漢  \n χαν  хан \ud83d\ude2c\ud83d\ude2c'

# print("print: " + s)
# print('unicode: ' + s.encode('unicode-escape').decode('utf-8'))

# u = s.encode('unicode-escape').decode('utf-8')
print('解回字符串: ' + s.encode("utf-8", "ignore").decode('utf-8'))

with open('test.txt', "w+", encoding="utf-8", errors="ignore") as out_file:
    out_file.write(s)


def test_func(name):
    print(name)


if __name__ == "__main__":
    test_func("main")


