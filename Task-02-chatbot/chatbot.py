
import json
import re
from pathlib import Path


# Locate the FAQ dataset in the same folder as this script.
FAQ_FILE = Path(__file__).parent / "sample_faq.json"


def load_faq_data():
    """Load greetings and FAQs from the JSON file."""
    try:
        with open(FAQ_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, dict):
            raise ValueError("The JSON data must be an object.")

        if not isinstance(data.get("greetings"), list):
            raise ValueError("The greetings section must be a list.")

        if not isinstance(data.get("faqs"), list):
            raise ValueError("The FAQs section must be a list.")

        # Validate FAQ entries before using them.
        for faq in data["faqs"]:
            if (
                not isinstance(faq, dict)
                or not isinstance(faq.get("question"), str)
                or not isinstance(faq.get("answer"), str)
            ):
                raise ValueError(
                    "Each FAQ must contain a question and an answer."
                )

        return data

    except FileNotFoundError:
        print(f"Error: Could not find {FAQ_FILE.name}.")
    except json.JSONDecodeError:
        print("Error: The FAQ file contains invalid JSON.")
    except (OSError, ValueError) as error:
        print(f"Error loading FAQ data: {error}")

    return None


def normalize_input(message):
    """Normalize user input for consistent matching."""
    return message.strip().lower()


def compile_greetings(greetings):
    """Create regex patterns for the configured greetings."""
    patterns = []

    for greeting in greetings:
        if isinstance(greeting, str) and greeting.strip():
            # Escape special regex characters in the dataset.
            pattern = re.compile(
                rf"(?<!\w){re.escape(greeting.strip())}(?!\w)",
                re.IGNORECASE,
            )
            patterns.append(pattern)

    return patterns


def contains_match(patterns, message):
    """Return True if any pattern matches the message."""
    return any(pattern.search(message) for pattern in patterns)


def identify_faqs(message, faqs):
    """Find all FAQ intents that match the user's message."""
    intent_patterns = {
        "hours": re.compile(
            r"\b(hours?|opening hours?|business hours?|"
            r"operating hours?|operation|open|close|closing|"
            r"working hours?|office hours?)\b",
            re.IGNORECASE,
        ),
        "internship_project": re.compile(
            r"\b(internship project|project submission|"
            r"submit|submission|upload|turn in|"
            r"github|student workspace)\b",
            re.IGNORECASE,
        ),
        "certificate": re.compile(
            r"\b(certificate|certificates|certification|"
            r"issued|issuance|receive my certificate|"
            r"get my certificate)\b",
            re.IGNORECASE,
        ),
    }

    # Associate each FAQ with its intent.
    faq_intents = {
        "hours": 0,
        "internship_project": 1,
        "certificate": 2,
    }

    matched_faqs = []

    for intent, pattern in intent_patterns.items():
        if pattern.search(message):
            index = faq_intents[intent]

            # Use the actual answer from the JSON dataset.
            if index < len(faqs):
                matched_faqs.append(faqs[index])

    return matched_faqs


def get_response(message, data, greeting_patterns):
    """Generate responses for greetings, FAQs and unknown queries."""
    message = normalize_input(message)

    if not message:
        return ["Please enter a message so I can help you."]

    responses = []

    # Recognize greetings, including greetings combined with questions.
    if contains_match(greeting_patterns, message):
        responses.append(
            "Hello! Welcome to customer support. How can I help you today?"
        )

    # Match every FAQ intent found in the message.
    matched_faqs = identify_faqs(message, data["faqs"])

    for faq in matched_faqs:
        responses.append(faq["answer"])

    # If no rule matched, use a helpful fallback.
    if not responses:
        responses.append(
            "I'm sorry, I didn't understand your question. "
            "You can ask about business hours, internship project "
            "submission, or certificates."
        )

    return responses


def chatbot():
    """Run the interactive customer support chatbot."""
    data = load_faq_data()

    if data is None:
        print("Chatbot could not start because the FAQ data is unavailable.")
        return

    greeting_patterns = compile_greetings(data["greetings"])

    print("=" * 48)
    print("       CUSTOMER SUPPORT CHATBOT")
    print("=" * 48)
    print("Bot: Hello! How can I help you today?")
    print("Bot: Type 'bye', 'exit', or 'quit' to end the chat.")

    while True:
        try:
            user_input = input("\nYou: ")
        except (EOFError, KeyboardInterrupt):
            print("\nBot: Thank you for chatting. Goodbye!")
            break

        message = normalize_input(user_input)

        # Exit only when the entire input is an exit command.
        if re.fullmatch(r"(bye|exit|quit)", message):
            print("Bot: Thank you for chatting with us. Goodbye!")
            break

        responses = get_response(message, data, greeting_patterns)

        for response in responses:
            print(f"Bot: {response}")


if __name__ == "__main__":
    chatbot()
