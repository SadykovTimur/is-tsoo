import allure
from _pytest.fixtures import FixtureRequest

from tests.api.steps import api_auth, create_plan


@allure.label('owner', 't.sadykov')
@allure.label('component', 'DIT')
@allure.epic('IS-TSOO')
@allure.story('Авторизация')
@allure.title('Запрос на создание плана посещения, используя полученный токен')
@allure.severity(allure.severity_level.BLOCKER)
def test_create_plan(request: FixtureRequest) -> None:
    token = api_auth(request.config.option.username_api, request.config.option.password_api)

    create_plan(token)
