# explore-typed-models

Example scripts demonstrating typed model inference using the [typesafe-sdk](https://github.com/typesafellm/typesafe) (System One endpoint). Each example prompts a local LLM to answer structured questions — choices, scoring, and unconstrained outputs — with type-safe results.

## Examples

| Script | Description |
| --- | --- |
| `customer-ticket-classification-example.py` | Classifies a support ticket by team, refund intent, and urgency. |
| `customer-ticket-sentiment-example.py` | Assesses whether a return is within policy, classifies it, and scores customer sentiment. |
| `user-prompt-routing-example.py` | Routes a user prompt to the appropriate destination. |
| `tool-call-moderation-example.py` | Moderates tool calls for safety. |

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com) running locally (default API at `http://localhost:11434`)
- The `nimble:9b` model installed: `ollama pull nimble:9b`

## Setup

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Configure your environment by copying the included `.env.example` to `.env` and updating the values as needed:

   ```bash
   cp .env.example .env
   ```

   - `TYPESAFE_BASE_URL` — TypeSafe/Ollama API base URL.
   - `TYPESAFE_API_KEY` — API key (any value works for local Ollama).
   - `TYPESAFE_DEFAULT_MODEL` — Model used when one isn't specified per request.

## Usage

Run any example script directly; it reads `.env` automatically:

```bash
python customer-ticket-classification-example.py
```

Each script prints the parsed result as indented JSON.

## Project layout

```
customer-ticket-classification-example.py
customer-ticket-sentiment-example.py
user-prompt-routing-example.py
tool-call-moderation-example.py
requirements.txt
.env
```
