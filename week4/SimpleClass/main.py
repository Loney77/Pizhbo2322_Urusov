from money import Money

def test_money_operations():
    # Создание объектов
    salary = Money(1500.0, "USD")
    bonus = Money.from_string("300.50 USD")
    
    # Арифметические операции
    total = salary + bonus
    difference = total - Money(200.0, "USD")
    
    # Сохранение/загрузка
    total.save("total.json")
    loaded_money = Money(0, "USD")
    loaded_money.load("total.json")
    
    print("Тестирование класса Money:")
    print(f"Зарплата: {salary}")
    print(f"Бонус: {bonus}")
    print(f"Итого: {total}")
    print(f"После расходов: {difference}")
    print(f"Загруженная сумма: {loaded_money}")
    print(f"Форматированная: {loaded_money.formatted}")
    print(f"Положительная? {loaded_money.is_positive}")
    print(f"Конвертация в EUR (0.85): {loaded_money.convert_to('EUR', 0.85)}")
    print(f"Начисление 10%: {loaded_money.apply_interest(10)}")
    print(f"Разделение на 3 части: {[str(x) for x in loaded_money.split(3)]}")

if __name__ == "__main__":
    test_money_operations()