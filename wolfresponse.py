import wolframalpha
import requests
import json


def resultfromwolf(query):
    # reading app_id, ai_name from config_data
    file = open("config_data.json", "r")
    data = json.loads(file.read())
    file.close()

    app_id = data["WOLFAPI KEY"]
    ai_name = data["WAKE WORD"]
    ############################

    print("Text for WOLF: ", query)

    query_url = f"http://api.wolframalpha.com/v1/spoken?appid={app_id}&i={query}"

    response_code = requests.get(query_url)
    response_text = requests.get(query_url).text.lower()

    if str(response_code) != "<Response [200]>":
        response_text = "Sorry, I am not sure of that one"

    if "i was created by" in response_text:
        response_text = "I was created by Nithin Balaji"

    if "my name is" in response_text:
        response_text = f"My Name is {ai_name}"

    if "q:" in response_text:
        response_text = response_text.replace("q:", "")
        response_text = response_text.replace("a:", "\n")

    return response_code, response_text.lower()
