import socket
from uuid import uuid4

def make_unique(file, files):
    while file in files:
        file = f"{str(uuid4())[:9]}{file}"
    return file

def my_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP
