#!/usr/bin/python3
"""
script that fetches https://intranet.hbtn.io/status
"""
import requests
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(argv[1], argv[2]))
    json_ditc = response.json()
    print(json_ditc.get("id"))
