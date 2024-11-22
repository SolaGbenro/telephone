# Translation Telephone Game

A fun and interactive language translation game that demonstrates how messages can transform as they're translated through multiple languages, similar to the classic children's game "Telephone."

## Description

Translation Telephone is a Python application that takes a message and passes it through a series of language translations before finally translating it back to English. The game uses OpenAI's language models through the LangChain framework to perform the translations, allowing you to see how your message changes as it moves through different languages.

## Features

- Chain multiple language translations in sequence
- Configurable translation model (supports various OpenAI models)
- Adjustable delay between translations to manage API rate limits
- Detailed translation journey tracking
- Pretty-printed results showing the transformation at each step

## Prerequisites

- Python 3.8 or higher
- OpenAI API key
- LangChain v0.3

- Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

### Basic Usage

```python
from telephone import TranslationTelephone, print_game_results

# Create game instance
game = TranslationTelephone(model_name="gpt-4o-mini")

# Define your message and language chain
message = "Keep the change, ya filthy animal."
languages = ["French", "Japanese", "Russian", "Arabic", "Spanish"]

# Play the game
results = game.play_game(message, languages)

# Print results
print_game_results(results)
```

### Example Output

```
=== Translation Telephone Game Results ===

Original message: "Keep the change, ya filthy animal."

Translation journey:

1. English → French:
   "Garde la monnaie, espèce d'animal crasseux."

2. French → Japanese:
   "お釣りを取っておけ、この汚い動物め。"

3. Japanese → Russian:
   "Оставь себе сдачу, грязное животное."

4. Russian → Arabic:
   "احتفظ بالباقي، أيها الحيوان القذر."

5. Arabic → Spanish:
   "Quédate con el cambio, animal sucio."

Final translation back to English:
"Keep the change, you dirty animal."
```

### Customization Options

#### Using Different Models

You can specify different OpenAI models when initializing the game:

```python
# Using GPT-4
game = TranslationTelephone(model_name="gpt-4")

# Using GPT-3.5-turbo
game = TranslationTelephone(model_name="gpt-3.5-turbo")
```

#### Custom Language Chains

Create your own language translation chains:

```python
# European languages
languages_europe = ["French", "German", "Italian", "Spanish", "Portuguese"]

# Asian languages
languages_asia = ["Japanese", "Korean", "Mandarin", "Vietnamese", "Thai"]

# Mix and match as desired
languages_custom = ["French", "Arabic", "Japanese", "Hindi", "Spanish"]
```

## Error Handling

The application includes basic error handling for translation failures. If a translation fails, it will:
1. Print an error message
2. Return the input text unchanged
3. Continue with the next translation in the chain
