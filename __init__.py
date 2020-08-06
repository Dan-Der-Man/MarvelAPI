from marvel import MarvelApi

PUBLIC_KEY = "17f0f19*****57315a"
PRIVATE_KEY = "36655c186*****d5bd91522e"

# Instantiate object
_marvelObj = MarvelApi(PUBLIC_KEY, PRIVATE_KEY)

# Set proxy (with authentication)
# _marvelObj.proxyconfig("http", "proxy2.eq.edu.au", "80", "MY_USERNAME", "MY_PASSWORD")
# _marvelObj.proxyconfig("http", "proxy2.eq.edu.au", "80")

# Use object's 'request' method which returns JSON
# https://developer.marvel.com/docs#!/public/getCreatorCollection_get_0
_resultJson = _marvelObj.request("https://gateway.marvel.com/v1/public/characters", {"limit": 5, "offset": 1})

# Print full result
print(_resultJson)

# Parse and print JSON
# for _i in _resultJson['data']['results']:
    # print(_i['name'])
