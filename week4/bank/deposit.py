from abc import ABC, abstractmethod
from typing import List, Dict

class Deposit(ABC):
    """Абстрактный базовый класс для банковских вкладов"""
    
    @abstractmethod
    def calculate_profit(self, amount: float, period: float) -> float:
        """
        Рассчитывает прибыль по вкладу

        Параметры:
            amount (float): Сумма вклада
            period (float): Срок вклада в годах

        Результат:
            float: Размер прибыли
        """
        pass


class TermDeposit(Deposit):
    """Срочный вклад с простыми процентами"""
    
    def __init__(self, rate: float) -> None:
        """
        Инициализация срочного вклада

        Параметры:
            rate (float): Годовая процентная ставка (десятичная дробь)
        """
        self.rate = rate
    
    def calculate_profit(self, amount: float, period: float) -> float:
        """
        Расчет по формуле простых процентов: P = amount * rate * period

        Параметры:
            amount (float): Сумма вклада
            period (float): Срок вклада в годах

        Результат:
            float: Размер прибыли
        """
        return amount * self.rate * period


class BonusDeposit(Deposit):
    """Бонусный вклад с дополнительным процентом от прибыли"""
    
    def __init__(self, rate: float, min_amount: float, bonus_percent: float) -> None:
        """
        Инициализация бонусного вклада

        Параметры:
            rate (float): Базовая годовая ставка
            min_amount (float): Минимальная сумма для получения бонуса
            bonus_percent (float): Дополнительный процент от прибыли (десятичная дробь)
        """
        self.rate = rate
        self.min_amount = min_amount
        self.bonus_percent = bonus_percent
    
    def calculate_profit(self, amount: float, period: float) -> float:
        """
        Расчет прибыли с учетом бонуса. 
        Если сумма вклада >= min_amount: общая прибыль = базовая прибыль + (базовая прибыль * bonus_percent)

        Параметры:
            amount (float): Сумма вклада
            period (float): Срок вклада в годах

        Результат:
            float: Размер прибыли с учетом бонуса
        """
        profit = amount * self.rate * period
        if amount >= self.min_amount:
            profit += profit * self.bonus_percent
        return profit


class CapitalizedDeposit(Deposit):
    """Вклад с капитализацией процентов"""
    
    def __init__(self, rate: float, frequency: int) -> None:
        """
        Инициализация вклада с капитализацией

        Параметры:
            rate (float): Годовая номинальная ставка
            frequency (int): Частота капитализации в год (12 - ежемесячно, 4 - ежеквартально)
        """
        self.rate = rate
        self.frequency = frequency
    
    def calculate_profit(self, amount: float, period: float) -> float:
        """
        Расчет по формуле сложных процентов с капитализацией: 
        total = amount * (1 + rate/frequency)^(frequency*period)
        profit = total - amount

        Параметры:
            amount (float): Сумма вклада
            period (float): Срок вклада в годах

        Результат:
            float: Размер прибыли
        """
        total = amount * (1 + self.rate / self.frequency) ** (self.frequency * period)
        return total - amount
