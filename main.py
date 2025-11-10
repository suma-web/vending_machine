from suica import Suica
from vendingmachine import VendingMachine


suica = Suica()  # 初期500円
vm = VendingMachine()
suica.char = suica.charge

print("残高:", suica.get_balance())
print("在庫:", vm.get_stock_summary())

bottle = vm.purchase(suica, "ペプシ")
bottle = vm.purchase(suica, "ペプシ")
print("在庫:", vm.get_stock_summary())
print("残高:", suica.get_balance())
print("購入可能:", vm.get_purchasable_list(suica))

suica.char(400)
print("残高（チャージ後）:", suica.get_balance())
print("購入可能:", vm.get_purchasable_list(suica))

bottle = vm.purchase(suica, "いろはす")
bottle = vm.purchase(suica, "いろはす")
bottle = vm.purchase(suica, "モンスター")
print("在庫:", vm.get_stock_summary())
print("残高:", suica.get_balance())
print("購入可能:", vm.get_purchasable_list(suica))

suica.char(300)
print("残高（チャージ後）:", suica.get_balance())
print("購入可能:", vm.get_purchasable_list(suica))
print("在庫", vm.get_stock_summary())

vm.restock("ペプシ", 2) 
vm.restock("いろはす", 2) 
print("在庫", vm.get_stock_summary())
print("自販機の売上:", vm.get_sales_amount())