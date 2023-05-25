"""
Translator Module
"""

import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

# Create an authenticator instance with the API key
AUTHENTICATOR = IAMAuthenticator(apikey)

# Create a language translator instance with the URL and authenticator
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=AUTHENTICATOR
)
LANGUAGE_TRANSLATOR.set_service_url(url)

def english_to_french(text): # Function to Translate Input from English to French
    """
    Translates English text to French.

    Args:
        text (str): The input text in English.

    Returns:
        str or None: The translated text in French, or None if the input is empty or None.
    """
    if text:
        translation = LANGUAGE_TRANSLATOR.translate(
            text=text,
            model_id='en-fr').get_result()
        translated_text = translation['translations'][0]['translation']
    else:
        translated_text = None
    return translated_text

def french_to_english(text):  # Function to Translate Input from French to English
    """
    Translates French text to English.

    Args:
        text (str): The input text in French.

    Returns:
        str or None: The translated text in English, or None if the input is empty or None.
    """
    if text:
        translation = LANGUAGE_TRANSLATOR.translate(
            text=text,
            model_id='fr-en').get_result()
        translated_text = translation['translations'][0]['translation']
    else:
        translated_text = None
    return translated_text
    