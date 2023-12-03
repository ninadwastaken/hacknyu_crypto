import wolframalpha


def wolf(item):
    question = "price of " + item + " in NYC"
    app_id = "UJVXA4-674E3VU74G"
    client = wolframalpha.Client(app_id)
    # Stores the response fr
    res = client.query(question)

    # Includes only text from the response
    answer = next(res.results).text
    if answer == "(data not available)":
        return None

    return answer


print(wolf("gas"))
