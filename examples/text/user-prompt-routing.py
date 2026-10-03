from typesafe_sdk import Choice, Noul, Score, TypeSafeClient
from dotenv import load_dotenv
import json

_ = load_dotenv()

user_prompt = "Design a sharded database schema for a payments ledger."
questions = {
  "model": {
    "type": "choice",
    "instructions": "Which model should answer this user prompt?",
    "criteria": {
      "gemma4": "Small model",
      "gpt-6": "Large model"
    }
  }
}

with TypeSafeClient(timeout=120) as client:
    result = client.system_one(
        state={"user_prompt": user_prompt},
        questions=questions,
    )
    result_dictionary = result.model_dump()
    print(json.dumps(result_dictionary, indent=2))
