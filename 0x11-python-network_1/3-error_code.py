#!/usr/bin/python3
""" Write a Python script that fetches """
from urllib.error import HTTPError
from urllib.request import urlopen
from sys import argv


if __name__ == "__main__":
    try:
        with urlopen(argv[1]) as response:
            html = response.read()
        html = html.decode('utf-8')
        print(html)
    except HTTPError as error:
        print("Error code: {}".format(error.status))
