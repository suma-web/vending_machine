from juice import Juice


class VendingMachine:
    def __init__(self):
        self._sales_amount = 0
        self._stock = {}
        self._price_table = {}
        self.register_product("ペプシ", 150, 5)
        self.register_product("モンスター", 230, 5)
        self.register_product("いろはす", 120, 5)

    def register_product(self, name, price, count):
        if not isinstance(count, int) or count <= 0:
            raise ValueError("本数は正の整数にしてください。")
        self._price_table.setdefault(name, price)
        if name not in self._stock:
            self._stock[name] = []
        for _ in range(count):
            self._stock[name].append(Juice(name, price))
        return len(self._stock[name])

    def restock(self, name, count):
        if not isinstance(count, int) or count <= 0:
            raise ValueError("補充本数は正の整数にしてください。")
        if name not in self._price_table:
            raise ValueError(f"{name} は登録されていません。")
        price = self._price_table[name]
        for _ in range(count):
            self._stock[name].append(Juice(name, price))
        return len(self._stock[name])

    def get_sales_amount(self):
        return self._sales_amount

    def get_stock_summary(self):
        summary: dict[str, tuple[int, int]] = {}
        for name, items in self._stock.items():
            if items:
                price = items[0].get_price()
                summary[name] = (price, len(items))
            else:
                summary[name] = (self._price_table.get(name, 0), 0)
        return summary

    def can_purchase(self, suica, name):
        items = self._stock.get(name, [])
        if not items:
            return False
        price = items[0].get_price()
        return suica.get_balance() >= price

    def get_purchasable_list(self, suica):
        purchasable = []
        balance = suica.get_balance()
        for name, items in self._stock.items():
            if items and items[0].get_price() <= balance:
                purchasable.append(name)
        return purchasable

    def purchase(self, suica, name):
        items = self._stock.get(name, [])
        if not items:
            raise RuntimeError("在庫がありません。")
        price = items[0].get_price()
        if suica.get_balance() < price:
            raise RuntimeError("残高が足りません。")
        dispensed = items.pop(0)
        suica.pay(price)
        self._sales_amount += price
        return dispensed