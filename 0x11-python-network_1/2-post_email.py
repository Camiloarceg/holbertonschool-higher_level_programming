#!/usr/bin/python3
""" Write a Python script that fetches """
import urllib.request
from sys import argv


if __name__ == "__main__":
    data = urllib.parse.urlencode({'email': argv[2]})
    data = data.encode('utf-8')
    with urllib.request.urlopen(argv[1], data) as response:
        html = response.read()
    html = html.decode('utf-8')
    print(html)
