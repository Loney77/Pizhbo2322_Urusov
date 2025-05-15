import json
from money import Money

class MoneyCollection:
    """
    Класс-контейнер для управления коллекцией объектов Money

    Описание:
        Обеспечивает хранение, добавление, удаление, сохранение/загрузку
        и базовые операции с коллекцией денежных сумм
    """

    def __init__(self):
        """
        Инициализация пустой коллекции
        """
        self._data = []

    def __str__(self):
        """
        Назначение:
            Представление коллекции в виде строки

        Результат:
            str: Строковое представление всех элементов
        """
        return "\n".join(str(item) for item in self._data)

    def __getitem__(self, index):
        """
        Назначение:
            Доступ к элементам по индексу или срезу

        Параметры:
            index (int или slice): Индекс или срез

        Результат:
            Money или MoneyCollection: Элемент или новая коллекция для среза
        """
        if isinstance(index, slice):
            new_collection = MoneyCollection()
            new_collection._data = self._data[index]
            return new_collection
        return self._data[index]

    def add(self, value):
        """
        Назначение:
            Добавление нового элемента в коллекцию

        Параметры:
            value (Money): Добавляемый объект Money

        Исключения:
            TypeError: Если передан объект не типа Money
        """
        if not isinstance(value, Money):
            raise TypeError("Можно добавлять только объекты Money")
        self._data.append(value)

    def remove(self, index):
        """
        Назначение:
            Удаление элемента по индексу

        Параметры:
            index (int): Индекс удаляемого элемента

        Исключения:
            IndexError: При неверном индексе
        """
        if 0 <= index < len(self._data):
            del self._data[index]
        else:
            raise IndexError("Неверный индекс")

    def save(self, filename):
        """
        Назначение:
            Сохранение коллекции в JSON-файл

        Параметры:
            filename (str): Имя файла для сохранения
        """
        data = [{"amount": item.amount, "currency": item.currency} for item in self._data]
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load(self, filename):
        """
        Назначение:
            Загрузка коллекции из JSON-файла

        Параметры:
            filename (str): Имя файла для загрузки

        Исключения:
            ValueError: При неверном формате данных
        """
        with open(filename, 'r') as f:
            data = json.load(f)
        
        self._data.clear()
        for item in data:
            if "amount" not in item or "currency" not in item:
                raise ValueError("Некорректный формат данных")
            self._data.append(Money(item["amount"], item["currency"]))

    @property
    def count(self):
        """
        Назначение:
            Получение количества элементов

        Результат:
            int: Количество элементов в коллекции
        """
        return len(self._data)