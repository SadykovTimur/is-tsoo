from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.button import Button
from coms.qa.frontend.pages.component.text import Text
from coms.qa.frontend.pages.component.text_field import TextField
from selenium.common.exceptions import NoSuchElementException

__all__ = ['StartPage']


class StartPage(Page):
    title = Text(tag="h2")
    logo = Component(class_name='authLogo')
    login = TextField(css='[formcontrolname="username"]')
    password = TextField(css='[formcontrolname="password"]')
    submit = Button(xpath='//button[text()=" Войти "]')
    recovery_password = Component(xpath='//a[text()="Восстановить пароль"]')
    support = Component(css='[class*="support"]')

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert self.logo.visible
                assert 'АИС ЭМ ТСОО' == self.title
                assert self.logo.visible
                assert self.password.visible
                assert self.submit.visible
                assert self.recovery_password.visible

                return self.support.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Стартовая страница не загружена')
        self.app.restore_implicitly_wait()
