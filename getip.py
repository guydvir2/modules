import socket
import urllib.request
import time


def get_ip():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            internal_ip = s.getsockname()[0]
            s.close()
            external_ip = urllib.request.urlopen('http://ident.me').read().decode('utf8')
            return internal_ip, external_ip

        except OSError:
            #internal_ip ='0.0.0.0'
            #external_ip = '0.0.0.0'
            time.sleep(5)
  
