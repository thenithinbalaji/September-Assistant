import wikipedia


def resultfromwiki(query):
    print("Text for WIKI: ", query)
    try:
        result = wikipedia.summary(query, sentences=1).split("\n")[0]
    except:
        result = "What you tried to search on wikipedia sounded too vague. try asking something more specific"

    return result
