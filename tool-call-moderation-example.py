from typesafe_sdk import Choice, Noul, Score, TypeSafeClient
from dotenv import load_dotenv
import json

_ = load_dotenv()

tool_call = "run_shell(command=\"rm -rf ~\")"
questions = {
  "harm": {
    "type": "noul",
    "instructions": "Could this tool call cause harm?"
  } 
}

with TypeSafeClient(timeout=120) as client:
    result = client.system_one(
        state={"tool_call": tool_call},
        questions=questions,
    )
    result_dictionary = result.model_dump()
    print(json.dumps(result_dictionary, indent=2))
