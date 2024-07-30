from item import create_item
from order import OrderBuilder
from shopping_cart import Cart
from payment_factory import factory

products = [
    create_item("laptop", 59999),
    create_item("mobile", 35990),
    create_item("shirt", 1499),
    create_item("jeans", 2050),
    create_item("pen", 2000)
]

def add_items_to_cart(cart, products, bill, res=[]):
    #To display the products and prices in the cart in table format
    if not products:
        return res, bill
    
    if products:
        max_sized_product = len(max([product.name for product in products], key=len))
        print(f" |  Product{' '*(max_sized_product-(len('product')-1))}| Price\n-|---------------------")
        for idx, obj in enumerate(products):
            print(f"{idx+1}| {obj.name}{' '*(max_sized_product-len(obj.name))}  | {obj.price}")

        # To see the table and add to cart
        choice = input("product no / done: ").lower()
        if choice == 'done':
            return res, bill
        if choice.isdigit() and int(choice) >= 0 and int(choice) <= len(products):
            res.append(products[int(choice)-1].name)
            tmp_price = products[int(choice)-1].price
            products.pop(int(choice)-1)
            return add_items_to_cart(cart, products, bill+tmp_price, res)
        raise Exception("Invalid Entry")

def checkout(order:OrderBuilder, cart, bill):
    if not cart:
        return "Cart Empty"
    address = input("Enter Shipping Address: ").lower()
    mode = input("Enter Payment Method googlepay/phonpe/paypal/card: ").lower()

    order.set_shipping_address(address).set_bill(bill).set_payment_method(mode)
    for item in cart:
        order.add_item(item)
    return order.make_order()

obj = Cart.get_instance()
cart, bill = add_items_to_cart(obj, products.copy(), 0, obj.items)
print(f"Order Details:\n {checkout(OrderBuilder(), cart, bill)} \n Bill:{bill}")
obj.items.clear()
