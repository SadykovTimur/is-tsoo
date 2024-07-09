from __future__ import annotations

from coms.qa.core.helpers import wait_for
from coms.qa.frontend.pages import Page
from coms.qa.frontend.pages.component import Component
from coms.qa.frontend.pages.component.text import Text
from selenium.common.exceptions import NoSuchElementException

__all__ = ['MainPage']


class MainPage(Page):
    title = Text(css='[class*="logo__title"]')
    breadcrumb = Text(css='[class*="breadcrumb__title"]')
    user = Component(css='[class*="navbar-user"]')
    nav = Component(class_name='sidebar__nav-list')
    filter = Component(css='[class*="filter__toggle"]')
    form = Component(css='[class*="filter-form"]')
    submit = Component(xpath='//span[text()="Применить"]')
    reset = Component(xpath='//span[text()="Сбросить"]')
    table = Component(css='[class*="table-wrapper"]')
    loader = Component(css='[class*="loader"]')

    @property
    def is_loader_hide(self) -> bool:
        try:
            return not self.loader.visible
        except NoSuchElementException:
            return True

    def wait_for_loading(self) -> None:
        def condition() -> bool:
            try:
                assert 'АИС ЭМ ТСОО' == self.title
                assert 'Места накопления отходов' == self.breadcrumb
                assert self.user.visible
                assert self.nav.visible
                assert self.filter.visible
                assert self.form.visible
                assert self.submit.visible
                assert self.reset.visible
                assert self.is_loader_hide

                return self.table.visible

            except NoSuchElementException:

                return False

        self.app.set_implicitly_wait(1)
        wait_for(condition, timeout=70, msg='Главная страница не загружена')
        self.app.restore_implicitly_wait()
