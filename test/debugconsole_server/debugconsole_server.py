# coding=utf-8
import socket
import hashlib


if __name__ == "__main__":
    secret = "xEdyaR+b0BE4yK3dy5yC0JDe7b8GV2lJ5dHl05cChFVEcSl2LI+EkJEKNblXK3Mi"
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('0.0.0.0', 32979))
    print("bind udp on port:32979 ...")

    while True:
        data, addr = s.recvfrom(1024)
        info = data.decode(encoding="utf-8")
        print("Receive from {} {}".format(info, addr))
        signature = hashlib.md5((info + secret).encode('utf8')).hexdigest()
        s.sendto(signature.encode('utf8'), addr)
