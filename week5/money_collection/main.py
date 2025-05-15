from money import Money
from MoneyCollection import MoneyCollection

def test_collection():
    # Создание коллекции
    mc = MoneyCollection()
    
    # Добавление элементов
    mc.add(Money(100, "USD"))
    mc.add(Money.from_string("200.50 EUR"))
    
    # Проверка методов
    print("Количество элементов:", mc.count)
    print("Первый элемент:", mc[0])
    print("Все элементы:\n", mc)
    
    # Сохранение и загрузка
    mc.save("collection.json")
    
    new_mc = MoneyCollection()
    new_mc.load("collection.json")
    print("\nЗагруженная коллекция:\n", new_mc)
    
    # Удаление элемента
    new_mc.remove(0)
    print("\nПосле удаления:\n", new_mc)
    
    # Работа со срезом
    slice_mc = new_mc[:]
    print("\nСрез коллекции:\n", slice_mc)

if __name__ == "__main__":
    test_collection()