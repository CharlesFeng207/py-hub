# coding=utf-8
import socket
import hashlib
import json
import os
import traceback

if __name__ == "__main__":
    secret = "xEdyaR+b0BE4yK3dy5yC0JDe7b8GV2lJ5dHl05cChFVEcSl2LI+EkJEKNblXK3Mi"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('0.0.0.0', 32979))
    print("bind udp on port:32979 ...")

    while True:
        try:
            data, addr = s.recvfrom(1024000)
            info = data.decode(encoding="utf-8")
            msg = json.loads(info)

            if msg["loginStr"] is not None:
                print("{} from {}".format(info, addr))
                signature = hashlib.md5((msg["loginStr"] + secret).encode('utf8')).hexdigest()
                s.sendto(signature.encode('utf8'), addr)

            if msg["log"] is not None:
                folder = os.path.join("debugconsole_logs", msg["appName"], msg["deviceInfo"])
                if not os.path.exists(folder):
                    os.makedirs(folder)

                p = os.path.join(folder, msg["launchTime"] + '.log')

                if not os.path.exists(p):
                    print("create " + p)

                f = open(p, 'a+')
                f.write(msg["log"] + "\n")
                f.close()
        except Exception as e:
            print(e)
            print(traceback.format_exc())
            pass


