# import requests

# req = requests.get("https://google.com")
# print(req.status_code)

import requests
import time
while True:
    
    req = requests.get("https://google.com")
    print(req.status_code)
    if req.status_code != 200:
        pass
    time.sleep(10)
