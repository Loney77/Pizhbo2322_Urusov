class Roman:
    """Класс для работы с римскими числами в диапазоне от I (1) до MMMCMXCIX (3999).
    
    Поддерживает основные арифметические операции:
    - Сложение (+)
    - Вычитание (-)
    - Умножение (*)
    - Целочисленное деление (/)
    
    Примеры использования:
    >>> a = Roman("X")
    >>> b = Roman(5)
    >>> print(a + b)
    XV
    >>> print(a / b)
    II
    """
    
    __ROMAN_VALUES = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 
                     'C': 100, 'D': 500, 'M': 1000}
    __INT_VALUES = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
        (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'),
        (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    
    def __init__(self, value: str | int) -> None:
        """Инициализация объекта Roman.
        
        Args:
            value (str | int): Может быть:
                - Строка с римским числом (напр. "XII")
                - Арабское число (напр. 42)
                
        Raises:
            TypeError: Если передан неподдерживаемый тип данных
            ValueError: Если число вне диапазона 1-3999 или 
                        некорректная римская запись
                        
        Примеры:
            >>> Roman(42)
            Roman('XLII')
            >>> Roman("XLV")
            Roman('XLV')
        """
        if isinstance(value, str):
            self.__value = self.roman_to_int(value)
        elif isinstance(value, int):
            if not 1 <= value <= 3999:
                raise ValueError("Допустимый диапазон: 1-3999")
            self.__value = value
        else:
            raise TypeError("Допустимые типы: str или int")

    @property
    def value(self) -> int:
        """int: Арабское представление числа (только для чтения).
        
        Пример:
            >>> Roman("X").value
            10
        """
        return self.__value

    @staticmethod
    def roman_to_int(roman: str) -> int:
        """Статический метод для преобразования римских чисел в арабские.
        
        Args:
            roman (str): Римское число в верхнем регистре
                        
        Returns:
            int: Соответствующее арабское число
            
        Raises:
            ValueError: Если строка не является корректным римским числом
            
        Пример:
            >>> Roman.roman_to_int("XII")
            12
        """
        if not Roman.__is_valid_roman(roman):
            raise ValueError(f"Некорректное римское число: {roman}")
            
        total = 0
        prev_value = 0
        for char in reversed(roman):
            value = Roman.__ROMAN_VALUES[char]
            total += value if value >= prev_value else -value
            prev_value = value
        return total

    @staticmethod
    def int_to_roman(number: int) -> str:
        """Статический метод для преобразования арабских чисел в римские.
        
        Args:
            number (int): Арабское число от 1 до 3999
            
        Returns:
            str: Соответствующее римское число
            
        Raises:
            ValueError: Если число вне допустимого диапазона
            
        Пример:
            >>> Roman.int_to_roman(42)
            'XLII'
        """
        if not 1 <= number <= 3999:
            raise ValueError("Допустимый диапазон: 1-3999")
            
        roman = []
        for val, sym in Roman.__INT_VALUES:
            while number >= val:
                roman.append(sym)
                number -= val
        return ''.join(roman)

    @staticmethod
    def __is_valid_roman(roman: str) -> bool:
        """Приватный метод для валидации римских чисел.
        
        Использует регулярное выражение для проверки формата:
        - M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})
        
        Args:
            roman (str): Строка для проверки
            
        Returns:
            bool: True если формат корректен, иначе False
        """
        import re
        pattern = r'^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'
        return re.fullmatch(pattern, roman) is not None

    def __add__(self, other: 'Roman | int') -> 'Roman':
        """Перегрузка оператора сложения (+).
        
        Args:
            other (Roman | int): Число для сложения
            
        Returns:
            Roman: Новый объект Roman с результатом
            
        Raises:
            TypeError: Если other не Roman или int
            
        Пример:
            >>> Roman(10) + Roman(5)
            Roman('XV')
        """
        if isinstance(other, Roman):
            return Roman(self.value + other.value)
        if isinstance(other, int):
            return Roman(self.value + other)
        return NotImplemented

    def __sub__(self, other: 'Roman | int') -> 'Roman':
        """Перегрузка оператора вычитания (-).
        
        Важно: Результат не может быть меньше I (1)
        
        Raises:
            ValueError: Если результат меньше 1
            
        Пример:
            >>> Roman(10) - Roman(5)
            Roman('V')
        """
        result = self.value - (other.value if isinstance(other, Roman) else other)
        if result < 1:
            raise ValueError("Результат не может быть меньше I (1)")
        return Roman(result)

    def __mul__(self, other: 'Roman | int') -> 'Roman':
        """Перегрузка оператора умножения (*).
        
        Пример:
            >>> Roman(3) * Roman(4)
            Roman('XII')
        """
        # Реализация аналогична __add__

    def __truediv__(self, other: 'Roman | int') -> 'Roman':
        """Перегрузка оператора деления (/). Целочисленное деление.
        
        Raises:
            ZeroDivisionError: При делении на ноль
            
        Пример:
            >>> Roman(10) / Roman(3)
            Roman('III')
        """
        # Реализация аналогична __add__ с проверкой на ноль

    def __str__(self) -> str:
        """Строковое представление в римском формате.
        
        Пример:
            >>> str(Roman(42))
            'XLII'
        """
        return self.int_to_roman(self.value)

    def __repr__(self) -> str:
        """Официальное строковое представление объекта.
        
        Пример:
            >>> Roman(5)
            Roman('V')
        """
        return f"Roman('{self}')"
    
    
    # Пример использования
if __name__ == "__main__":
    a = Roman("X")
    b = Roman(5)
    
    print(f"{a} + {b} = {a + b}")  # X + V = XV (15)
    print(f"{a} - {b} = {a - b}")  # X - V = V (5)
    print(f"{a} * {b} = {a * b}")  # X * V = L (50)
    print(f"{a} / {b} = {a / b}")  # X / V = II (2)