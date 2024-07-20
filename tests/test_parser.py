from src.api_hh import APIHeadHunter
from src.vacancy import Vacancy
from src.parser import parser_data_website, get_value, get_dict_value, parse_string


def test_get_value(dict_vacancy_from_site):
    """ Проверить получение значения элемента словаря по ключу"""
    # для словаря
    assert get_value(dict_vacancy_from_site, 'name') == 'Менеджер по работе с клиентами'

    # для строки
    assert get_value(dict_vacancy_from_site, 'name1') == ''


def test_parse_string(dict_from_site):
    """ Проверить разбор пути к данным по конечному пути """
    assert parse_string(dict_from_site, 'area/name') == 'Воронеж'
    assert parse_string(dict_from_site, 'salary/currency') == 'RUR'
    assert parse_string(dict_from_site, 'salary/to') == '450000'
    assert parse_string(dict_from_site, 'no_key') == ''


def test_get_dict_value(dict_from_site, structure_fields, dict_from_site_result):
    """ Проверить чтение словаря с сайта в словарь для класса Vacancy"""
    result = get_dict_value(dict_from_site, structure_fields)
    assert get_dict_value(dict_from_site, structure_fields) == dict_from_site_result


def test_structure(structure_fields):
    """ Проверка струтуры соответствия полей данных сайт hh.ru и класса Vacancy"""
    assert structure_fields == APIHeadHunter().structure_fields


def test_parser_data_website(dict_vacancy_from_site, structure_fields):
    """ Проверка функции парсера словаря с сайта в список экземпляров класс Vacancy"""

    vacancies, dict_vacancies = parser_data_website(dict_vacancy_from_site, structure_fields)

    # проверяем, что в списке одна запись и это экземпляр класса Vacancy
    assert len(vacancies) == 1
    assert isinstance(vacancies[0], Vacancy)

    # проверяем, что второй результат - это словарь
    assert type(dict_vacancies) is dict
