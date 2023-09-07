import requests
from jsonpath import jsonpath
from config.config import local_config

def Token():
    session = requests.session()
    data = {"username": local_config.Username,
            "password": local_config.Passwd,
            "anban_password": local_config.Anban_Passwd}
    headers = {"Content-Type": "application/json"}
    res = session.post('{}api/user/login'.format(local_config.URL), json=data, headers=headers)
    token = 'Token ' + jsonpath(res.json(), '$.data.AuthToken')[0]
    return token
