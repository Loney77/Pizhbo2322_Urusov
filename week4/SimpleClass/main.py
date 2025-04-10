from money import Money

def test_money_class():
    # Создание объектов
    m1 = Money(100.50, "USD")
    m2 = Money.from_string("200.75 EUR")
    
    # Тестирование операций
    try:
        sum_m = m1 + m2  # Должно вызвать ошибку
    except ValueError as e:
        print(f"Ошибка: {e}")
    
    # Сохранение и загрузка
    m1.save("money.json")
    m3 = Money(0, "USD")
    m3.load("money.json")
    
    # Тестирование методов
    print("Тестирование класса Money:")
    print(f"m1: {m1}")
    print(f"m2: {m2}")
    print(f"m3: {m3} (загружен из файла)")
    print(f"Сравнение: m1 == m3? {m1 == m3}")
    print(f"Форматирование: {m1.formatted}")
    print(f"Конвертация: {m1.convert_to('EUR', 0.85)}")
    print(f"Начисление 10%: {m1.apply_interest(10)}")
    print(f"Разделение на 3 части: {[str(x) for x in m1.split(3)]}")

if __name__ == "__main__":
    test_money_class()
