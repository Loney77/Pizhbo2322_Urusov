from typing import List, Dict
from deposit import Deposit

class Bank:
    """Класс для управления вкладами и сравнения условий"""
    
    def __init__(self) -> None:
        """Инициализация банка с пустым списком вкладов"""
        self.deposits: List[Deposit] = []
    
    def add_deposit(self, deposit: Deposit) -> None:
        """
        Добавление вклада в список доступных

        Параметры:
            deposit (Deposit): Объект вклада для добавления
        """
        self.deposits.append(deposit)
    
    def calculate_profits(self, amount: float, period: float) -> List[Dict]:
        """
        Расчет прибыли для всех доступных вкладов

        Параметры:
            amount (float): Сумма вклада
            period (float): Срок вклада в годах

        Результат:
            List[Dict]: Список словарей с результатами в формате:
                {'type': тип вклада, 'profit': размер прибыли}
        """
        results = []
        for deposit in self.deposits:
            profit = deposit.calculate_profit(amount, period)
            deposit_type = deposit.__class__.__name__
            results.append({
                'type': deposit_type,
                'profit': round(profit, 2)
            })
        return results
