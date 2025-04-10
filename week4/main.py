from bank import Bank
from deposit import TermDeposit, BonusDeposit, CapitalizedDeposit

if __name__ == "__main__":
    # Инициализация банка и добавление вкладов
    bank = Bank()
    bank.add_deposit(TermDeposit(0.05))           # 5% годовых
    bank.add_deposit(BonusDeposit(0.04, 100000, 0.1)) # 4% + 10% бонус
    bank.add_deposit(CapitalizedDeposit(0.05, 12))    # 5% с ежемесячной капитализацией

    # Расчет прибыли для суммы 150000 руб на 1 год
    amount = 150000
    period = 1
    profits = bank.calculate_profits(amount, period)

    # Вывод результатов
    print(f"Сумма вклада: {amount} руб., срок: {period} год(а/лет)")
    for p in profits:
        print(f"Тип вклада: {p['type']}, Прибыль: {p['profit']} руб.")
