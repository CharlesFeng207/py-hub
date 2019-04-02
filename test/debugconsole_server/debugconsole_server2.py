# coding=utf-8
import socket
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def check_key_pairs():
    message = b"encrypted data"
    test_signature = private_key.sign(message,
                                      padding.PKCS1v15(),
                                      hashes.SHA256())
    try:
        public_key.verify(
            test_signature,
            message,
            padding.PKCS1v15(),
            hashes.SHA256())
    except:
        print("key pairs check failed")
        raise
    print("key pairs check success")


if __name__ == "__main__":
    private_key_file = open("rsa_private_key.pem", "rb")
    public_key_file = open("rsa_public_key.pem", "rb")

    private_key = serialization.load_pem_private_key(
        private_key_file.read(),
        password=None,
        backend=default_backend()
    )

    public_key = serialization.load_pem_public_key(
        public_key_file.read(),
        backend=default_backend()
    )

    public_key_file.close()
    private_key_file.close()

    check_key_pairs()

    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    s.bind(('0.0.0.0', 32978))
    print("bind udp on port:32978 ...")

    while True:
        data, addr = s.recvfrom(1024)
        info = data.decode(encoding="utf-8")
        print("Receive from {} {}".format(info, addr))
        signature = private_key.sign(data, padding.PKCS1v15(), hashes.SHA256())
        s.sendto(signature, addr)
