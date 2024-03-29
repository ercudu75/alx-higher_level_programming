#!/usr/bin/python3
"""script that fetches URL"""
from requests import get


if __name__ == "__main__":
    response = get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
