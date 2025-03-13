from typing import Any

from src.vacancy import Vacancy


def get_vacancies_by_salary_from(vacancies: Any, salary_from: Any) -> Any:
    """Возвращает список вакансий в заданном диапазоне зарплат"""

    return [vac for vac in vacancies if vac.salary >= salary_from]


def sort_vacancies_by_salary(vacancies: Any) -> Any:
    """Сортирует вакансии по зарплате"""

    return sorted(vacancies, key=lambda vacancy: vacancy.salary, reverse=True)


def get_top_vacancies(vacancies: Any, top_n: Any) -> Any:
    """Возвращает топ N вакансий по зарплате"""
    sorted_vacancies = sort_vacancies_by_salary(vacancies)

    return sorted_vacancies[:top_n]
