import allure
from _pytest.fixtures import FixtureRequest

from tests.api.steps import api_auth


@allure.label('owner', 't.sadykov')
@allure.label('component', 'DIT')
@allure.epic('IS-TSOO')
@allure.story('Авторизация')
@allure.title('Выполнение авторизации через API')
@allure.severity(allure.severity_level.BLOCKER)
def test_check_api_auth(request: FixtureRequest) -> None:

    api_auth(request.config.option.username_api, request.config.option.password_api)
