class Cart:
    from item_manager import show_items
    from ownable import set_owner
    def __init__(self, owner):
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.wallet.balance < self.total_amount():
            print("Saldo Insuficiente")
            
        for item in  self.items:
            item.owner.wallet.deposit(item.price)
            self.owner.wallet.withdraw(item.price)
            item.owner = self.owner   # check_outメソッドをコーディングする際はpassは削除してください。
        # 要件
        #   - カートの中身（Cart#items）のすべてのアイテムの購入金額が、カートのオーナーのウォレットからアイテムのオーナーのウォレットに移されること。
        #   - カートの中身（Cart#items）のすべてのアイテムのオーナー権限が、カートのオーナーに移されること。
        #   - カートの中身（Cart#items）が空になること。
        # ヒント
        #   - カートのオーナーのウォレット ==> self.owner.wallet
        #   - アイテムのオーナーのウォレット ==> item.owner.wallet
        #   - お金が移されるということ ==> (？)のウォレットからその分を引き出して、(？)のウォレットにその分を入金するということ
        #   - アイテムのオーナー権限がカートのオーナーに移されること ==> オーナーの書き換え（item.owner = ?）
        # Al codificar el método check_out, elimina el pass.
# Requisitos
#   - El monto de compra de todos los elementos en el carrito (Cart#items) se transfiere de la billetera del propietario del carrito a la billetera del propietario del artículo.
#   - Se transfiere la autoridad del propietario de todos los elementos en el carrito (Cart#items) al propietario del carrito.
#   - El contenido del carrito (Cart#items) se vacía.
# Sugerencias
#   - Billetera del propietario del carrito ==> self.owner.wallet
#   - Billetera del propietario del artículo ==> item.owner.wallet
#   - La transferencia de dinero implica ==> Retirar esa cantidad de la billetera de (¿?) y depositarla en la billetera de (¿?)
#   - La autoridad del propietario del artículo se transfiere al propietario del carrito ==> Reemplazar el propietario (item.owner = ?)

