#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status
"""
import requests
from sys import argv


if __name__ == "__main__":
    response = requests.get("{}".format(argv[1])).headers['X-Request-Id']
    print(response)
