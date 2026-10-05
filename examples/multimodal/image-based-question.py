from typesafe_sdk import Noul, TypeSafeClient
from dotenv import load_dotenv
import base64
import json
from pathlib import Path

_ = load_dotenv()

image_path = Path(__file__).resolve().parent / "images" / "taj-mahal.jpg"
with open(image_path, "rb") as image_file:
    image_base64 = base64.b64encode(image_file.read()).decode("ascii")

state = {
    "request": "An image is attached",
}

questions = {
    "is_taj_mahal": Noul(
        instructions="Is this a picture of the Taj Mahal?",
        criteria={
            "true": "The image shows the Taj Mahal.",
            "false": "The image does not show the Taj Mahal.",
        },
    ),
    "is_nighttime": Noul(
        instructions="Was this image captured during night-time?",
        criteria={
            "true": "The image was captured during night-time.",
            "false": "The image was not captured during night-time.",
        },
    ),
}

with TypeSafeClient(timeout=120) as client:
    result = client.system_one(
        state=state,
        questions=questions,
        extra_body={"images": [image_base64]},
    )
    result_dictionary = result.model_dump()
    print(json.dumps(result_dictionary, indent=2))

    # The noul answer reports a probability of "yes" (true) from 0 to 1.
    # Threshold at 0.5 to obtain a boolean response.
    is_taj_mahal = result.nouls["is_taj_mahal"].noul >= 0.5
    print("is_taj_mahal:", is_taj_mahal)

    is_nighttime = result.nouls["is_nighttime"].noul >= 0.5
    print("is_nighttime:", is_nighttime)

    assert is_nighttime is False, "Expected the model to report the image was not captured at night."
