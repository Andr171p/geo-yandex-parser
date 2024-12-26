from src.driver import Driver
from src.config import settings


class YandexMapsOpen:
    def __init__(self, driver: Driver) -> None:
        self.driver = driver

    def open_yandex_maps(self) -> None:
        self.driver.get(settings.yandex.maps_url)
