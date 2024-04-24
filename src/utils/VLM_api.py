import os
import base64
from openai import OpenAI

# open_ai_key = ""
open_ai_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key= open_ai_key)

def run_gpt4v(image_path, textual_prompt):
    """
    Uploads an image and a textual prompt to the GPT-4 Vision API and gets a response.

    :param image_path: Path to the image file.
    :param textual_prompt: Textual prompt to be used with the image.
    :return: Response from the GPT-4 Vision API.
    """
    # Read and encode the image file
    with open(image_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": textual_prompt},
                    {"type": "image", "image": encoded_image}
                ],
            }
        ],
    }

    response = client.chat.completions.create(**payload)
    pure_response = response.choices[0].message.content
    return pure_response
