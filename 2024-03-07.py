import socket
import requests
import re


print(socket.gethostname())
in_addr = socket.gethostbyname(socket.gethostname())
in_adr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
in_adr.connect(("www.google.com", 443))

print(in_addr, in_adr.getsockname()[0])

req = requests.get("http://ipconfig.kr")
out_addr = re.search(r'IP Address : (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[1] #request.get으로 IP address : xxx.xxx.xxx.xxx 을 찾음
print(out_addr)