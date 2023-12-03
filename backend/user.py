import json

# spending money, money we want at the end of the month (json file)
class User:
    def __init__(self, user_id):
        f = open("../data/users.json")
        data = json.load(f)
        user_data = data[user_id]
        self.balance = user_data["balance"]
        self.min_month_end_money = user_data["min_month_end_money"]
        self.username = user_data["name"]


