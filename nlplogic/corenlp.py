from textblob import TextBlob
import wikipedia


def search_wikipedia(name):
    print(f"Searching for name: {name}")
    return wikipedia.search(name)


def summarize_wikipedia(name):
    print(f"Finding Wikipedia summary for name: {name}")
    return wikipedia.summary(name)


def get_text_blob(text):
    blob = TextBlob(text)
    return blob


def get_phrases(name):
    text = summarize_wikipedia(name)
    blob = get_text_blob(text)
    phrases = blob.noun_phrases
    return phrases


golden_state_warriors = wikipedia.summary("Golden State Warriors")
