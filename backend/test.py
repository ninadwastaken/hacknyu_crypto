# from openai import OpenAI
# API_KEY = "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"
# client = OpenAI(api_key=API_KEY)
#
# response = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a helpful assistant."},
#     {"role": "user", "content": "Who won the world series in 2020?"},
#     {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
#     {"role": "user", "content": "Where was it played?"}
#   ]
# )
#
# print(response)

import json

memos = {"1": {
  "store_name": "burger king",
  "product_name": "big mac",
  "product_cost": 10
}
}

users = {"1":{
  "balance": 100,
  "min_month_end_money": 50,
  "name": "your mom"
}
}





with open("../data/users.json", "w") as f:
  json.dump(users, f)