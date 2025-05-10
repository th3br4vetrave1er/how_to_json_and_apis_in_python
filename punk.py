import json
import requests
from random import randint


def main():
    # 1. URL для получения СПИСКА всех монстров
    list_url = 'https://www.dnd5eapi.co/api/monsters/'

    # Базовый URL API
    base_api_url = 'https://www.dnd5eapi.co'

    # Выполняем запрос для получения списка
    r_list = requests.get(list_url)
    data_list = json.loads(r_list.text)

    # Получаем список монстров из поля results
    monsters_list = data_list['results']
    # Выбираем случайный индекс монстра
    random_index = randint(0, len(monsters_list) - 1)

    # Получаем информацию о случайном монстре из списка
    random_monster_summary = monsters_list[random_index]

    # Получаем относительный URL для детальной информации об этом монстре
    monster_detail_relative_url = random_monster_summary['url']

    # Составляем полный URL для запроса детальной информации
    monster_detail_url = base_api_url + monster_detail_relative_url

    print(f"Выбран случайный монстр: {random_monster_summary['name']}")
    print(f"Получаем детальную информацию по URL: {monster_detail_url}")

    # 2. Выполняем запрос для получения детальной информации о выбранном монстре
    r_detail = requests.get(monster_detail_url)
    data_detail = json.loads(r_detail.text)

    # Теперь у нас есть полные данные о монстре в data_detail
    # Выводим нужную нам информацию о монстре:
    print("\nДетали монстра:")
    print(f"Имя: {data_detail.get('name', 'N/A')}") # .get() для безопасного доступа
    print(f"Размер: {data_detail.get('size', 'N/A')}")
    print(f"Тип: {data_detail.get('type', 'N/A')}")
    print(f"Класс брони: {data_detail.get('armor_class', 'N/A')}")
    print(f"Хиты: {data_detail.get('hit_points', 'N/A')}")
    print(f"Скорость: {data_detail.get('speed', 'N/A')}")


if __name__ == "__main__":
    main()