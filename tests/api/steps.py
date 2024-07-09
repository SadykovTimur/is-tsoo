import allure

from dit.qa.api.auth import auth
from dit.qa.api.create import create

__all__ = ['api_auth', 'create_plan']


def api_auth(login: str, password: str) -> str:
    with allure.step(f'API authorization by {login}'):
        code, token = auth(login, password)

        assert code == 200, f"Код ответа {code} не соответствует ожидаемому"

        return token


@allure.step('Checking create plan')
def create_plan(token: str) -> None:
    code = create(token)

    assert code == 201, f"Код ответа {code} не соответствует ожидаемому"
