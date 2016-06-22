from horizon_autotests.app.pages import BasePage
from horizon_autotests.pom.utils import Waiter

waiter = Waiter(polling=0.1)


class BaseSteps(object):

    def __init__(self, app):
        self.app = app

    @property
    def base_page(self):
        return BasePage(self.app)

    def _open(self, page):
        if not isinstance(self.app.current_page, page):
            self.app.open(page)
        return page(self.app)

    def switch_project(self, name):
        self.base_page.project_dropdown.click()
        self.base_page.project_dropdown.project_item(name).click()
        self.close_notification('success')

    def close_notification(self, level):
        with self.base_page.notification(level) as notification:
            notification.close_button.click()
            notification.wait_for_absence()
