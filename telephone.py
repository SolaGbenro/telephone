from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from typing import List
import time
from dotenv import load_dotenv

load_dotenv()


class TranslationTelephone:
    def __init__(self, model_name: str = "gpt-4o-mini"):
        """
        Initialize the Translation Telephone game.

        Args:
            model_name (str): The name of the model to use (default: "gpt-4o-mini")
        """
        self.llm = ChatOpenAI(
            temperature=0.0,
            model_name=model_name
        )

        # Create a translation prompt template
        self.translation_prompt = ChatPromptTemplate.from_template(
            "Translate the following text from {source_lang} to {target_lang}. "
            "Maintain the tone and style as much as possible:\n\n{text}"
        )

        self.translation_chain = self.translation_prompt | self.llm | StrOutputParser()

    def translate(self, text: str, source_lang: str, target_lang: str) -> str:
        """
        Translate text from source language to target language.

        Args:
            text (str): Text to translate
            source_lang (str): Source language
            target_lang (str): Target language

        Returns:
            str: Translated text
        """
        try:
            response = self.translation_chain.invoke({
                "source_lang": source_lang,
                "target_lang": target_lang,
                "text": text
            })
            # return response.strip()
            return response
        except Exception as e:
            print(f"Error during translation: {e}")
            return text

    def play_game(self, message: str, languages: List[str], delay: float = 1.0) -> dict:
        """
        Play the translation telephone game.

        Args:
            message (str): Initial message in English
            languages (List[str]): List of languages to translate through
            delay (float): Delay between API calls in seconds

        Returns:
            dict: Dictionary containing the game results
        """
        results = {
            "original": message,
            "translations": [],
            "final": None
        }

        current_text = message
        current_lang = "English"

        # Forward translation through all languages
        for target_lang in languages:
            time.sleep(delay)  # Add delay to avoid rate limiting

            translation = self.translate(text=current_text, source_lang=current_lang, target_lang=target_lang)
            cur_eng_translation = self.translate(text=translation, source_lang=target_lang, target_lang="English")
            results["translations"].append({
                "from": current_lang,
                "to": target_lang,
                "text": translation,
                "current_english_translation": cur_eng_translation
            })

            current_text = translation
            current_lang = target_lang

        # Translate back to English
        time.sleep(delay)
        final_translation = self.translate(current_text, current_lang, "English")
        results["final"] = final_translation

        return results


def print_game_results(results: dict):
    """
    Print the results of the translation telephone game in a readable format.

    Args:
        results (dict): Dictionary containing game results
    """
    print("\n=== Translation Telephone Game Results ===\n")
    print(f"Original message: \"{results['original']}\"\n")
    print("Translation journey:")

    for i, translation in enumerate(results["translations"], 1):
        print(f"\n{i}. {translation['from']} → {translation['to']}:")
        print(f"   \"{translation['text']}\"")
        print(f"   \"{translation['current_english_translation']}\"")

    print(f"\nFinal translation back to English:")
    print(f"\"{results['final']}\"\n")


# Example usage:
if __name__ == "__main__":

    # Create game instance
    game = TranslationTelephone(model_name="gpt-4o-mini")

    # Example message and languages
    # message = "The quick brown fox jumps over the lazy dog"
    message = "Keep the change, ya filthy animal."
    languages = ["French", "Japanese", "Russian", "Arabic", "Spanish"]

    # Play the game
    results = game.play_game(message, languages)

    # Print results
    print_game_results(results)
