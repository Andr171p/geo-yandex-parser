import logging
from typing import TYPE_CHECKING

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from src.yandex_maps.service.search_form import YandexMapsSearchForm
from src.yandex_maps.schemas.result import ResultSchema

if TYPE_CHECKING:
    from selenium.webdriver.remote.webelement import WebElement


log = logging.getLogger(__name__)


class YandexMapsSearchResult(YandexMapsSearchForm):
    def get_first_result(self, timeout: int = 3) -> None:
        try:
            result: WebElement = WebDriverWait(
                driver=self.driver,
                timeout=timeout
            ).until(ec.presence_of_element_located(
                (By.XPATH, "//ul[@class='search-list-view__list']"))
            )
            result.click()
        except Exception as _ex:
            log.warning(_ex)
            log.info("Current result was found the first time")

    def open_result_page(self) -> None:
        element = self.driver.find_element(
            by=By.CLASS_NAME,
            value='card-title-view__title-link'
        )
        link = element.get_attribute("href")
        self.driver.get(link)

    def get_result_data(self) -> ResultSchema:
        self.get_first_result()
        self.open_result_page()
        name = self.driver.find_element(
            by=By.XPATH,
            value='//h1[@class="orgpage-header-view__header"]'
        )
        phone = self.driver.find_element(
            by=By.XPATH,
            value='//div[@class="orgpage-phones-view__phone-number"]'
        )
        rating = self.driver.find_element(
            by=By.XPATH,
            value='//span[@class="business-rating-badge-view__rating-text"]'
        )
        address = self.driver.find_element(
            by=By.XPATH,
            value='//a[@class="orgpage-header-view__address"]'
        )
        result = ResultSchema(
            name=name.text,
            phone=phone.text,
            address=address.get_attribute("title"),
            link=self.driver.current_url,
            rating=float(rating.text.replace(',', '.'))
        )
        log.info(result)
        return result

