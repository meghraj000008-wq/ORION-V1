# ORION V1.5 - TOOLS.py - Internet + All Languages
# OWNER: MXLLVXW

import requests
import json

class ORION_TOOLS:
    def __init__(self):
        print("TOOLS: Internet + Translator Loaded")

    def internet_search(self, query):
        """
        Real internet search using DuckDuckGo + Wikipedia
        Works in Colab
        """
        print(f"[INTERNET] Searching: {query}")
        try:
            # Wikipedia search - free, no API key needed
            url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}"
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                data = r.json()
                return f"Wikipedia: {data.get('extract', '')[:500]}"

            # Fallback to DuckDuckGo Instant Answer
            url2 = f"https://api.duckduckgo.com/?q={query}&format=json"
            r2 = requests.get(url2, timeout=10)
            data2 = r2.json()
            abstract = data2.get("AbstractText", "")
            if abstract:
                return f"DuckDuckGo: {abstract[:500]}"

            return f"Search for '{query}' completed - No direct wiki, but I can reason from my world model"
        except Exception as e:
            return f"Internet error (offline mode): {e} - Using internal world model"

    def translate(self, text, target_lang="bn"):
        """
        Simple translator - uses MyMemory free API
        Supports 100+ languages
        """
        try:
            url = f"https://api.mymemory.translated.net/get?q={text}&langpair=en|{target_lang}"
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                translated = r.json()["responseData"]["translatedText"]
                return translated
            return text
        except:
            return text

    def speak_all_languages(self, text):
        """
        ORION will answer in user's language
        """
        # Detect if Bengali, Hindi, English etc - for now return as is
        # V2 will have full auto-detect
        return {
            "en": text,
            "bn": self.translate(text, "bn"),
            "hi": self.translate(text, "hi"),
            "es": self.translate(text, "es")
        }

# Test
if __name__ == "__main__":
    t = ORION_TOOLS()
    print(t.internet_search("artificial super intelligence"))
    print(t.translate("I will help humanity", "bn"))
