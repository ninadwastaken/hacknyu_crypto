import json

# memo: store name, name of product, cost (in json format)
class Memo:
    def __init__(self, transaction_id):
        f = open("../data/memos.json")
        data = json.load(f)
        transaction = data[transaction_id]
        self.store_name = transaction["store_name"]
        self.product_name = transaction["product_name"]
        self.product_cost = transaction["product_cost"]
