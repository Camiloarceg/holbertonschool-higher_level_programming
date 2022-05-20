#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status
"""
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.post(argv[1], {'email': argv[2]})
    print(response.text)
