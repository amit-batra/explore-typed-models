from typesafe_sdk import Choice, Noul, Score, TypeSafeClient
from dotenv import load_dotenv
import json

_ = load_dotenv()

state = {
  "policy": "Returns are allowed within 30 days of purchase.",
  "request": "I bought these headphones 12 days ago and want to send them back.",
}

questions = {
  "eligible": Noul(
    instructions="Is this return within the allowed window?",
  ),

  "category": Choice(
    instructions="What kind of request is this?",
    criteria={
      "return": "The customer wants to send an item back.",
      "exchange": "The customer wants a different item instead.",
      "other": "None of the above.",
    },
  ),

  "sentiment": Score(
    instructions="How positive is the customer's message?",
    criteria=["Negative", "Neutral", "Positive"],
  )
}

with TypeSafeClient(timeout=120) as client:
    result = client.system_one(
        state=state,
        questions=questions,
    )
    result_dictionary = result.model_dump()
    print(json.dumps(result_dictionary, indent=2))
