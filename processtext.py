from random import randint, choice
from more_itertools import random_combination
from wikiresponse import *
from wolfresponse import *
import webbrowser
import os
import json


def processtext(query):
    # loading config_data into data
    file = open("config_data.json", "r")
    data = json.loads(file.read())
    file.close()

    # setting default browser path
    default_browser_path = data["DEFAULT BROWSER PATH"]

    query = query.lower()
    query = query.strip()

    # default response code
    response_code = "<Response [200]>"

    # removing september from query
    if query[:9] == "september":
        query = query[10:]

    if query in ["hey september", "hello september", "hai", "hai september"]:
        query = "hello"

    query = query.replace("hey september", "")
    query = query.replace("hello september", "")
    query = query.replace("hai september", "")
    query = query.replace("8 september", "")

    query = query.strip()
    ###########################################

    print("Stripped Text for processing: ", query)

    if len(query) == 0:
        response_text = "How can I help you?"

    elif "from wikipedia" in query or "from wiki" in query:
        query = query.replace("from wikipedia", "")
        query = query.replace("from wiki", "")
        query = query.strip()

        response_code = "<Response [200]>"

        if len(query) > 0:
            response_text = resultfromwiki(query)
        else:
            response_text = "What? what should i search from wikipedia?"

    elif "open chrome" in query or "open google chrome" in query:
        response_text = "opening chrome"
        os.system(f'start "" "{data["CHROME PATH"]}"')

    elif (
        "close chrome" in query
        or "close google chrome" in query
        or "quit chrome" in query
        or "quit google chrome" in query
        or "exit chrome" in query
        or "exit google chrome" in query
    ):
        response_text = "shutting down chrome"
        os.system(f"taskkill /im chrome.exe /f")

    elif (
        "open edge" in query
        or "open microsoft edge" in query
        or "open internet explorer" in query
    ):
        response_text = "opening edge"
        os.system(f'start "" "{data["EDGE PATH"]}"')

    elif (
        "close edge" in query
        or "close microsoft edge" in query
        or "close interent explorer" in query
        or "quit edge" in query
        or "quit microsoft edge" in query
        or "exit edge" in query
    ):
        response_text = "shutting down edge"
        os.system(f"taskkill /im msedge.exe /f")

    elif "open notepad" in query:
        response_text = "opening notepad"
        os.system(f'start "" "{data["NOTEPAD PATH"]}"')

    elif "close notepad" in query or "quit notepad" in query:
        response_text = "closing notepad"
        os.system(f"taskkill /im notepad.exe /f")

    elif (
        "open vscode" in query
        or "open visual studio code" in query
        or "open vs code" in query
    ):
        response_text = "opening vs code"
        os.system(f'start "" "{data["VSCODE PATH"]}"')

    elif "close vs code" in query or "quit vs code" in query:
        response_text = "closing vs code"
        os.system(f"taskkill /im Code.exe /f")

    elif "open discord" in query:
        response_text = "opening discord"
        os.system(f'start "" "{data["DISCORD PATH"]}"')

    elif "close discord" in query or "quit discord" in query:
        response_text = "shutting down discord"
        os.system(f"taskkill /im discord.exe /f")

    elif "open setting" in query:
        response_text = "opening settings"
        response_code = "settings code"

    elif "open calculator" in query:
        response_text = "opening calculator"
        os.system(f'start "" "{data["CALCULATOR PATH"]}"')

    elif "close calculator" in query or "quit calculator" in query:
        response_text = "quitting the process"
        os.system(f"taskkill /im calculator.exe /f")

    elif "open youtube" in query:
        response_text = "trying to Open Youtube on browser"

        webbrowser.register(
            "chrome", None, webbrowser.BackgroundBrowser(default_browser_path)
        )
        webbrowser.get("chrome").open("youtube.com")

    elif "open gmail" in query:
        response_text = "trying to Open Gmail on browser"

        webbrowser.register(
            "chrome", None, webbrowser.BackgroundBrowser(default_browser_path)
        )
        webbrowser.get("chrome").open("mail.google.com")

    elif "open google" in query:
        response_text = "trying to Open google on browser"

        webbrowser.register(
            "chrome", None, webbrowser.BackgroundBrowser(default_browser_path)
        )
        webbrowser.get("chrome").open("google.com")

    elif "open netflix" in query:
        response_text = "trying to Open netlfix on browser"

        webbrowser.register(
            "chrome", None, webbrowser.BackgroundBrowser(default_browser_path)
        )
        webbrowser.get("chrome").open("netflix.com")

    elif "open github" in query:
        response_text = "trying to Open github on browser"

        webbrowser.register(
            "chrome", None, webbrowser.BackgroundBrowser(default_browser_path)
        )
        webbrowser.get("chrome").open("github.com")

    elif query[:4] == "open" and len(query) > 4:
        response_text = "started search"
        webbrowser.register(
            "chrome", None, webbrowser.BackgroundBrowser(default_browser_path)
        )
        query = query[4:]
        query = query.strip()

        if "on google" in query:
            query = query.replace("on google", "")
            webbrowser.get("chrome").open(f"https://www.google.com/search?q={query}")

        elif "on youtube" in query:
            query = query.replace("on youtube", "")
            webbrowser.get("chrome").open(
                f"https://www.youtube.com/results?search_query={query}"
            )

        else:
            webbrowser.get("chrome").open(f"https://www.google.com/search?q={query}")

    elif query[:10] == "search for" and len(query) > 10:
        response_text = "started search"
        webbrowser.register(
            "chrome", None, webbrowser.BackgroundBrowser(default_browser_path)
        )
        query = query.replace("search for", "")

        if "on google" in query:
            query = query.replace("on google", "")
            webbrowser.get("chrome").open(f"https://www.google.com/search?q={query}")

        elif "on youtube" in query:
            query = query.replace("on youtube", "")
            webbrowser.get("chrome").open(
                f"https://www.youtube.com/results?search_query={query}"
            )

        else:
            webbrowser.get("chrome").open(f"https://www.google.com/search?q={query}")

    elif query[:6] == "search" and len(query) > 6:
        response_text = "started search"
        webbrowser.register(
            "chrome", None, webbrowser.BackgroundBrowser(default_browser_path)
        )
        query = query[6:]

        if "on google" in query:
            query = query.replace("on google", "")
            webbrowser.get("chrome").open(f"https://www.google.com/search?q={query}")

        elif "google for" in query:
            query = query.replace("google for", "")
            webbrowser.get("chrome").open(f"https://www.google.com/search?q={query}")

        elif "on youtube" in query:
            query = query.replace("on youtube", "")
            webbrowser.get("chrome").open(
                f"https://www.youtube.com/results?search_query={query}"
            )

        elif "youtube for" in query:
            query = query.replace("youtube for", "")
            webbrowser.get("chrome").open(
                f"https://www.youtube.com/results?search_query={query}"
            )

        else:
            webbrowser.get("chrome").open(f"https://www.google.com/search?q={query}")

    elif query[:4] == "play" and len(query) > 4:
        query = query[4:]
        response_text = "started search"
        webbrowser.register(
            "chrome", None, webbrowser.BackgroundBrowser(default_browser_path)
        )

        if "on youtube" in query:
            query = query.replace("on youtube", "")
            webbrowser.get("chrome").open(
                f"https://www.youtube.com/results?search_query={query}"
            )

        elif "from youtube" in query:
            query = query.replace("from youtube", "")
            webbrowser.get("chrome").open(
                f"https://www.youtube.com/results?search_query={query}"
            )

        else:
            webbrowser.get("chrome").open(
                f"https://www.youtube.com/results?search_query={query}"
            )

    elif query[:6] == "google" and len(query) > 6:
        if "google for" in query:
            query = query.replace("google for", "")
        else:
            query = query[6:]
        response_text = "started search"
        webbrowser.register(
            "chrome", None, webbrowser.BackgroundBrowser(default_browser_path)
        )
        webbrowser.get("chrome").open(f"https://www.google.com/search?q={query}")

    elif "on google" in query:
        query = query.replace("on google", "")
        webbrowser.get("chrome").open(f"https://www.google.com/search?q={query}")

    elif query == "search":
        response_text = "went to search nothing and found nothing"

    elif query == "stop":
        response_text = "okay"

    elif query.split()[0] == "say":
        response_text = query.strip()[3:]

    elif query.split()[0] == "repeat":
        response_text = query.strip()[6:]

    elif "flip a coin" in query:
        flip_a_coin_list = ["Heads", "Tails"]
        response_text = f"It landed on {choice( flip_a_coin_list )}"

    elif "roll a die" in query:
        roll_a_die_list = [1, 2, 3, 4, 5, 6]
        response_text = f"It landed on {choice(roll_a_die_list)}"

    elif query in ["bye", "bye bye", "exit", "close", "quit", "shut down", "good bye"]:
        response_code = "bye code"
        response_text = "good bye, happy to see you go"

    else:
        response_code, response_text = resultfromwolf(query)

    return response_code, response_text.lower()
