from ..backend import chatgpt_interactor
from venmo_api import Client

def pay(user, memo, discretionary):
    if discretionary:
        tax = chatgpt_interactor.get_tax(memo, user)
        user.locked_savings_money += tax
        user.discretionary_money -= tax
        user.discretionary_money -= memo.product_cost
        actual_pay(user.access_token, memo.receiver_venmo_id, memo.product_cost)

    else:
        user.unlocked_savings_money -= memo.product_cost
        actual_pay(user.access_token, memo.receiver_venmo_id, memo.product_cost)




def actual_pay(user_id, receiver_id, amt):
    def pay2(access_token, target, amnt):
        client = Client(access_token=access_token)
        note = "transaction made"
        client.payment.send_money(amnt, note, target)

    pay2(user_id, receiver_id, amt)
