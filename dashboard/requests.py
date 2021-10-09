# importing the requests library
import requests

def sendsms(text, number):
    # api-endpoint
    URL = "https://api.smsglobal.com/http-api.php"
    number  = str(number)
    # defining a params dict for the parameters to be sent to the API
    PARAMS = {'action':'sendsms',
            'user':'1bfz48ju',
            'password':'uVh9zc5Z',
            'from': 'Pizza.ae',
            'to': '971' + number,
            'text': text,}
    # sending get request and saving the response as response object
    res = requests.get(url = URL, params = PARAMS)
    return res