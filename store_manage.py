class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар '{item_name}' добавлен с ценой {price} руб. в {self.name} по адресу: {self.address}")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален в {self.name} по адресу: {self.address}")
        else:
            print(f"Товар '{item_name}' не найден в {self.name} по адресу: {self.address}")

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' изменилась на цену {new_price} руб. в {self.name} по адресу: {self.address}")
        else:
            print(f"Товар '{item_name}' не найден в {self.name} по адресу: {self.address}")


# Создание объектов класса Store
store1 = Store('Магазин "Эльдорадо"', "Москва, Ленинградское ш., д. 112/1")
store2 = Store("Овощной магазин", "Москва, Алтуфьевское ш., д. 13/1")
store3 = Store("Книжный магазин", "Москва, Дмитровское ш., д. 43/2")

# Добавление товаров в магазины
store1.add_item("Ноутбук", 24999.0)
store1.add_item("Смартфон", 14999.99)

store2.add_item("Яблоки", 109.0)
store2.add_item("Бананы", 100.0)

store3.add_item("Книга про рецепты", 520.99)
store3.add_item("Тетрадь", 59.99)

# Тестирование методов на одном из магазинов
print("\nТестирование методов на примере мегазина 'Эльдорадо':")
store1.add_item("Планшет Samsung", 14999.99)
print(f"Цена планшета Samsung: {store1.get_price('Планшет Samsung')} руб.")

store1.update_price("Планшет Samsung", 11999.99)
print(f"Новая цена планшета Samsung: {store1.get_price('Планшет Samsung')} руб.")

store1.remove_item("Планшет Samsung")
print(f"Цена планшета Samsung после удаления: {store1.get_price('Планшет Samsung')} руб.")