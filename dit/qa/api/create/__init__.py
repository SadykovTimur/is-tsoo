from typing import Any
from uuid import uuid4

import requests


def create(token: str) -> tuple[int, Any]:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f'Bearer {token}',
    }

    data = {
        "waste_site": 22,
        "tracker_id": "883223000",
        "local_datetime_from": "2021-02-10T09:00:00",
        "local_datetime_to": "2021-02-10T19:00:00",
        "date": "2021-02-11",
        "assignment": 1,
        "ext_id": str(uuid4()),
        "containers_list": [
            {"assignment": 1, "volume": 0.8, "type": 3, "container_id": 46},
            {"assignment": 1, "volume": 0.8, "type": 3, "container_id": 46},
        ],
    }

    response = requests.post(
        'https://tsoo.mos.ru/api/batch__waste_site_visit_plan/', headers=headers, json=data, timeout=70
    )

    return response.status_code
