from openai import OpenAI
from user import User
from memo import Memo

API_KEY = "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"
client = OpenAI(api_key=API_KEY)

def get_tax(memo, user):
    prompt = f"I have {user.balance}$ in my bank account. " \
             f"I want to have {user.min_month_end_money}$ left at the end of the month. " \
             f"I want to buy a {memo.product_name} from {memo.store_name} for ${memo.product_cost}. " \
             "On a scale of 0 to 1000, how bad is this purchase? " \
             "1000 being horrible and 0 being insanely good. " \
             "Give me an objective value. " \
             "Reply only with a concrete number and nothing else."
    curr_input = [{"role": "user", "content": prompt}]

    response = client.chat.completions.create(
        messages=curr_input,
        model="gpt-3.5-turbo",
    )

    return int(response.choices[0].message.content.strip())


if __name__ == '__main__':
    user1 = User("1")
    memo1 = Memo("1")
    print(get_tax(memo1, user1))

