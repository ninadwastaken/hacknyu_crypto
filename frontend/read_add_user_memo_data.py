import json
from user import User
from memo import Memo

def add_user_data(username, discretionary_money, locked_savings_money, unlocked_savings_money, min_month_end_money, access_token):
    f = open('../data/users.json')
    data = json.load(f)
    user_id = get_user_id()
    data[user_id] = {
        "name": username,
        "min_month_end_money": min_month_end_money,
        "discretionary_money": discretionary_money,
        "locked_savings_money": locked_savings_money,
        "unlocked_savings_money": unlocked_savings_money,
        "access_token": access_token
    }
    with open("../data/users.json", "w") as f:
        json.dump(data, f)

    return user_id

def add_memo_data(store_name, product_name, product_cost, receiver_venmo_id):
    f = open('../data/memos.json')
    data = json.load(f)
    memo_id = get_memo_id()
    data[memo_id] = {
        "store_name": store_name,
        "product_name": product_name,
        "product_cost": product_cost,
        "receiver_venmo_id": receiver_venmo_id
    }
    with open("../data/memos.json", "w") as f:
        json.dump(data, f)

    return memo_id


def read_memo(memo_id):
    memo_object = Memo(memo_id)
    return memo_object

def read_user(user_id):
    return User(user_id)





def get_user_id():
    curr = 1
    f = open('../data/users.json')
    data = json.load(f)
    try:
        while True:
            _ = data[str(curr)]
            curr += 1
    except KeyError:
        return str(curr)



def get_memo_id():
    f = open('../data/memos.json')
    data = json.load(f)

    curr = 1
    try:
        while True:
            _ = data[str(curr)]
            curr += 1
    except KeyError:
        return str(curr)


if __name__ == '__main__':
    print(add_user_data("jn", "100", "37"))


