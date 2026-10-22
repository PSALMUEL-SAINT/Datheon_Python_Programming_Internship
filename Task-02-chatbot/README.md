
# Rule-Based Customer Support Chatbot

## Overview

This project is an interactive customer support chatbot built with Python. It uses regular expressions to recognize user messages and provides answers to common questions using a JSON FAQ dataset.

## Features

- Recognizes common greetings.
- Answers questions about business hours.
- Provides internship project submission instructions.
- Answers questions about certificate processing.
- Uses regular expressions for keyword and intent matching.
- Handles multiple supported intents in a single message.
- Normalizes user input using lowercase conversion and whitespace removal.
- Provides fallback responses for unrecognized questions.
- Supports `bye`, `exit`, and `quit` commands.
- Handles missing or invalid JSON files and interrupted input.

## Technologies Used

- Python 3
- `re` — regular expressions
- `json` — loading FAQ data
- `pathlib` — locating the dataset file

No third-party packages are required.

## Project Structure

```text
Task-02-Chatbot/
├── chatbot.py
├── sample_faq.json
└── README.md
```

## How to Run

1. Ensure `chatbot.py` and `sample_faq.json` are in the same folder.
2. Open the terminal in that folder.
3. Run:

   ```bash
   python chatbot.py
   ```

   On Windows, you can also use:

   ```powershell
   py chatbot.py
   ```

## Example Conversation

```text
Bot: Hello! How can I help you today?

You: What are your hours of operation?
Bot: We operate Monday through Friday from 9:00 AM to 6:00 PM IST.

You: How do I submit my internship project?
Bot: You can submit your public GitHub repository link through your Student Workspace.

You: When will I receive my certificate?
Bot: Certificates are reviewed and issued within 3-5 business days after your code review.

You: quit
Bot: Thank you for chatting with us. Goodbye!
```

## FAQ Dataset

The `sample_faq.json` file contains:

- `greetings`: recognized greeting phrases.
- `faqs`: questions and their corresponding answers.

You can update the answers by editing the JSON file while preserving valid JSON syntax.

## Error Handling

The chatbot handles missing FAQ files, invalid JSON, malformed FAQ entries, and interrupted terminal input.

## Limitations

The chatbot uses predefined rules rather than machine learning or a language model. New FAQ topics may require additional intent-matching rules in `chatbot.py`.

## Author

Created as part of a Python Programming Internship task.
