#!/usr/bin/python3
"""script that fetches URL"""
from requests import get


if __name__ == "__main__":
    response = get("https://alx-intranet.hbtn.io/status")
    print("Body response:")
    print(f"\t- type: {type(response.text)}")
    print(f"\t- content: {response.text}")
