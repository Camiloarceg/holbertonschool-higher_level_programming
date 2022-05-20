#!/usr/bin/python3
""" script that fetches https://intranet.hbtn.io/status
"""
import requests


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    response = requests.get("{}".format(url)).headers['X-Request-Id']
    print(response)
