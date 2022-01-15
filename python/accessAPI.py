import requests
import sys


response = requests.get("http://10.40.3.171:51400/?message="+sys.argv[1])
response.encoding = response.apparent_encoding
print(response.text.encode("utf_8"))