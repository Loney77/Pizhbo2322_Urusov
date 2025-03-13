from abc import ABC, abstractmethod

class Pizza(ABC):
    """Базовый класс для всех видов пицц"""
    
    def __init__(self):
        self.name = ""
        self.dough = ""
        self.sauce = ""
        self.toppings = []
        self.price = 0

    def prepare(self):
        """Процесс подготовки пиццы"""
        print(f"Подготовка пиццы {self.name}:")
        print(f" - Тесто: {self.dough}")
        print(f" - Соус: {self.sauce}")
        print(f" - Начинка: {', '.join(self.toppings)}")

    def bake(self):
        """Процесс выпекания"""
        print("Выпекаем пиццу... Готово!")

    def cut(self):
        """Процесс нарезки"""
        print("Нарезаем на аппетитные кусочки.")

    def pack(self):
        """Процесс упаковки"""
        print("Упаковываем в фирменную коробку.")

    def __str__(self):
        return f"{self.name} ({self.price} руб.)"

class PepperoniPizza(Pizza):
    """Пицца Пепперони"""
    
    def __init__(self):
        super().__init__()
        self.name = "Пепперони"
        self.dough = "тонкое"
        self.sauce = "томатный"
        self.toppings = ["пепперони", "сыр моцарелла"]
        self.price = 350

class BBQPizza(Pizza):
    """Пицца Барбекю"""
    
    def __init__(self):
        super().__init__()
        self.name = "Барбекю"
        self.dough = "толстое"
        self.sauce = "барбекю"
        self.toppings = ["курица", "лук", "сыр моцарелла"]
        self.price = 450

class SeafoodPizza(Pizza):
    """Пицца Дары Моря"""
    
    def __init__(self):
        super().__init__()
        self.name = "Дары Моря"
        self.dough = "тонкое"
        self.sauce = "чесночный"
        self.toppings = ["креветки", "мидии", "сыр моцарелла"]
        self.price = 550

class Order:
    """Класс для управления заказом"""
    
    order_counter = 0
    
    def __init__(self):
        Order.order_counter += 1
        self.order_number = Order.order_counter
        self.pizzas = []

    def add_pizza(self, pizza: Pizza):
        """Добавление пиццы в заказ"""
        self.pizzas.append(pizza)

    def calculate_total(self) -> int:
        """Расчет общей суммы заказа"""
        return sum(pizza.price for pizza in self.pizzas)

    def execute(self):
        """Выполнение заказа"""
        print("\nПриготовление заказа:")
        for pizza in self.pizzas:
            pizza.prepare()
            pizza.bake()
            pizza.cut()
            pizza.pack()
        print("Заказ готов! Приятного аппетита!")

    def __str__(self):
        pizzas = "\n".join(f"- {pizza}" for pizza in self.pizzas)
        return (f"Заказ №{self.order_number}\n"
                f"Состав:\n{pizzas}\n"
                f"Итого: {self.calculate_total()} руб.\n")

class Terminal:
    """Класс для взаимодействия с пользователем"""
    
    def __init__(self):
        self.menu = [PepperoniPizza, BBQPizza, SeafoodPizza]
        self.current_order = None

    def show_menu(self):
        """Отображение меню"""
        print("\nМеню:")
        for i, pizza_class in enumerate(self.menu, 1):
            pizza = pizza_class()
            print(f"{i}. {pizza.name} - {pizza.price} руб.")
            print(f"   Тесто: {pizza.dough}, Соус: {pizza.sauce}")
            print(f"   Начинка: {', '.join(pizza.toppings)}")

    def process_order(self):
        """Обработка заказа"""
        self.current_order = Order()
        
        while True:
            self.show_menu()
            print("\nКоманды: добавить [номер], подтвердить, отменить, выход")
            command = input("Введите команду: ").strip().lower()
            
            if command == "подтвердить":
                if not self.current_order.pizzas:
                    print("Добавьте пиццы в заказ!")
                    continue
                print("\nТекущий заказ:")
                print(self.current_order)
                if input("Подтвердить заказ? (да/нет): ").lower() == "да":
                    self.process_payment()
                    return
            elif command == "отменить":
                self.current_order = None
                print("Заказ отменен")
                return
            elif command == "выход":
                exit()
            elif command.startswith("добавить"):
                try:
                    pizza_num = int(command.split()[1])
                    if 1 <= pizza_num <= len(self.menu):
                        pizza = self.menu[pizza_num-1]()
                        self.current_order.add_pizza(pizza)
                        print(f"Добавлена {pizza.name}")
                    else:
                        print("Неверный номер пиццы")
                except (IndexError, ValueError):
                    print("Неверная команда")
            else:
                print("Неизвестная команда")

    def process_payment(self):
        """Обработка оплаты"""
        total = self.current_order.calculate_total()
        print(f"\nСумма к оплате: {total} руб.")
        
        while True:
            try:
                amount = float(input("Введите сумму оплаты: "))
                if amount >= total:
                    if amount > total:
                        print(f"Сдача: {amount - total:.2f} руб.")
                    print("Оплата принята!")
                    self.current_order.execute()
                    break
                else:
                    print("Недостаточно средств!")
            except ValueError:
                print("Неверная сумма!")

    def start(self):
        """Запуск терминала"""
        print("Добро пожаловать в пиццерию!")
        while True:
            self.process_order()
            if input("\nСделать новый заказ? (да/нет): ").lower() != "да":
                print("До свидания!")
                break

if __name__ == "__main__":
    terminal = Terminal()
    terminal.start()