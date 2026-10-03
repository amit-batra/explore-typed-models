from typesafe_sdk import Choice, Noul, Score, TypeSafeClient
from dotenv import load_dotenv
import json

_ = load_dotenv()

ticket = "I was charged twice. Please refund the extra payment."
questions = {
    "team": Choice(
        instructions="Which team should handle this ticket?",
        criteria={
            "billing": "Payments and refunds",
            "technical": "Bugs and integrations",
            "other": "None of the above",
        },
    ),
    "refund": Noul(
        instructions="Does the customer explicitly ask for a refund?",
    ),
    "urgency": Score(
        instructions="How urgent is this ticket?",
        criteria=["Routine", "Soon", "Urgent"],
    ),
}

with TypeSafeClient(timeout=120) as client:
    result = client.system_one(
        state={"ticket": ticket},
        questions=questions,
    )
    result_dictionary = result.model_dump()
    print(json.dumps(result_dictionary, indent=2))
