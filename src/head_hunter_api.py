from abc import ABC, abstractmethod
from typing import Any

import requests


class Parser(ABC):

    @abstractmethod
    def load_vacancies(self, keyword: str) -> list[dict]:
        pass


class HeadHunterAPI(Parser):
    """Класс для работы с API HeadHunter"""

    def __init__(self) -> None:
        """Инициализатор класса HeadHunterAPI"""
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params: Any = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies: Any = []

    @property
    def url(self) -> Any:
        """Возвращает войство url"""
        return self.__url

    def __api_connect(self) -> Any:
        """Подключение к API hh.ru"""
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        if response.status_code == 200:
            return response
        return "Ошибка получения данных"

    def load_vacancies(self, keyword: Any) -> Any:
        """Получение вакансий по ключевому слову"""
        self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            response = self.__api_connect()
            if response:
                vacancies = response.json()["items"]
                self.__vacancies.extend(vacancies)
                self.__params["page"] += 1
            else:
                break

        vacancies_list = []

        if self.__vacancies:

            # получение списка словарей с ключами name, url, requirement, responsibility, salary
            for vacancy in self.__vacancies:
                name = vacancy.get("name")
                url = vacancy.get("alternate_url")
                requirement = vacancy.get("snippet").get("requirement")
                responsibility = vacancy.get("snippet").get("responsibility")

                if vacancy.get("salary"):
                    if vacancy.get("salary").get("to"):
                        salary = vacancy.get("salary").get("to")
                    elif vacancy.get("salary").get("from"):
                        salary = vacancy.get("salary").get("from")
                else:
                    salary = 0

                vac = {
                    "name": name,
                    "url": url,
                    "requirement": requirement,
                    "responsibility": responsibility,
                    "salary": salary,
                }
                vacancies_list.append(vac)

        return vacancies_list
