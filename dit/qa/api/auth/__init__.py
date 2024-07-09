import json
from typing import Any, Tuple

import requests


def auth(login: str, password: str) -> Tuple[int, Any]:
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }

    response = requests.post(
        'https://tsoo.mos.ru/api/token-auth/',
        headers=headers,
        data={'username': login, 'password': password},
        timeout=70,
    )

    return response.status_code, json.loads(response.text)['token']
