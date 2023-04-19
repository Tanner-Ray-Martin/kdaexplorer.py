from constants import KDA_WS_URL, CONNECT_MSG, SUBSCIRIBE_MSGS


import json


url = "https://backend-dev.euclabs.net/kadena-indexer/v1/recent-blocks?pageId=0&pageSize=2"

import requests


sleep = 2

running = True

times = 20

r = requests.get(url)

kadena = r.json()

from objects import Height

heights = [Height(height) for height in kadena]

for height in heights:
    print(height.value)
    for block in height.blocks:
        print(block.chain.value)
