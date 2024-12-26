import logging

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent


ua = UserAgent(platforms='desktop')


log = logging.getLogger(__name__)


class Driver(webdriver.Chrome):
    _options = webdriver.ChromeOptions()
    _options.add_argument(f"--user-agent={ua.random}")
    _options.add_experimental_option("excludeSwitches", ["enable-automation"])
    _options.add_experimental_option('useAutomationExtension', False)
    _service = Service(ChromeDriverManager().install())

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, options=self._options, service=self._service, **kwargs)
        log.info("Chrome web-driver successfully installed")
