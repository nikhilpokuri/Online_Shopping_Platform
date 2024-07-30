from abstract_payment import Payment

class GooglepayPayment(Payment):
    def pay(self, amount):
        return f"Payment of {amount} Done Using GooglePay"

class PhonepePayment(Payment):
    def pay(self, amount):
        return f"Payment of {amount} Done Using Phonepe"

class PaypalPayment(Payment):
    def pay(self, amount):
        return f"Payment of {amount} Done Using Paypal"

class CardPayment(Payment):
    def pay(self, amount):
        return f"Payment of {amount} Done Using Card"

def factory(mode, bill):
    modes = {
        "phonepe": PhonepePayment,
        "googlepay": GooglepayPayment,
        "paypal": PaypalPayment,
        "card": CardPayment
    }
    if mode in modes:
        print(modes[mode]().pay(bill))
        return True
    return False