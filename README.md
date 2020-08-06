# MarvelApi
An easy library for sending requests to the Marvel Api!
Created by Alex Chung.

# Usage
Importing the class
```
from marvel import MarvelApi
```

Instantiating the object
```
PUBLIC_KEY = ""  # Put your public key here
PRIVATE_KEY = ""  # Put your private key here

_marvelObj = MarvelApi(PUBLIC_KEY, PRIVATE_KEY)
```

Sending a request and using the returned data (Json format)
```
# Here 'limit' and 'offset are used as the sample parameters
_resultJson = _marvelObj.request("https://gateway.marvel.com/v1/public/characters", {"limit": 5, "offset": 2})

print(_resultJson)
```

Another good test to see the request is working...
```
# Here 'limit' and 'offset are used as the sample parameters
_resultJson = _marvelObj.request("https://gateway.marvel.com/v1/public/characters", {"limit": 5, "offset": 2})

for _i in _resultJson['data']['results']:
    print(_i['name'])
```
