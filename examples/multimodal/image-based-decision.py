from typesafe_sdk import Choice, Noul, Score, TypeSafeClient
from dotenv import load_dotenv
import base64
import json
from pathlib import Path

_ = load_dotenv()

image_path = Path(__file__).resolve().parent / "images" / "happy-birthday.png"
with open(image_path, "rb") as image_file:
    image_base64 = base64.b64encode(image_file.read()).decode("ascii")

state = {
    "request": "An image representing an occasion is attached",
}

questions = {
    "occasion": Choice(
        instructions="What occasion does this image represent?",
        criteria={
            "birthday": None,
            "anniversary": None,
            "graduation": None,
        },
    )
}

with TypeSafeClient(timeout=120) as client:
    result = client.system_one(
        state=state,
        questions=questions,
        extra_body={"images": [image_base64]},
    )
    result_dictionary = result.model_dump()
    print(json.dumps(result_dictionary, indent=2))
