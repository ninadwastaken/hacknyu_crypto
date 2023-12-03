import json

# spending money, money we want at the end of the month (json file)
class User:
    def __init__(self, user_id):
        f = open("../data/users.json")
        data = json.load(f)
        user_data = data[user_id]
        self.discretionary_money = user_data["discretionary_money"]
        self.locked_savings_money = user_data["locked_savings_money"]
        self.unlocked_savings_money = user_data["unlocked_savings_money"]
        self.min_month_end_money = user_data["min_month_end_money"]
        self.username = user_data["name"]
        self.access_token = user_data["access_token"]

    def spend_unlocked_savings(self, amt, receiver_id):
        self.unlocked_savings_money -= amt
        self.pay(receiver_id, amt)

    def pay(self, receiver_id, amt):
        pass

    def spend_discretionary(self, amt, receiver_id):
        pass



