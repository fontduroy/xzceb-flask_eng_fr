"""Functions for translating strings between English and French
    using IBM Watson."""

import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

def create_service():
    """Create an instance of LanguageTranslator to IBM Watson."""

    authenticator = IAMAuthenticator(apikey)
    language_translator = LanguageTranslatorV3(
        version='2018-05-01',
        authenticator=authenticator
    )

    language_translator.set_service_url(url)

    return language_translator

def english_to_french(english_text):
    """Translates a string from English to French"""

    if len(english_text) == 0:
        return None

    language_translator = create_service()

    translation = language_translator.translate(
        text=english_text,
        model_id='en-fr').get_result()

    french_json = json.dumps(translation, indent=2, ensure_ascii=False)

    french_text = json.JSONDecoder().decode(french_json)['translations'][0]['translation']

    print(french_text)
    return french_text


def french_to_english(french_text):
    """Translates a string from French to English."""

    if len(french_text) == 0:
        return None

    language_translator = create_service()

    translation = language_translator.translate(
        text=french_text,
        model_id='fr-en').get_result()

    english_json = json.dumps(translation, indent=2, ensure_ascii=False)

    english_text = json.JSONDecoder().decode(english_json)['translations'][0]['translation']

    print(english_text)
    return english_text

english_to_french("")
french_to_english("")
english_to_french("Hello")
french_to_english("Bonjour")
