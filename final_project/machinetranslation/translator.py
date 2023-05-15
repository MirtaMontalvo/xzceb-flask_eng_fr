"""
Translator Module
"""

import os
import json
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

API_KEY = os.environ['apikey']
URL = os.environ['url']

# Create an authenticator instance with the API key
AUTHENTICATOR = IAMAuthenticator(API_KEY)

# Create a language translator instance with the URL and authenticator
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=AUTHENTICATOR
)

# Set the service URL
LANGUAGE_TRANSLATOR.set_service_url(URL)

def englishToFrench(english_text):
    """
    Translates English text to French.
    """
    if not english_text:  # Check if english_text is empty
        return ''  # Return empty string
    translation_response = LANGUAGE_TRANSLATOR.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()
    french_text = translation_response['translations'][0]['translation']
    print(json.dumps(translation_response, indent=2, ensure_ascii=False))
    return french_text

def frenchToEnglish(french_text):
    """
    Translates French text to English.
    """
    if not french_text:  # Check if french_text is empty
        return ''  # Return empty string
    translation_response = LANGUAGE_TRANSLATOR.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()
    english_text = translation_response['translations'][0]['translation']
    print(json.dumps(translation_response, indent=2, ensure_ascii=False))
    return english_text
