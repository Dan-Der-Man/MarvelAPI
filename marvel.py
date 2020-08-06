"""
Simple Marvel API request library
by Alex Chung

https://github.com/lick-chickens/MarvelApi
"""

import json
from time import time
import requests
import hashlib

from requests.auth import HTTPProxyAuth


class MarvelApi:
    """Marvel API request library"""

    PUBLIC_KEY = "No key set yet"
    PRIVATE_KEY = "No key set yet"

    PAYLOAD = dict()  # {"ts":0, "hash":""}

    PROXY_SETTINGS = None
    PROXY_AUTH = None

    # Constructor
    def __init__(self, pubkey, privkey):
        """Pass in your PUBLIC_KEY and PRIVATE_KEY as strings"""

        # Prep keys
        self.PUBLIC_KEY = pubkey
        self.PRIVATE_KEY = privkey

        # Prep security
        # https://developer.marvel.com/documentation/authorization
        _timestamp = int(time())
        _input_string = str(_timestamp) + privkey + pubkey
        _hash = hashlib.md5(_input_string.encode("utf-8")).hexdigest()  # Encodes string as utf-8 bytes
        self.PAYLOAD['ts'] = _timestamp
        self.PAYLOAD['hash'] = _hash

    def request(self, gateway, params):
        """Send a request, gateway as string, params as dict() | eg. {"offset":100}"""

        # Send request
        _params = {"ts": self.PAYLOAD['ts'], "apikey": self.PUBLIC_KEY, "hash": self.PAYLOAD['hash'], **params}
        _response = requests.get(gateway, params=_params, proxies=self.PROXY_SETTINGS, auth=self.PROXY_AUTH)

        # Convert to Json
        return json.loads(_response.content.decode('utf-8'))  # Decode, opposite of encode above

    def proxyconfig(self, protocol, address, port, username=None, password=None):
        self.PROXY_SETTINGS = {protocol: protocol + "://" + address + ":" + port}  # {"http": "http://proxy2.eq.edu.au:80"}
        self.PROXY_AUTH = (None, HTTPProxyAuth(username, password))[(username and password) is not None]
