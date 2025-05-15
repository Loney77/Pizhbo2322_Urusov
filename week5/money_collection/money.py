import json
from typing import Union, List

class Money:
    """
    Класс для представления денежных сумм с поддержкой основных арифметических операций,
    конвертации, сохранения/загрузки и дополнительных финансовых операций.

    Атрибуты:
        amount (float): Сумма денег
        currency (str): Валюта (3 символа)
    """
    
    def __init__(self, amount: float, currency: str = "USD") -> None:
        """
        Инициализация денежной единицы

        Назначение:
            Создает объект денежной суммы с валидацией входных данных

        Параметры:
            amount (float): Сумма денег (должна быть неотрицательной)
            currency (str): Код валюты из 3 символов (по умолчанию USD)

        Исключения:
            ValueError: Если сумма отрицательная или неверный формат валюты
        """
        if amount < 0:
            raise ValueError("Сумма не может быть отрицательной")
        if len(currency) != 3:
            raise ValueError("Неверный формат валюты")
            
        self.amount = round(amount, 2)
        self.currency = currency.upper()

    def __str__(self) -> str:
        """
        Назначение:
            Представление объекта в формате для пользователя

        Результат:
            str: Строка в формате '100.50 USD'
        """
        return f"{self.amount:.2f} {self.currency}"
    
    def __add__(self, other: 'Money') -> 'Money':
        """
        Назначение:
            Сложение денежных сумм одной валюты

        Параметры:
            other (Money): Вторая денежная сумма

        Результат:
            Money: Новая сумма после сложения

        Исключения:
            ValueError: При разных валютах
        """
        if self.currency != other.currency:
            raise ValueError("Разные валюты")
        return Money(self.amount + other.amount, self.currency)
    
    def __sub__(self, other: 'Money') -> 'Money':
        """
        Назначение:
            Вычитание денежных сумм одной валюты

        Параметры:
            other (Money): Вычитаемая сумма

        Результат:
            Money: Новая сумма после вычитания

        Исключения:
            ValueError: При разных валютах
        """
        if self.currency != other.currency:
            raise ValueError("Разные валюты")
        return Money(self.amount - other.amount, self.currency)
    
    def __eq__(self, other: 'Money') -> bool:
        """
        Назначение:
            Проверка эквивалентности сумм

        Параметры:
            other (Money): Сравниваемая сумма

        Результат:
            bool: True если суммы и валюты совпадают
        """
        return self.amount == other.amount and self.currency == other.currency
    
    def __lt__(self, other: 'Money') -> bool:
        """
        Назначение:
            Сравнение сумм (меньше)

        Параметры:
            other (Money): Сравниваемая сумма

        Результат:
            bool: True если текущая сумма меньше

        Исключения:
            ValueError: При разных валютах
        """
        if self.currency != other.currency:
            raise ValueError("Разные валюты")
        return self.amount < other.amount

    @classmethod
    def from_string(cls, str_value: str) -> 'Money':
        """
        Назначение:
            Создание объекта из строки формата '100.00 USD'

        Параметры:
            str_value (str): Входная строка

        Результат:
            Money: Созданный объект

        Исключения:
            ValueError: При неверном формате строки
        """
        try:
            amount_str, currency = str_value.split()
            return cls(float(amount_str), currency)
        except Exception as e:
            raise ValueError(f"Некорректный формат строки: {str_value}") from e

    def save(self, filename: str) -> None:
        """
        Назначение:
            Сохранение объекта в JSON-файл

        Параметры:
            filename (str): Путь к файлу для сохранения
        """
        data = {
            'amount': self.amount,
            'currency': self.currency
        }
        with open(filename, 'w') as f:
            json.dump(data, f)

    def load(self, filename: str) -> None:
        """
        Назначение:
            Загрузка объекта из JSON-файла

        Параметры:
            filename (str): Путь к файлу для загрузки
        """
        with open(filename, 'r') as f:
            data = json.load(f)
        self.amount = data['amount']
        self.currency = data['currency']

    def convert_to(self, target_currency: str, rate: float) -> 'Money':
        """
        Назначение:
            Конвертация в другую валюту по указанному курсу

        Параметры:
            target_currency (str): Целевая валюта
            rate (float): Курс обмена (1 текущая = rate целевой)

        Результат:
            Money: Новая сумма в целевой валюте
        """
        return Money(self.amount * rate, target_currency)

    def apply_interest(self, percent: float) -> 'Money':
        """
        Назначение:
            Начисление процентов на сумму

        Параметры:
            percent (float): Процентная ставка

        Результат:
            Money: Новая сумма с начисленными процентами
        """
        return Money(self.amount * (1 + percent/100), self.currency)

    def split(self, parts: int) -> List['Money']:
        """
        Назначение:
            Разделение суммы на равные части

        Параметры:
            parts (int): Количество частей (должно быть > 0)

        Результат:
            List[Money]: Список из частей суммы

        Исключения:
            ValueError: При некорректном количестве частей
        """
        if parts <= 0:
            raise ValueError("Количество частей должно быть положительным")
            
        part = round(self.amount / parts, 2)
        remainder = self.amount - part * (parts-1)
        return [Money(part, self.currency) for _ in range(parts-1)] + [Money(remainder, self.currency)]

    @property
    def formatted(self) -> str:
        """
        Назначение:
            Получение форматированной строки с валютой

        Результат:
            str: Строка в формате 'USD 100.50'
        """
        return f"{self.currency} {self.amount:,.2f}"

    @property
    def is_positive(self) -> bool:
        """
        Назначение:
            Проверка положительности суммы

        Результат:
            bool: True если сумма больше нуля
        """
        return self.amount > 0