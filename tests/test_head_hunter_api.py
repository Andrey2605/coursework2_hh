from typing import Any

from src.head_hunter_api import HeadHunterAPI


def test_head_hunter_api() -> Any:
    api = HeadHunterAPI()
    assert api.url == "https://api.hh.ru/vacancies"
    vacs = api.load_vacancies("python")
    assert len(vacs) == 2000
