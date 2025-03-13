from typing import List, Literal, Union


class Product:
    """Класс для представления товара.
    
    Attributes:
        __name: Название товара
        __store: Название магазина
        __price: Цена товара в рублях
    """
    
    def __init__(self, name: str, store: str, price: Union[int, float]) -> None:
        """
        Назначение:
            Инициализация объекта товара
            
        Параметры:
            name: Название товара
            store: Название магазина
            price: Стоимость товара (целое или дробное число)
        """
        self.__name = name
        self.__store = store
        self.__price = price

    @property
    def name(self) -> str:
        """
        Назначение:
            Получение названия товара
            
        Результат:
            Строка с названием товара
        """
        return self.__name

    @property
    def store(self) -> str:
        """
        Назначение:
            Получение названия магазина
            
        Результат:
            Строка с названием магазина
        """
        return self.__store

    @property
    def price(self) -> Union[int, float]:
        """
        Назначение:
            Получение цены товара
            
        Результат:
            Числовое значение цены
        """
        return self.__price

    def __add__(self, other: Union['Product', int, float]) -> Union[int, float, NotImplemented]:
        """
        Назначение:
            Сложение цен товаров (перегрузка оператора +)
            
        Параметры:
            other: Второй операнд (товар или число)
            
        Результат:
            Сумма цен или NotImplemented для неподдерживаемых типов
        """
        if isinstance(other, Product):
            return self.price + other.price
        if isinstance(other, (int, float)):
            return self.price + other
        return NotImplemented

    def __radd__(self, other: Union[int, float]) -> Union[int, float]:
        """
        Назначение:
            Правостороннее сложение (для работы функции sum())
            
        Параметры:
            other: Левый операнд (число)
            
        Результат:
            Сумма цен
        """
        return self.__add__(other)

    def __str__(self) -> str:
        """
        Назначение:
            Строковое представление товара
            
        Результат:
            Форматированная строка с информацией о товаре
        """
        return f"Товар: {self.name}, Магазин: {self.store}, Цена: {self.price} руб."


class Warehouse:
    """Класс для управления складом товаров.
    
    Attributes:
        __items: Список товаров на складе
    """
    
    def __init__(self) -> None:
        """Инициализация пустого склада"""
        self.__items: List[Product] = []

    def add_product(self, product: Product) -> None:
        """
        Назначение:
            Добавление товара на склад
            
        Параметры:
            product: Объект товара для добавления
        """
        self.__items.append(product)

    def __getitem__(self, index: int) -> Product:
        """
        Назначение:
            Получение товара по индексу
            
        Параметры:
            index: Индекс товара в списке
            
        Результат:
            Объект товара
        """
        return self.__items[index]

    def find_by_name(self, name: str) -> List[Product]:
        """
        Назначение:
            Поиск товаров по названию
            
        Параметры:
            name: Искомое название товара
            
        Результат:
            Список найденных товаров
        """
        return [product for product in self.__items if product.name == name]

    def sort_by(self, key: Literal['name', 'store', 'price']) -> None:
        """
        Назначение:
            Сортировка товаров по указанному ключу
            
        Параметры:
            key: Критерий сортировки:
                'name' - по названию товара
                'store' - по названию магазина
                'price' - по цене
        """
        if key == 'name':
            self.__items.sort(key=lambda p: p.name)
        elif key == 'store':
            self.__items.sort(key=lambda p: p.store)
        elif key == 'price':
            self.__items.sort(key=lambda p: p.price)
        else:
            raise ValueError("Неверный ключ сортировки. Допустимо: 'name', 'store', 'price'")

    def __len__(self) -> int:
        """
        Назначение:
            Получение количества товаров на складе
            
        Результат:
            Целое число - количество товаров
        """
        return len(self.__items)

    def get_all_products(self) -> List[Product]:
        """
        Назначение:
            Получение копии списка товаров
            
        Результат:
            Копия списка товаров на складе
        """
        return self.__items.copy()


# Пример использования
if __name__ == "__main__":
    # Создание товаров
    p1 = Product("Книга", "Литрес", 500)
    p2 = Product("Мышь", "Эльдорадо", 2000)
    p3 = Product("Книга", "Озон", 450)

    # Создание и заполнение склада
    warehouse = Warehouse()
    warehouse.add_product(p1)
    warehouse.add_product(p2)
    warehouse.add_product(p3)

    # Вывод по индексу
    print("Товар по индексу 0:")
    print(warehouse[0])

    # Поиск по названию
    print("\nПоиск товаров с названием 'Книга':")
    for product in warehouse.find_by_name("Книга"):
        print(product)

    # Сортировка по цене
    warehouse.sort_by('price')
    print("\nСклад после сортировки по цене:")
    for product in warehouse.get_all_products():
        print(product)

    # Сложение цен товаров
    total = p1 + p2 + p3
    print(f"\nСуммарная стоимость всех товаров: {total} руб.")

    # Использование sum() для сложения
    total_sum = sum(warehouse.get_all_products())
    print(f"Общая сумма через sum(): {total_sum} руб.")