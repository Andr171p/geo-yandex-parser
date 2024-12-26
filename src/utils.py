import logging

from src.yandex_maps.service.result import YandexMapsSearchResult
from src.driver import Driver


logging.basicConfig(level=logging.INFO)


driver = Driver()

search_result = YandexMapsSearchResult(Driver())
search_result.enter_input_to_form(name='МБОУ СОШ №28 имени Молодова С.Г. г. Челябинска, г. Челябинск')
print(search_result.get_result_data())
search_result.open_yandex_maps()
search_result.enter_input_to_form(name='ГАПОУ Тюменской области ""Тюменский техникум строительной индустрии и городского хозяйства"", г. Тюмень')
print(search_result.get_result_data())