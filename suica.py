class Suica:
    def __init__(self, initial_deposit=500):
        self._balance = initial_deposit

    def get_balance(self):
        return self._balance

    def set_balance(self, value):
        self._balance = value

    def charge(self, amount):
        if amount is None or not isinstance(amount, int):
            raise ValueError("チャージ金額は整数で指定してください。")
        if amount < 100:
            raise ValueError("100円未満はチャージできません。")
        self._balance += amount
        return self._balance

    def pay(self, amount):
        if self._balance < amount:
            raise RuntimeError("残高不足です。")
        self._balance -= amount
        return self._balance