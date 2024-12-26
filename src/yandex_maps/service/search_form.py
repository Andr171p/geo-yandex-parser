import time
import logging
from typing import TYPE_CHECKING

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from src.driver import Driver
from src.yandex_maps.service.open import YandexMapsOpen

if TYPE_CHECKING:
    from selenium.webdriver.remote.webelement import WebElement


log = logging.getLogger(__name__)


class YandexMapsSearchForm(YandexMapsOpen):
    def __init__(self, driver: Driver) -> None:
        super().__init__(driver)
        self.open_yandex_maps()

    def _search_form_element(
            self,
            timeout: int = 5
    ) -> "WebElement":
        form: "WebElement" = WebDriverWait(
            driver=self.driver,
            timeout=timeout
        ).until(ec.presence_of_element_located(
            (By.XPATH, "//input[@class='input__control _bold']"))
        )
        return form

    def enter_input_to_form(
            self,
            name: str,
            timeout: int = 1
    ) -> None:
        form = self._search_form_element()
        form.clear()
        form.send_keys(name)
        form.send_keys(Keys.ENTER)
        log.info("Entered name: %s", name)
        time.sleep(timeout)
