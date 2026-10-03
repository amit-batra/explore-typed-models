# explore-typed-models

Example scripts demonstrating typed model inference using the [typesafe-sdk](https://github.com/typesafellm/typesafe) (System One endpoint). Each example prompts a local LLM to answer structured questions — choices, scoring, and unconstrained outputs — with type-safe results.

## Examples

| Script | Description |
| --- | --- |
| `examples/text/customer-ticket-classification.py` | Classifies a support ticket by team, refund intent, and urgency. |
| `examples/text/customer-ticket-sentiment-analysis.py` | Assesses whether a return is within policy, classifies it, and scores customer sentiment. |
| `examples/text/user-prompt-routing.py` | Routes a user prompt to the appropriate destination. |
| `examples/text/tool-call-moderation.py` | Moderates tool calls for safety. |
| `examples/multimodal/image-based-decision.py` | Reads an image and decides which occasion it represents, using the `clef-flash:9b` model. |

## Requirements

- Python 3.10+
- [Ollama](https://ollama.com) running locally (default API at `http://localhost:11434`)
- The `clef-flash:9b` model installed: `ollama pull clef-flash:9b`

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

Run any example script from the repo root; it reads `.env` automatically:

```bash
python examples/text/customer-ticket-classification.py
python examples/multimodal/image-based-decision.py
```

Each script prints the parsed result as indented JSON.

## Project layout

```
examples/
  text/
    customer-ticket-classification.py
    customer-ticket-sentiment-analysis.py
    user-prompt-routing.py
    tool-call-moderation.py
  multimodal/
    image-based-decision.py
    images/
      happy-birthday.png
requirements.txt
.env
```
